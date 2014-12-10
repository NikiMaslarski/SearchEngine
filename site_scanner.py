import requests
import json
from bs4 import BeautifulSoup
from sqlalchemy import create_engine
from urllib.parse import urlparse, urljoin

from manage_database import Website, Page, Base


class CrawlSite:

    def __init__(self, domain, engine):
        self.engine = engine
        self.domain = domain
        self.scaned_urls = []
        self.paths_for_crowl = set()
        self.paths_for_crowl.add('/')

    def __save_website(self, soup, url):
        pass
        # site = Website(url=self.domain, relece_date=, ssl=, html_version=)

    def __crawl_page(self, url):
        if url in self.scaned_urls:
            return
        self.scaned_urls.append(url)
        a = self.__get_subdomain(url)

        print(a)

    def __get_subpages(self, soup):
        pass


    def __crawl_website(self):
        r = requests.get(self.domain)
        html = r.text
        soup = BeautifulSoup(html)
        hrefs = soup.find_all("a", href=True)
        for link in hrefs:
            temp = urlparse(link["href"])
            if temp.netloc == self.domain or temp.netloc == '':
                self.paths_for_crowl.add(temp.path)
        # print(self.paths_for_crowl)

        while len(self.paths_for_crowl):
            self.__crawl_page(self.paths_for_crowl.pop())
            print()

    def __get_subdomain(self, url):
        return urljoin(self.domain, url)

    def start_crawling(self):
        self.__crawl_website()


def main():
    db_engine = create_engine("sqlite:///site_stats.db")
    Base.metadata.create_all(db_engine)
    sites_for_crawl = json.load(open("sites_for_crawl.json"))

    for site in sites_for_crawl:
        crawl_sites = CrawlSite(site, db_engine)
        crawl_sites.start_crawling()


if __name__ == "__main__":
    main()
