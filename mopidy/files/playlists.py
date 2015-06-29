from __future__ import unicode_literals

import logging

from mopidy import backend

logger = logging.getLogger(__name__)


class PlaylistsProvider(backend.PlaylistsProvider):

    def __init__(self, backend):
        self._backend = backend

    def get_items(self, uri):
        logger.debug(u'get_items called for uri %s' % uri)

    def lookup(self, uri):
        logger.debug(u'lookup called for uri %s' % uri)

    def as_list(self):
        logger.debug(u'as_list called')
        return []
        
