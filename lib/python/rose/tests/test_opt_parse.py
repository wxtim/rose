# -*- coding: utf-8 -*-
# -----------------------------------------------------------------------------
# Copyright (C) 2012-2019 British Crown (Met Office) & Contributors.
#
# This file is part of Rose, a framework for meteorological suites.
#
# Rose is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Rose is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Rose. If not, see <http://www.gnu.org/licenses/>.
# -----------------------------------------------------------------------------
# Tests for rose.opt_parse.PY2

import unittest
# import sys
import os

# This is clearly not the right way to do things, but it's a good first step
# sys.path.append('/home/h02/tpilling/metomi/rose.git/lib/python')

from rose.opt_parse import RoseOptionParser

os.environ['ROSE_HOME_BIN'] = 'ROSE-FUDGE' 

BASIC_KWARGDICT = {'debug_mode': None,
                   'profile_mode': False,
                   'quietness': 0,
                   'verbosity': 1}
BASIC_ARGLIST = []
  

class TestRoseOptionParser(unittest.TestCase):
    def test_init(self):
        "Create a basic instance of RoseOption parser without args or kwargs"
        x = RoseOptionParser()
        self.assertEqual(str(type(x)),
                         "<class 'rose.opt_parse.RoseOptionParser'>",
                         "Trivial Test")
        opts, args = x.parse_args()
        self.assertEqual(opts, BASIC_KWARGDICT)
        self.assertEqual(args, BASIC_ARGLIST)

    def test_add_my_options_valid_all(self):
        """For each of the optkeys available in the module call rose.opt_parse
        and check that the RoseOptionParser.parse_args() produces the
        desired result."""
        # Set up list of keys to test, only excluding the ones
        # from BASIC_KWARGDICT
        optkeys = [key for key in list(RoseOptionParser.OPTIONS.keys())\
                   if key not in ['debug_mode', 'profile_mode',
                                  'quietness', 'verbosity']]

        for optkey in optkeys:
            optval = RoseOptionParser.OPTIONS[optkey][1]
            with self.subTest(optional_key=optkey):

                # Use RoseOptionParser
                x = RoseOptionParser()
                x.add_my_options(optkey)
                opts, _ = x.parse_args()
                
                # Set up expected output values
                new_kwargdict = BASIC_KWARGDICT.copy()
                newkey = optkey
                try:
                    newkey = optval['dest']
                except KeyError:
                    pass
                newval = None
                try:
                    newval = optval['default']
                except KeyError:
                    pass
                new_kwargdict[newkey] = newval

                # Message is req'd because assertEqual won't show full diff
                msg = "\nexpected: {}\n     got: {}"
                self.assertEqual(opts,
                                 new_kwargdict,
                                 msg.format(new_kwargdict, opts))

if __name__ == "__main__":
    unittest.main()