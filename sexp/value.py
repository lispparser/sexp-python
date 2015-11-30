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


class Value:

    def __init__(self, pos):
        self.pos = pos

    def is_nil(self):
        return False

    def is_boolean(self):
        return False

    def is_integer(self):
        return False

    def is_real(self):
        return False

    def is_cons(self):
        return False

    def is_string(self):
        return False

    def is_symbol(self):
        return False

    def is_array(self):
        return False

    def line():
        return self.pos[0]

    def column():
        return self.pos[1]


class Nil(Value):

    def __init__(self, pos=None):
        super().__init__(pos)

    def is_nil(self):
        return True

    def __str__(self):
        return "()"


class Boolean(Value):

    def __init__(self, v, pos=None):
        super().__init__(pos)
        self.value = v

    def is_boolean(self):
        return True

    def __str__(self):
        if self.value:
            return "#t"
        else:
            return "#f"


class Integer(Value):

    def __init__(self, v, pos=None):
        super().__init__(pos)
        self.value = v

    def is_integer(self):
        return True

    def __str__(self):
        return str(self.value)


class Real(Value):

    def __init__(self, v, pos=None):
        super().__init__(pos)
        self.value = v

    def is_real(self):
        return True

    def __str__(self):
        return str(self.value)


class String(Value):

    def __init__(self, v, pos=None):
        super().__init__(pos)
        self.value = v

    def is_string(self):
        return True

    def __str__(self):
        return str(self.value)


class Symbol(Value):

    def __init__(self, v, pos=None):
        super().__init__(pos)
        self.value = v

    def is_symbol(self):
        return True

    def __str__(self):
        return str(self.value)


class Cons(Value):

    def __init__(self, car, cdr, pos=None):
        super().__init__(pos)
        self.car = car
        self.cdr = cdr

    def is_cons(self):
        return True

    def get_car(self):
        return self.car

    def get_cdr(self):
        return self.cdr

    def __str__(self):
        result = "("

        cur = self
        while not cur.is_nil():
            result += str(cur.car)
            if cur.cdr.is_cons():
                result += " "
                cur = cur.cdr
            elif cur.cdr.is_nil():
                break
            else:
                result += " . " + str(cur.cdr)
                break

        result += ")"
        return result


class Array(Value):

    def __init__(self, *values, pos=None):
        self.values = values

    def is_array(self):
        return True

    def __str__(self):
        return "#(" + " ".join([str(v) for v in self.values]) + ")"


def make_list(*values):
    if not values:
        return Nil()
    else:
        return Cons(values[0], make_list(*values[1:]))


# EOF #
