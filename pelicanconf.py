#!/usr/bin/env python
# -*- coding: utf-8 -*- #

###################################################################################################



from __future__ import unicode_literals
from collections import OrderedDict
import datetime
import hashlib
import os


###################################################################################################
# 系统的全局设置

# 名称以及站点相关
AUTHOR = u'FinalTheory'
SITENAME = u'黄闻天的技术笔记'
HOMENAME = '首页'
# HOMEURL = ''
SITEURL = ''

# 时间与区域
DEFAULT_LANG = 'zh'
TIMEZONE = 'Asia/Shanghai'
DEFAULT_DATE = 'fs'
UPDATEDATE_MODE = 'metadata'

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

###################################################################################################
# 与路径相关的设置，以及插件等

PATH = 'content'
STATIC_PATHS = ['images', 'files', 'extra']
THEME = "MyTheme/pelican-theme"
PLUGIN_PATHS = ['pelican-plugins', 'MyTheme']
FILENAME_METADATA = '(?P<slug>.*)'
PLUGINS = [
    'assets',
    'gravatar',
    'extract_headings',
    'niux2_hermit_player',
    'pelican-update-date',
    'sitemap',
    'summary',
    'render_math',
    'i18n_subsites'
]

NIUX2_HEADER_DROPDOWN_SECTIONS_EN = OrderedDict()
NIUX2_HEADER_DROPDOWN_SECTIONS_EN[('Archives', 'fa-archive')] = [
    ('By Publish', 'archives order by publish time', '/en/archives.html', 'fa-calendar'),
    ('By Update', 'archives order by modify time', '/en/archives_updatedate.html', 'fa-pencil'),
]

I18N_SUBSITES = {
    "en": {
        "SITENAME": "Tech Notes of Yan Huang",
        "HOMENAME": "Home",
        "NIUX2_CATEGORY_MAP": {
            'algorithm': ('Algorithm', 'fa-cogs'),
            'research': ('Research', 'fa-flask'),
            'note': ('Notes', 'fa-book'),
            'life': ('Life', 'fa-coffee'),
            'thinking': ('Thinking', 'fa-leaf'),
            'collection': ('Collection', 'fa-briefcase'),
        },
        "NIUX2_HEADER_SECTIONS": [
            ('Tags', 'Tags', '/en/tag/', 'fa-tags'),
            ('About Me', 'About Me', '/en/AboutMe_en.html', 'fa-anchor'),
            ('Site Home', 'Site HomePage', 'http://finaltheory.me/', 'fa-sitemap'),
        ],
        "NIUX2_HEADER_DROPDOWN_SECTIONS": NIUX2_HEADER_DROPDOWN_SECTIONS_EN,
        "NIUX2_CATEGORY_TRANSL": 'Category'
    }
}

I18N_UNTRANSLATED_ARTICLES = "hide"
I18N_UNTRANSLATED_PAGES = "hide"


# 下面这个dict定义了一组编译后不变的静态地址链接
# 注意这里路径的写法，如果是在Linux下，要换成对应的风格！
EXTRA_PATH_METADATA = {
    'extra/favicon.ico': {'path': 'favicon.ico'},
    'extra/LICENSE.txt': {'path': 'LICENSE.txt'},
    'extra/robots.txt': {'path': 'robots.txt'},
}

TEMPLATE_PAGES = {
		"abstracts.html": "abstracts.html",
    "404.html": "404.html",
    "archives_updatedate.html": "archives_updatedate.html",
}

# 下面这组设置重新安排了article输出、page输出以及目录、标签的布局方式
ARTICLE_URL = '{category}/{slug}.html'
ARTICLE_SAVE_AS = ARTICLE_URL
PAGE_URL = '{slug}.html'
PAGE_SAVE_AS = PAGE_URL
CATEGORY_URL = '{slug}/index.html'
CATEGORY_SAVE_AS = CATEGORY_URL
TAG_URL = 'tag/{slug}.html'
TAG_SAVE_AS = TAG_URL
TAGS_SAVE_AS = 'tag/index.html'

# disable author pages
AUTHOR_SAVE_AS = ''
AUTHORS_SAVE_AS = ''

###################################################################################################
# RSS以及文章输出相关的设置

# 缓存策略与页面输出
SUMMARY_MAX_LENGTH = 10
MAX_ABSTRACT_NUM = 3
LOAD_CONTENT_CACHE = False
CACHE_CONTENT = False
# 加入这个傻逼插件后，会在包含大写的header中自动加入<span>，因此一定要关掉！！！
TYPOGRIFY = False

# Feed generation is usually not desired when developing
FEED_DOMAIN = SITEURL
FEED_ALL_RSS = None
FEED_MAX_ITEMS = 20
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# 文章分类的设置
USE_FOLDER_AS_CATEGORY = True
DELETE_OUTPUT_DIRECTORY = True
DEFAULT_CATEGORY = 'uncategorized'
DEFAULT_PAGINATION = 8


