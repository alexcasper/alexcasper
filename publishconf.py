# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys

sys.path.append(os.curdir)
from pelicanconf import *
IGNORE_FILES = ['readme.md','README.md']
# If your site is available via HTTPS, make sure SITEURL begins with https://
RELATIVE_URLS = False
FEED_ALL_ATOM = "feeds/all.atom.xml"
CATEGORY_FEED_ATOM = "feeds/{slug}.atom.xml"
THEME="sidecar"
DELETE_OUTPUT_DIRECTORY = True
# Following items are often useful when publishing

# DISQUS_SITENAME = ""
# GOOGLE_ANALYTICS = ""
