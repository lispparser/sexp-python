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


import unittest
import sexp


class Value(unittest.TestCase):

    def test_boolean(self):
        v = sexp.Boolean(True)
        self.assertEqual(str(v), "#t")

        v = sexp.Boolean(False)
        self.assertEqual(str(v), "#f")

    def test_cons(self):
        v = sexp.Cons(sexp.Integer(5), sexp.Integer(5))
        self.assertEqual(str(v), "(5 . 5)")

        v = sexp.Cons(sexp.Integer(1),
                      sexp.Cons(sexp.Integer(2),
                                sexp.Cons(sexp.Integer(3),
                                          sexp.Cons(sexp.Integer(4),
                                                    sexp.Nil()))))
        self.assertEqual(str(v), "(1 2 3 4)")

    def test_string(self):
        self.assertEqual(str(sexp.String("HelloWorld")), '"HelloWorld"')
        self.assertEqual(str(sexp.String("Hello\nWorld")), "\"Hello\\nWorld\"")
        self.assertEqual(str(sexp.String("Hello\"World")), "\"Hello\\\"World\"")

    def test_list(self):
        v = sexp.make_list(sexp.Integer(1),
                           sexp.Integer(2),
                           sexp.Integer(3),
                           sexp.Integer(4))
        self.assertEqual(str(v), "(1 2 3 4)")

    def test_array(self):
        v = sexp.Array([1, 2, 3, 4, 5], pos=(1, 5))
        self.assertEqual(str(v), "(1 2 3 4 5)")

    def test_eq(self):
        self.assertTrue(sexp.Boolean(True) == sexp.Boolean(True))
        self.assertEqual(sexp.Boolean(True), sexp.Boolean(True))
        self.assertEqual(sexp.Integer(1), sexp.Integer(1))
        self.assertEqual(sexp.Real(5), sexp.Real(5))
        self.assertEqual(sexp.String("HelloWorld"), sexp.String("HelloWorld"))
        self.assertEqual(sexp.Symbol("HelloWorld"), sexp.Symbol("HelloWorld"))


if __name__ == '__main__':
    unittest.main()


# EOF #
