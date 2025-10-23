# Copyright (C) British Crown (Met Office) & Contributors.
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
"""Tests for metomi/rose/checksum.py"""

from hashlib import md5
import pytest
from types import SimpleNamespace

from metomi.rose.checksum import _get_hexdigest, get_checksum



def test__get_hexdigest_path(tmp_path):
    """Function recognizes strings and handles.
    """
    input_ = b'hello world'
    expect = md5(input_).hexdigest()
    foo = tmp_path / 'foo'
    foo.write_text('hello world')

    # Pass a filepath to function
    assert _get_hexdigest('md5', str(foo)) == expect

    # Pass a filepath to function
    with open(str(foo), 'rb') as handle:
        assert _get_hexdigest('md5', handle) == expect


def test_get_hexdigest_symlinks(tmp_path):
    link = tmp_path / 'link'
    missing = tmp_path / 'missing'
    # missing.touch()
    link.symlink_to(missing)
    breakpoint()
    assert _get_hexdigest('md5', str(missing)) == md5(b'missing').hexdigest()

