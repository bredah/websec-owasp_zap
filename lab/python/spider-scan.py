#!/usr/bin/env python
# A basic ZAP Python API example which spiders and scans a target URL

import time
from pprint import pprint
from zapv2 import ZAPv2
from enum import Enum


class Report(Enum):
    JSON = 1
    XML = 2


class Script():

    def set_target(self, url):
        """ Set the target for testing:
        url - Target to attack
        """
        self.target = url

    def setup_zap(self, url, apikey=None):
        """ Set the OWASP ZAP Server:
        url - Server address
        apikey - Security key to connect to the server
        """
        if apikey is None:
            self.zap = ZAPv2(proxies={'http': url, 'https': url})
        else:
            self.zap = ZAPv2(apikey=apikey, proxies={
                             'http': url, 'https': url})

    def spider(self):
        import sys
        dot = '.'
        """ Start spider scanner
        """
        # Proxy a request to the target so that ZAP has something to deal with
        print('Accessing target:\n\t{}'.format(self.target))
        self.zap.urlopen(self.target)
        # Give the sites tree a chance to get updated
        time.sleep(1)
        scanid = self.zap.spider.scan(self.target)
        # Give the Spider a chance to start
        time.sleep(1)
        sys.stdout.write('Spider: Start passive scan now, waiting')
        while (int(self.zap.spider.status(scanid)) < 100):
            # # Loop until the spider has finished
            # print('Spider progress %: {}'.format(
            #     self.zap.spider.status(scanid)))
            sys.stdout.write(dot)
            sys.stdout.flush()
            time.sleep(2)
        # print('Spider progress %: 100')
        sys.stdout.write('\nSpider: Scan all pages now, waiting')
        url_found = 0
        while (int(self.zap.pscan.records_to_scan) > 0):
            url_found = int(self.zap.pscan.records_to_scan)
            sys.stdout.write(dot)
            sys.stdout.flush()
            time.sleep(0.5)
        print('\nSpider: found {} urls to scan'.format(url_found))
        print('Spider: completed')

    def active_scan(self):
        """ Start active scanner
        """
        print('Active Scanning target {}'.format(self.target))
        scanid = zap.ascan.scan(self.target)
        while (int(zap.ascan.status(scanid)) < 100):
            # Loop until the scanner has finished
            print('Scan progress %: {}'.format(self.zap.ascan.status(scanid)))
            time.sleep(5)
        print('Active Scan completed')

    def report(self, format=None):
        """ Generate output report
        format - See Report to define a specific report format 
        """
        print('Hosts: ' + ', '.join(self.zap.core.hosts))
        print('Sites: ' + ', '.join(self.zap.core.sites))
        # print('Urls: ' + ', '.join(self.zap.core.urls))
        print('Hosts: {}'.format(', '.join(self.zap.core.hosts)))
        #print('Alerts: ')
        # print(self.zap.core.alerts())
        if format == Report.JSON:
            print(self.zap.core.jsonreport())
        if format == Report.XML:
            print(self.zap.core.xmlreport())

    def show_urls(self):
        spider_urls = []
        for item in  self.zap.core.urls():
            if item not in spider_urls:
                spider_urls.append(item)
        print("URL's found ({}):".format(len(spider_urls)))
        for item in  spider_urls:
            print ("\t" + item)

    def run(self):
        # Set the OWASP ZAP server
        self.setup_zap('http://127.0.0.1:9999')
        # Set the target
        self.set_target('http://testphp.vulnweb.com/')
        # Start passive scan (spider)
        self.spider()

        self.show_urls()
        # Show report
        self.report()


if __name__ == "__main__":
    Script().run()
