AUTHOR = "LSC"
SITENAME = "LSC Info"
SITESUBTITLE = "Info Page for LSC"
TIMEZONE = "Europe/London"
THEME="basic"
# can be useful in development, but set to False when you're ready to publish
RELATIVE_URLS = False
REVERSE_CATEGORY_ORDER = True
LOCALE = "C"
DEFAULT_PAGINATION = 4
DEFAULT_DATE = (2012, 12, 21, 14, 1, 1)
LINKS = (
    ("LSC", "http://reddit.com/r/LondonSocialClub/"),
    ("Contribute", "https://github.com/londonsocialclub/londonsocialclub.github.io")
    )
SOCIAL =  ()
# global metadata to all the contents
DEFAULT_METADATA = {"yeah": "it is"}

# path-specific metadata
EXTRA_PATH_METADATA = {
    "extra/robots.txt": {"path": "robots.txt"},
    'extra/favicon.ico': {'path': 'favicon.ico'},
}

# static paths will be copied without parsing their contents
STATIC_PATHS = [
    "images",
    "extra",
]

# there is no other HTML content
READERS = {"html": None}

# code blocks with line numbers
PYGMENTS_RST_OPTIONS = {"linenos": "table"}


