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
"""
Convenient functions for searching resource files.
"""

import unittest
import os
from rose.resource import (get_util_home, ResourceLocator)


class Test_get_util_home(unittest.TestCase):
    def test_ROSE_HOME_not_in_env(self):
        """Checks whether get_util_home correctly finds ROSE_HOME in the event
        of ROSE_HOME being unset.
        """
        if "ROSE_HOME" in os.environ:
            os.unsetenv("ROSE_HOME")

        self.assertEqual(get_util_home(),
                         os.getcwd())


class TestResourceLocator(unittest.TestCase):
    def test_get_doc_url(self):
        # Utterly trivial test :(
        resource_locator_instance = ResourceLocator()
        url = resource_locator_instance.get_doc_url()
        self.assertEqual(url, f'file://{os.getcwd()}/doc/')

    def test_get_synopsis_exceptIOError(self):
        # Check that
        ...