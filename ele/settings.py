# -*- coding: utf-8 -*-

# Scrapy settings for ele project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'ele'

SPIDER_MODULES = ['ele.spiders']
NEWSPIDER_MODULE = 'ele.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'ele (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = True

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
  'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
  'accept-encoding': 'gzip, deflate, br',
  'accept-language': 'zh-CN,zh;q=0.9',
  'cache-control': 'no-cache',
  'pragma': 'no-cache',
  'referer': 'https://www.baidu.com/link?url=rNU4URR9gI3FjT_wcZ6bIAeLOgOHscr2WwFhkBWoApa&wd=&eqid=af04f22300022151000000065b9a2ba8',
  # 'referer': 'https://h5.ele.me/login/',
  'upgrade-insecure-requests': '1',
}

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'ele.middlewares.EleSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
    # 'ele.middlewares.EleDownloaderMiddleware': 543,
    # 'dianping.middlewares.ProxyMiddleware': 101,
    # 'ele.middlewares.RandomUserAgentMiddleware': 443,
    'ele.middlewares.RandomCookiesMiddleware': 545,
    # 'scrapy.downloadermiddlewares.retry.RetryMiddleware': None,
    # 'ele.middlewares.TooManyRequestsRetryMiddleware': 540,
}

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    # 'ele.pipelines.ElePipeline': 300,
    'ele.pipelines.MongoPipeline': 300,
    'ele.pipelines.MysqlPipeline': 301,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'


# REDIRECT_ENABLED = False
# HTTPERROR_ALLOWED_CODES = [403, 302]
HTTPERROR_ALLOWED_CODES = list(range(300, 600))
# RETRY_HTTP_CODES = [500, 502, 503, 504, 400, 403, 404, 408, 429]
RETRY_HTTP_CODES = list(range(400, 600))
RETRY_TIMES = 6


MONGO_URI = 'localhost'
MONGO_DB = 'Eleme_MongoDB'

MYSQL_HOST = 'localhost'
MYSQL_DATABASE = 'eleme'
MYSQL_USER = 'root'
MYSQL_PASSWORD = '123456'
MYSQL_PORT = 3306

LOG_LEVEL = 'DEBUG'
LOG_FILE = 'log.txt'
# COMMANDS_MODULE = 'dianping.commands'