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
from sexp.parser import Parser
from sexp.value import Integer, Real, Array


class ParserTest(unittest.TestCase):

    def cmp(self, sxi_str, sxo_str):
        self.assertEqual(str(Parser.from_string(sxi_str)), sxo_str)

    def test_parse(self):
        sx1 = Parser.from_string("(1.0 2 3 4 5)")
        sx2 = [Array([Real(1.0), Integer(2), Integer(3), Integer(4), Integer(5)])]
        self.assertEqual(sx1, sx2)

        self.cmp('(() ("bar" foo) ()) () bar ',
                 '[(() ("bar" foo) ()), (), bar]')

        self.cmp(';;comment\n("Hello World" 5 1 123) ("Hello" 123 123 "foobar") ;; comment',
                 '[("Hello World" 5 1 123), ("Hello" 123 123 "foobar")]')

        self.cmp('(8(8)8)',
                 '[(8 (8) 8)]')

        self.cmp('',
                 '[]')

        self.cmp('  ',
                 '[]')

        sxi = Parser.from_file("tests/white.stf")
        # self.assertEqual(sxi, sxo)


# EOF #
