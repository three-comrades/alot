# Copyright (C) 2011-2012  Patrick Totzke <patricktotzke@gmail.com>
# This file is released under the GNU GPL, version 3 or a later revision.
# For further details see the COPYING file

"""
Widgets specific to Bufferlist mode
"""
from __future__ import absolute_import

import urwid


class QuerylineWidget(urwid.Text):
    """
    selectable text widget that represents a :class:`~alot.buffers.Buffer`
    in the :class:`~alot.buffers.BufferlistBuffer`.
    """

    def __init__(self, query):
        self.query = query
        urwid.Text.__init__(self, query.__str__(), wrap='clip')

    def selectable(self):
        return True

    def keypress(self, size, key):
        return key

    def get_query(self):
        return self.query
