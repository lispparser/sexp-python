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

    def test_parse(self):
        sx1 = Parser.from_string("(1.0 2 3 4 5)")
        sx2 = [Array([Real(1.0), Integer(2), Integer(3), Integer(4), Integer(5)])]
        self.assertEqual(sx1, sx2)


# EOF #
