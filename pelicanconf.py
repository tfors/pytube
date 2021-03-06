#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import os

AUTHOR = 'Paul Logston'
SITENAME = 'PyTube.org'

PATH = 'content'

TIMEZONE = 'UTC'

DEFAULT_LANG = 'en'

DEFAULT_PAGINATION = 10

ARTICLE_URL = ARTICLE_SAVE_AS = '{category}/{slug}.html'
ARTICLE_LANG_URL = ARTICLE_LANG_SAVE_AS = '{category}/{slug}-{lang}.html'
DRAFT_URL = DRAFT_SAVE_AS = 'drafts/{category}/{slug}.html'
DRAFT_LANG_URL = DRAFT_LANG_SAVE_AS = 'drafts/{category}/{slug}-{lang}.html'
PAGE_URL = PAGE_SAVE_AS = 'pages/{slug}.html'
PAGE_LANG_URL = PAGE_LANG_SAVE_AS = 'pages/{slug}-{lang}.html'
CATEGORY_URL = CATEGORY_SAVE_AS = 'events/{slug}.html'
TAGS_URL = TAGS_SAVE_AS = 'tags.html'
# Hack to avoid this issue: https://github.com/getpelican/pelican/issues/1137
TAG_URL = 'tag/{slug}/'
TAG_SAVE_AS = 'tag/{slug}/index.html'
# End hack to avoid issue #1137
YEAR_ARCHIVE_SAVE_AS = 'archives/{date:%Y}/index.html'
MONTH_ARCHIVE_SAVE_AS = 'archives/{date:%Y}/{date:%b}/index.html'
CATEGORIES_SAVE_AS = 'events.html'

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

DELETE_OUTPUT_DIRECTORY = True

THEME = 'themes/pytube-201601/'

GITHUB_URL = 'https://github.com/pytube/pytube'
CONTRIBUTE_URL = 'https://github.com/pytube/pytube/wiki/How-to-Contribute-Media'

PUBLISHER_URL = (os.environ.get('PUBLISHER_URL') or '').strip()
PUBLISHER_URL = PUBLISHER_URL or 'https://publisher.pytube.org/publish'

STATIC_PATHS = [
    'images',
    'extra/robots.txt',
    'extra/favicon.ico',
    'extra/CNAME',
]

EXTRA_PATH_METADATA = {
    'extra/CNAME': {'path': 'CNAME'},
    'extra/robots.txt': {'path': 'robots.txt'},
    'extra/favicon.ico': {'path': 'favicon.ico'}
}


PLUGINS = ['bin.plugins', 'extended_sitemap']
