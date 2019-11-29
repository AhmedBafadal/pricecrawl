# Web crawler Price

## Description
Web crawler to extract URLs from websites to later be scraped for product data.

The logic within this repository utilises Scrapy to extract the relevant URLs without using a sitemap, while also respecting the directives specified in the robots.txt file. 


Further, performance was considered during development, with calibrations applied within the settings.py file to enforce a maximum of 2 requests made per second to target sites. This includes prioritising Breadth First Search over the default Depth First Search algorithm to capture performance gains.

For convienience, changes to settings.py to reflect performance are listed below:

```
SCHEDULER_PRIORITY_QUEUE = 'scrapy.pqueues.DownloaderAwarePriorityQueue'
DEPTH_PRIORITY = 1
SCHEDULER_DISK_QUEUE = 'scrapy.squeues.PickleFifoDiskQueue'
SCHEDULER_MEMORY_QUEUE = 'scrapy.squeues.FifoMemoryQueue'
REACTOR_THREADPOOL_MAXSIZE = 20
RETRY_ENABLED = False
DOWNLOAD_TIMEOUT = 15
REDIRECT_ENABLED = False
DOWNLOAD_DELAY = 1
HTTPCACHE_ENABLED = True
COOKIES_ENABLED = False
```

## Installation
```
pip install -r requirements.txt

scrapy crawl pricecrawler
```

## Implementation
To begin the scraper, one can add a url in text form to a "urls.txt" file located at the root of the directory. If this is not available, please create one.

Once the scraper has been completed and all unique & relevant links are extracted, a text file is generated at the root of the directory, which is named using the domain of the website crawled (e.g. crawling quotes.toscrape.com generates "toscrape-output.txt").

To run scraper:
```
scrapy crawl pricecrawler
```

