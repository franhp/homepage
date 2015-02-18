from ajax_select import LookupChannel
from tvdb_api import Tvdb

from tvseries.models import TVSeries


class TVSeriesLookup(LookupChannel):
    tv = Tvdb()
    min_length = 3

    def get_query(self, q, request):
        results = []
        search = self.tv.search(q)
        for res in search:
            results.append(TVSeries(name=res['seriesname'],
                                    year=res['firstaired'] if 'firstaired' in res else 'empty'))
        return results

    def get_result(self, obj):
        res = self.tv[obj.name]
        return '|'.join([res.data['seriesname'],
                         res.data['imdb_id'] or 'empty',
                         res.data['firstaired'] or 'empty',
                         res.data['poster'] or 'empty'])

    def format_match(self, obj):
        return '%s (%s)' % (obj.name, obj.year[0:3])