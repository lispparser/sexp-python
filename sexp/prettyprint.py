# SExp - A S-Expression Parser for Python
# Copyright (c) 2018 Ingo Ruhnke <grumbel@gmail.com>
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


from sexp import Value, String, is_list


def pretty_print(sx: Value, indent: int, fout):
    _pretty_print(sx, 1, indent, fout)
    fout.write("\n")


def _pretty_print(sx: Value, depth: int, indent: int, fout):
    if sx.is_array():
        fout.write("(")
        fout.write(str(sx[0]))

        if len(sx) > 1 and sx[1].is_array() and sx[1][0].value != "_":
            fout.write("\n")
            for i in range(1, len(sx)):
                if sx[i].is_array():
                    fout.write(depth * indent * " ")
                    _pretty_print(sx[i], depth + 1, indent, fout)
                else:
                    fout.write(depth * indent * " ")
                    fout.write(str(sx[i]))

                if i != len(sx) - 1:
                    fout.write("\n")

            fout.write("\n" + (depth - 1) * indent * " " + ")")
        else:
            for i in range(1, len(sx)):
                fout.write(" ")
                fout.write(str(sx[i]))
            fout.write(")")
    else:
        fout.write(str(sx))


# EOF #
