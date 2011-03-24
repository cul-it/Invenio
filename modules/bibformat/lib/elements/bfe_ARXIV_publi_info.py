# -*- coding: utf-8 -*-
##
## This file is part of Invenio.
## Copyright (C) 2006, 2007, 2008, 2010, 2011 CERN.
##
## Invenio is free software; you can redistribute it and/or
## modify it under the terms of the GNU General Public License as
## published by the Free Software Foundation; either version 2 of the
## License, or (at your option) any later version.
##
## Invenio is distributed in the hope that it will be useful, but
## WITHOUT ANY WARRANTY; without even the implied warranty of
## MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
## General Public License for more details.
##
## You should have received a copy of the GNU General Public License
## along with Invenio; if not, write to the Free Software Foundation, Inc.,
## 59 Temple Place, Suite 330, Boston, MA 02111-1307, USA.
"""BibFormat element - Prints publcation information and link to ejournal
"""
__revision__ = "$Id$"

from urllib import quote
import cgi

def format_element(bfo):
    """
    Displays inline publication information with html link to ejournal
    (when available).
    """

    out = ''

    publication_info = bfo.field('773__')
    if publication_info == "":
        return ""

    journal_ref = publication_info.get('o')

    if journal_ref != '':
        out = '%(journal_ref)s' % {'journal_ref': journal_ref}

    return out

def escape_values(bfo):
    """
    Called by BibFormat in order to check if output of this element
    should be escaped.
    """
    return 0





