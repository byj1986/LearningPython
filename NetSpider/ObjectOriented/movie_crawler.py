from bs4 import BeautifulSoup
from crawler_base import crawler_base
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec


class movie_crawler(crawler_base):
    # until = None
    until = ec.presence_of_element_located((By.CLASS_NAME, "top-list-data"))
    HostUrl = "http://www.zhuixinfan.com/"
    MovieUrl = None

    def __init__(self):
        crawler_base.__init__(self)

    def validateHref(self, href: str) -> bool:
        return href and "main.php?" in href

    def getEpisodesUrl(self, soup: BeautifulSoup) -> []:
        resourcesUrl = []
        tds = soup.find_all('td')
        for td in tds:
            href = td.a and td.a["href"]
            if self.validateHref(href):
                resourcesUrl.append(href)
        return resourcesUrl

    def getDownloadUrls(self) -> []:
        soup = self.getResponse(self.HostUrl+self.MovieUrl, self.until)
        downloadUrls = []
        resourcesUrl = self.getEpisodesUrl(soup)
        for resource in resourcesUrl:
            resourceUrl = self.HostUrl+resource
            resourceSoup = self.getResponse(resourceUrl, self.until)
            downloadUrl = self.getDownloadUrl(resourceSoup)
            if downloadUrl:
                downloadUrls.append(downloadUrl)
        return downloadUrls

    def getDownloadUrl(self, soup: BeautifulSoup) -> str:
        downloadUrl = None
        dds = soup.find_all('dd', attrs={"id": "emule_url"})
        for dd in dds:
            downloadUrl = dd.text
        return downloadUrl


if __name__ == "__main__":
    movie_crawler = movie_crawler()
    movie_crawler.MovieUrl = "viewtvplay-1119.html"
    movieUrls = movie_crawler.getDownloadUrls()
    for movie in movieUrls:
        print(movie)