# 其他高级设置
READERS = {
    'html': None,
}

###################################################################################################
# 插件高级设置

JINJA_ENVIRONMENT = {
    "extensions": [
        "jinja2.ext.i18n",
        "jinja2.ext.do",
        "jinja2.ext.ExprStmtExtension"
    ],
}

# sitemap plugin config
SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.5,
        'indexes': 0.5,
        'pages': 0.5
    },
    'changefreqs': {
        'articles': 'weekly',
        'indexes': 'daily',
        'pages': 'monthly'
    }
}

def my_slugify(value, sep='-'):
    if isinstance(value, str):
        # Match old Windows vs Unix behavior
        if os.name.lower().startswith('nt'):
            value = value.encode('gb18030', errors='ignore')
        else:
            value = value.encode('utf-8', errors='ignore')
    elif not isinstance(value, (bytes, bytearray)):
        value = str(value).encode('utf-8', errors='ignore')

    h = hashlib.md5()
    h.update(value)
    return h.hexdigest()[:8]

MY_SLUGIFY_FUNC = my_slugify
MY_HEADING_LIST_STYLE = 'ol'

MARKDOWN = {
    "extensions": [
        "markdown.extensions.meta",
        "markdown.extensions.nl2br",
        "markdown.extensions.extra",
        "markdown.extensions.footnotes",
        "markdown.extensions.tables",
        "markdown.extensions.codehilite",
    ],
    "extension_configs": {
        "markdown.extensions.codehilite": {
            "linenums": False,
            "guess_lang": False,
        },
    },
    "output_format": "html5",
}


###################################################################################################
NIUX2_CATEGORY_TRANSL = '分类'
NIUX2_404_TITLE_TRANSL = '404 ERROR'
NIUX2_404_INFO_TRANSL = 'Requested Page Not Found!'
NIUX2_ARCHIVE_TRANSL = 'Archives'
NIUX2_ARCHIVE_UPDATEDATE_TRANSL = 'Archives (By Update Time)'
NIUX2_SEARCH_PLACEHOLDER_TRANSL = 'You probably need VPN to use Google!'
NIUX2_LAZY_LOAD_TEXT = '囧rz~Loading!'

# 其他与主题相关的设置

NIUX2_AUTHOR_LINK = SITEURL
NIUX2_PYGMENTS_THEME = 'github'
NIUX2_PAGINATOR_LENGTH = 11
NIUX2_RECENT_UPDATE_NUM = 10
NIUX2_FAVICON_URL = '/favicon.ico'
NIUX2_GOOGLE_CSE_ID = '8094c665b86c645ea'
NIUX2_DISPLAY_TITLE = True
NIUX2_LAZY_LOAD = True
NIUX2_TOOLBAR = True
# 这个选项是用来显示博客的提交历史的，如果是托管在github上面的话
# NIUX2_GITHUB_REPO = ''

NIUX2_CATEGORY_MAP = {
    'algorithm': ('算法', 'fa-cogs'),
    'research': ('研究', 'fa-flask'),
    'note': ('笔记', 'fa-book'),
    'life': ('日常', 'fa-coffee'),
    'thinking': ('随笔', 'fa-leaf'),
    'collection': ('收藏', 'fa-briefcase'),
}

NIUX2_HEADER_SECTIONS = [
    ('标签', 'Tags', '/tag/', 'fa-tags'),
#    ('项目', 'My Projects', '/MyProjects.html', 'fa-rocket'),
    ('关于我', 'About Me', '/AboutMe.html', 'fa-anchor'),
    ('网站首页', 'Site HomePage', 'http://finaltheory.me/', 'fa-sitemap'),
]

NIUX2_HEADER_DROPDOWN_SECTIONS = OrderedDict()
NIUX2_HEADER_DROPDOWN_SECTIONS[('归档', 'fa-archive')] = [
    ('按发布时间', 'archives order by publish time', '/archives.html', 'fa-calendar'),
    ('按更新时间', 'archives order by modify time', '/archives_updatedate.html', 'fa-pencil'),
]

NIUX2_FOOTER_LINKS = [
    ('LICENSE', 'Terms, license and privacy etc', '/LICENSE.txt', ''),
]

NIUX2_FOOTER_ICONS = [
    ('fa-linkedin', 'My Linkedin', 'https://www.linkedin.com/in/yan-huang-4061769b/'),
    ('fa-github', 'My Github Page', 'https://github.com/FinalTheory'),
    ('fa-instagram', 'My Instagram', 'https://www.instagram.com/yanhuang9421/'),
    ('fa-facebook-square', 'My Facebook Page', 'https://www.facebook.com/ForFinalTheory'),
    ('fa-book', 'My RED Page', 'https://www.xiaohongshu.com/user/profile/5839b2e3a9b2ed428801e6c6'),
    ('fa-envelope-o', 'Send E-mail to Me', 'mailto: FinalTheory@hotmail.com'),
    ('fa-rss', 'Subscribe My Blog', '/feed.xml'),
]
