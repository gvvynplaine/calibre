#!/usr/bin/env  python

##    Copyright (C) 2008 Kovid Goyal kovid@kovidgoyal.net
##    This program is free software; you can redistribute it and/or modify
##    it under the terms of the GNU General Public License as published by
##    the Free Software Foundation; either version 2 of the License, or
##    (at your option) any later version.
##
##    This program is distributed in the hope that it will be useful,
##    but WITHOUT ANY WARRANTY; without even the implied warranty of
##    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
##    GNU General Public License for more details.
##
##    You should have received a copy of the GNU General Public License along
##    with this program; if not, write to the Free Software Foundation, Inc.,
##    51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
'''
bbc.co.uk
'''

from libprs500.web.feeds.news import BasicNewsRecipe

class BBC(BasicNewsRecipe):
    title          = u'The BBC'
    no_stylesheets = True

    remove_tags    = [dict(name='div', attrs={'class':'footer'})]
    extra_css      = '.headline {font-size: x-large;} \n .fact { padding-top: 10pt  }' 

    feeds          = [
                      ('News Front Page', 'http://newsrss.bbc.co.uk/rss/newsonline_world_edition/front_page/rss.xml'), 
                      ('Science/Nature', 'http://newsrss.bbc.co.uk/rss/newsonline_world_edition/science/nature/rss.xml'),
                      ('Technology', 'http://newsrss.bbc.co.uk/rss/newsonline_world_edition/technology/rss.xml'),
                      ('Enterntainment', 'http://newsrss.bbc.co.uk/rss/newsonline_world_edition/entertainment/rss.xml'),
                      ('Magazine', 'http://newsrss.bbc.co.uk/rss/newsonline_world_edition/uk_news/magazine/rss.xml'),
                      ('Business', 'http://newsrss.bbc.co.uk/rss/newsonline_world_edition/business/rss.xml'),
                      ('Health', 'http://newsrss.bbc.co.uk/rss/newsonline_world_edition/health/rss.xml'),
                      ('Americas', 'http://newsrss.bbc.co.uk/rss/newsonline_world_edition/americas/rss.xml'),
                      ('Europe', 'http://newsrss.bbc.co.uk/rss/newsonline_world_edition/europe/rss.xml'),
                      ('South Asia', 'http://newsrss.bbc.co.uk/rss/newsonline_world_edition/south_asia/rss.xml'),
                      ('UK', 'http://newsrss.bbc.co.uk/rss/newsonline_world_edition/uk_news/rss.xml'),
                      ('Asia-Pacific', 'http://newsrss.bbc.co.uk/rss/newsonline_world_edition/asia-pacific/rss.xml'),
                      ('Africa', 'http://newsrss.bbc.co.uk/rss/newsonline_world_edition/africa/rss.xml'),
                    ]

    def print_version(self, url):
        return url.replace('http://', 'http://newsvote.bbc.co.uk/mpapps/pagetools/print/')