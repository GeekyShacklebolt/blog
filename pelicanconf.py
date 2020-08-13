#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Shiva Saxena'
SITENAME = 'Shiva Saxena'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Asia/Kolkata'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
# SOCIAL = (('You can add links in your config file', '#'),
#           ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

#############################
#    My Custom Additions    #
#############################
THEME = '/home/shiva/.virtualenvs/pelicanblog/lib/python3.8/site-packages/pelican/themes/pelican-clean-blog'
RELATIVE_URLS = True

# Social icons
SOCIAL = (
    ('github', 'https://github.com/geekyshacklebolt'),
    ('linkedin', 'https://linkedin.com/in/shiva-saxena'),
    ('instagram', 'https://instagram.com/geekyshacklebolt'),
    ('twitter', 'https://twitter.com/ershivasaxena'),
    ('wordpress', 'https://geekyshacklebolt.wordpress.com'),
    ('pencil', 'http://www.thegeekyway.com/author/geekyshacklebolt'),
    ('envelope', 'mailto:shivasaxena911@gmail.com'),
)

SITESUBTITLE = 'Blog'
SHOW_SITESUBTITLE_IN_HTML = 'True'
HEADER_PAGE_TITLE = 'A Personal Blog'
SHOW_CREDIT_BY_AUTHOR = 'True'
NAVBAR_BRAND = 'GeekyShacklebolt'
HEADER_COVER = 'images/my-blog-header-bg.jpg'
AUTHOR_NICK = 'GeekyShacklebolt'

