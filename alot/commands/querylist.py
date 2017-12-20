# Copyright (C) 2011-2012  Patrick Totzke <patricktotzke@gmail.com>
# This file is released under the GNU GPL, version 3 or a later revision.
# For further details see the COPYING file
from __future__ import absolute_import

from . import Command, registerCommand
from .globals import SearchCommand

MODE = 'querylist'

@registerCommand(MODE, 'select')
class QuerylistSelectCommand(Command):

    """search for messages with selected query"""
    def apply(self, ui):
        query_name = ui.current_buffer.get_selected_query()
        cmd = SearchCommand(query=['query:"%s"' % query_name])
        ui.apply_command(cmd)
