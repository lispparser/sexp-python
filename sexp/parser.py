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


from sexp.value import Boolean, Integer, Real, Cons


class TextIO:

    def __init__(self, text):
        self.text = text
        self.i = 0

        self.line = 1
        self.column = 0

    def getchar(self):
        c = self.text[self.i]
        if c == '\n':
            self.line += 1
            self.column = 0
        else:
            self.column += 1
        self.i += 1
        return c

    def eof(self):
        return self.i >= len(self.text)

    def ungetchar(self):
        self.i -= 1


class Parser:

    @staticmethod
    def from_file(filename):
        with open(filename, "r") as fin:
            return Parser.from_string(fin.read())

    @staticmethod
    def from_string(text):
        parser = Parser(TextIO(text))
        return parser.parse()

    def __init__(self, io):
        self.io = io
        self.stack = [[]]
        self.state = self.parse_list
        self.atom = ""

    def parse_list(self, c):
        if c == '(':
            self.stack.append([])
        elif c == ')':
            self.stack[-2].append(self.stack.pop())
        elif c == "\"":
            self.state = self.parse_string
            self.atom = ""
        elif c == ";":
            self.state = self.parse_comment
        elif c.isalpha():
            self.state = self.parse_symbol
            self.atom = c
        elif c.isdigit():
            self.state = self.parse_number
            self.atom = c
        elif c.isspace():
            pass
        else:
            raise Exception("%d:%d: error: unexpected character: '%s'" % (self.io.line, self.io.column, c))

    def parse_comments(self, c):
        if c == '\n':
            self.state = self.parse_list

    def parse_string(self, c):
        if c == "\\":
            self.atom += self.io.getchar()
        elif c == "\"":
            self.stack[-1].append(self.atom)
            self.state = self.parse_list
        else:
            self.atom += c

    def parse_number(self, c):
        if not c.isdigit() or c != ".":
            self.stack[-1].append(int(self.atom))
            self.state = self.parse_list
            self.io.ungetchar()
        else:
            self.atom += c

    def parse_symbol(self, c):
        if c.isspace() or c == '(' or c == ')':
            self.stack[-1].append(self.atom)
            self.state = self.parse_list
            self.io.ungetchar()
        else:
            self.atom += c

    def parse(self):
        while not self.io.eof():
            c = self.io.getchar()
            self.state(c)

        if len(self.stack) == 1:
            return self.stack[0]
        else:
            raise Exception("error: list not closed")


# EOF #