#!/usr/bin/env python
# A basic ZAP Python API example which spiders and scans a target URL

import time
from pprint import pprint
from zapv2 import ZAPv2

target = 'http://testphp.vulnweb.com/'
apikey = 'abc123' # Change to match the API key set in ZAP, or use None if the API key is disabled
#
# By default ZAP API client will connect to port 8080
#zap = ZAPv2(apikey=apikey)
# Use the line below if ZAP is not listening on port 8080, for example, if listening on port 8090
zap = ZAPv2(apikey=apikey, proxies={'http': 'http://127.0.0.1:9999', 'https': 'http://127.0.0.1:9999'})

# Proxy a request to the target so that ZAP has something to deal with
print('Accessing target {}'.format(target))
zap.urlopen(target)
# Give the sites tree a chance to get updated
time.sleep(2)

print('Spidering target {}'.format(target))
scanid = zap.spider.scan(target)
# Give the Spider a chance to start
time.sleep(2)
while (int(zap.spider.status(scanid)) < 100):
    print('Spider progress %: ' + zap.spider.status(scanid))
    time.sleep(2)

print('Spider completed')
# # Give the passive scanner a chance to finish
# time.sleep(5)

# print('Scanning target %s' % target)
# scanid = zap.ascan.scan(target)
# while (int(zap.ascan.status(scanid)) < 100):
#     print('Scan progress %: ' + zap.ascan.status(scanid))
#     time.sleep(5)

# print('Scan completed')

# Report the results

print ('Hosts: ' + ', '.join(zap.core.hosts))
print ('Sites: ' + ', '.join(zap.core.sites))
print ('Urls: ')
spider_urls = []
for item in  zap.core.urls():
   if item not in spider_urls:
      spider_urls.append(item)

print("URL's found ({}):".format(len(spider_urls)))
for item in  spider_urls:
   print (item)
# print ('   ')
# print ('Hosts: {}'.format(', '.join(zap.core.hosts)))
# print ('Alerts: ')
# print (zap.core.alerts())