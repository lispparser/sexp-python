# SExp - A S-Expression Parser for Python
# Copyright (C) 2015 Ingo Ruhnke <grumbel@gmail.com>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

class Parser:

    @staticmethod
    def from_file(filename):
        with open(filename, "r") as fin:
            return from_string(fin.read())

    @staticmethod
    def from_string(text):
        stack = [[]]
        state = 'list'
        i = 0
        line = 1
        column = 0
        while i < len(text):
            c = text[i]
            if c == '\n':
                line += 1
                column = 0
            else:
                column += 1

            if state == 'list':
                if c == '(':
                    stack.append([])
                elif c == ')':
                    stack[-2].append(stack.pop())
                elif c == "\"":
                    state = 'string'
                    atom = ""
                elif c == ";":
                    state = 'comment'
                elif c.isalpha():
                    state = 'symbol'
                    atom = c
                elif c.isdigit():
                    state = 'number'
                    atom = c
                elif c.isspace():
                    pass
                else:
                    raise Exception("%d:%d: error: unexpected character: '%s'" % (line, column, c))

            elif state == 'comment':
                if c == '\n':
                    state = 'list'
                else:
                    pass

            elif state == 'string':
                if c == "\\":
                    i += 1
                    atom += text[i]
                elif c == "\"":
                    stack[-1].append(atom)
                    state = 'list'
                else:
                    atom += c

            elif state == 'number':
                if not c.isdigit() or c != ".":
                    stack[-1].append(int(atom))
                    state = 'list'
                    i -= 1
                else:
                    atom += c

            elif state == 'symbol':
                if c.isspace() or c == '(' or c == ')':
                    stack[-1].append(atom)
                    state = 'list'
                    i -= 1
                else:
                    atom += c

            # print c, stack

            i += 1

        if len(stack) == 1:
            return stack[0]
        else:
            raise Exception("error: list not closed")


# EOF #
