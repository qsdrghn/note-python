# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals

# useful for handling different item types with a single interface
from itemadapter import is_item, ItemAdapter

from logging import getLogger, Logger
from typing import Optional, Union

from twisted.internet import defer
from twisted.internet.error import (
    ConnectError,
    ConnectionDone,
    ConnectionLost,
    ConnectionRefusedError,
    DNSLookupError,
    TCPTimedOutError,
    TimeoutError,
)
from twisted.web.client import ResponseFailed

from scrapy.core.downloader.handlers.http11 import TunnelError
from scrapy.exceptions import NotConfigured
from scrapy.http.request import Request
from scrapy.spiders import Spider
from scrapy.utils.python import global_object_name
from scrapy.utils.response import response_status_message
import time
#use time.sleep() to emulate delay
import csv

class MyretryMiddleware:
#初始化参数届时在settings.py中进行赋值
    def __init__(self, settings):
        if not settings.getbool('RETRY_ENABLED'):
            raise NotConfigured
        self.max_retry_times = settings.getint('RETRY_TIMES')
        self.retry_http_codes = set(int(x) for x in settings.getlist('RETRY_HTTP_CODES'))
        self.priority_adjust = settings.getint('RETRY_PRIORITY_ADJUST')


    @classmethod
    def from_crawler(cls, crawler):
        return cls(crawler.settings)

    def process_response(self, request, response, spider):
        time.sleep(3)
        print('开始处理',response.url)
        if request.meta.get('dont_retry', False):
            return response
        if response.status in self.retry_http_codes:
            reason = response_status_message(response.status)
            time.sleep(10)
            print('response出现错误，开始进行重试',response.status)
            return self._retry(request, reason, spider) or response
        return response

    def process_exception(self, request, exception, spider):
        exception = str(exception)
        print('This Exception is: %s'%exception)
        time.sleep(10)
        print('请求出现错误，开始进行重试')
        return self._retry(request, exception, spider)

    def _retry(self, request, reason, spider):
        max_retry_times = request.meta.get('max_retry_times', self.max_retry_times)
        priority_adjust = request.meta.get('priority_adjust', self.priority_adjust)
        url = request.url
        stats = spider.crawler.stats
        retry_times = request.meta.get('retry_times',0) + 1
        if retry_times <= max_retry_times:
            print('请求（%s）正在进行第%d次重试'%(url,retry_times))
            time.sleep(5)
            new_request = request.copy()
            new_request.meta['retry_times'] = retry_times
            new_request.dont_filter = True
            new_request.priority = request.priority + priority_adjust
            return new_request
        else:
            with open('./retry_url.csv','a+',newline='') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow([url, reason])
            return None




