
BOT_NAME = 'real_estate'

SPIDER_MODULES = ['real_estate.spiders']
NEWSPIDER_MODULE = 'real_estate.spiders'

USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36 Edge/15.15063'
ROBOTSTXT_OBEY = False
DOWNLOAD_DELAY = 1

RETRY_TIMES = 15
RETRY_HTTP_CODES = [500, 503, 504, 400, 403, 404, 408]
PROXY_MODE = 0

DOWNLOADER_MIDDLEWARES = {

    'scrapy.downloadermiddlewares.retry.RetryMiddleware': 90,
    'scrapy_proxies.RandomProxy': 100,
    'scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware': 110,
    # 'scrapy_splash.SplashCookiesMiddleware': 723,
    # 'scrapy_splash.SplashMiddleware': 725,
    'scrapy.downloadermiddlewares.httpcompression.HttpCompressionMiddleware': 810,
    # Downloader side
}

# SPIDER_MIDDLEWARES = {
#     'scrapy_splash.SplashDeduplicateArgsMiddleware': 100,
# }
PROXY_LIST = 'proxy.txt'

# SPLASH_URL = 'http://127.0.0.1:8050/'
# SPLASH_URL = 'http://192.168.59.103:8050/'
# DUPEFILTER_CLASS = 'scrapy_splash.SplashAwareDupeFilter'
# HTTPCACHE_STORAGE = 'scrapy_splash.SplashAwareFSCacheStorage'

ITEM_PIPELINES = {
   'real_estate.pipelines.BetGatheringPipeline': 300,
}

MONGO_URI = 'mongodb+srv://login:haslo@url_bazy'
MONGO_DB = 'real_estate_wroclaw'
