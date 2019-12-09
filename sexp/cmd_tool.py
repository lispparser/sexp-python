# SExp - A S-Expression Parser for Python
# Copyright (c) 2015 Ingo Ruhnke <grumbel@gmail.com>
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


from typing import List, Optional

import sys
import argparse
import sexp


def parse_args(args: List[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="S-Expresion Tool")
    parser.add_argument("CMD", nargs=1)
    parser.add_argument("FILE", nargs='+')
    parser.add_argument('-v', '--verbose', action='store_true', default=False,
                        help="Be verbose")
    parser.add_argument('-x', '--exclude', metavar="SEXPPATH", action='append',
                        help="Exclude SEXPPATH from output")
    parser.add_argument('-m', '--modify', action='store_true', default=False,
                        help="Modify files in place")

    # subparsers = parser.add_subparsers(title='subcommands',
    #                                    description='valid subcommands',
    #                                    help='additional help')

    return parser.parse_args(args)


def flatten_traverse(sx, parents, excludes: List[List[str]], context: Optional[str]):
    if sx.is_array() and sx[0].is_symbol():
        head = sx[0]
        tail = sx[1:]

        parents.append(str(head))

        if parents in excludes:
            print("skipping {}".format(parents))
        else:
            for cx in tail:
                flatten_traverse(cx, parents=parents[:], excludes=excludes, context=context)
    else:
        print("{}:{}:{}: {} = {}".format(context, sx.pos[0], sx.pos[1], ".".join([str(x) for x in parents]), sx))


def main(argv: List[str]) -> None:
    args = parse_args(argv[1:])
    for filename in args.FILE:
        try:
            sxs = sexp.Parser.from_file(filename)
        except Exception as err:
            print(filename, err)
        else:
            if False:
                # split string exclude into path exclude
                excludes = [x.split(".") for x in args.exclude]

                for sx in sxs:
                    flatten_traverse(sx, [], excludes=excludes, context=filename)
            else:
                if args.modify:
                    print("rewriting {}".format(filename))
                    try:
                        with open(filename, "w") as fout:
                            for sx in sxs:
                                sexp.pretty_print(sx, indent=2, fout=fout)
                    except:
                        print("error rewriting {}".format(filename))
                else:
                    for sx in sxs:
                        sexp.pretty_print(sx, indent=2, fout=sys.stdout)


def main_entrypoint() -> None:
    main(sys.argv)


# EOF #
