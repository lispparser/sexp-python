#!/usr/bin/env python

# Copyright (c) 2014 Ingo Ruhnke <grumbel@gmail.com>
#
# This software is provided 'as-is', without any express or implied
# warranty. In no event will the authors be held liable for any damages
# arising from the use of this software.
#
# Permission is granted to anyone to use this software for any purpose,
# including commercial applications, and to alter it and redistribute it
# freely, subject to the following restrictions:
#
# 1. The origin of this software must not be misrepresented; you must not
#    claim that you wrote the original software. If you use this software
#    in a product, an acknowledgment in the product documentation would be
#    appreciated but is not required.
# 2. Altered source versions must be plainly marked as such, and must not be
#    misrepresented as being the original software.
# 3. This notice may not be removed or altered from any source distribution.

import re

def parse(text):
    stack = [[]]
    state = 'list'
    i = 0
    while i < len(text):
        c = text[i]

        if state == 'list':
            if c == '(':
                stack.append([])
            elif c == ')':
                tmp = stack.pop()
                stack[-1].append(tmp)
            elif c == "\"":
                state = 'string'
                stack.append("")
            elif c == ";":
                state = 'comment'
            elif str.isalpha(c):
                state = 'symbol'
                stack.append(c)
            elif str.isdigit(c):
                state = 'number'
                stack.append(c)
            elif str.isspace(c):
                pass
            else:
                raise "error"
        elif state == 'comment':
            if c == '\n':
                state = 'list'
            else:
                pass
        elif state == 'string':
            if c == "\\":
                pass
            elif c == "\"":
                tmp = stack.pop()
                stack[-1].append(tmp)
                state = 'list'                
            else:
                stack[-1] = stack[-1] + c
        elif state == 'number':
            if not str.isdigit(c) or c != ".":
                tmp = stack.pop()
                stack[-1].append(int(tmp))
                state = 'list'
                i -= 1
            else:
                stack[-1] = stack[-1] + c           
        elif state == 'symbol':
            if str.isspace(c) or c == '(' or c == ')':
                tmp = stack.pop()
                stack[-1].append(tmp)
                state = 'list'
                i -= 1
            else:
                stack[-1] = stack[-1] + c

        # print c, stack

        i += 1

    return stack[0]

if __name__ == "__main__":
    print "parsing..."
    result = parse(r'(() ("bar" foo) ()) () bar ')
    print "1.", result
    print "2.", parse(""";;comment
    ("Hello World" 5 1 123) ("Hello" 123 123 "foobar") ;; comment""")
    

# EOF #
