
from scrapy.spiders import Request, CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy import Request
from tldextract import extract
from urllib.robotparser import RobotFileParser

class PriceCrawlerSpider(CrawlSpider):
    name = "pricecrawler"
    # Read from urls.txt file
    with open("urls.txt", "rt") as f:
        start_urls = [url.strip() for url in f.readlines()]

    def __init__(self, *args, **kwargs):
        self.unique_urls = set()


    def parse(self, response):
        le = LinkExtractor(unique=True)
        # Use robot file parser to check if links extracted are allowed
        rp = RobotFileParser()
        BASE_URL = response.request.url
        DOMAIN = extract(BASE_URL).domain
        rp.set_url(BASE_URL+'/robots.txt')
        rp.read()

        # Extract all the links
        all_links = le.extract_links(response)
        for link in all_links:
            # Ensure same domain
            if extract(link.url).domain == DOMAIN:
                if rp.can_fetch("*", link.url):
                    # Enforcing unique urls 
                    if link.url not in self.unique_urls:
                        self.write_to_file(link.url, DOMAIN)
                        self.unique_urls.add(link.url)
                    yield Request(link.url, callback=self.parse)
    
    def write_to_file(self, url, domain):
        
        with open(f"{domain}-output.txt", "a") as f:
            f.write(f"{url}\n")



                


