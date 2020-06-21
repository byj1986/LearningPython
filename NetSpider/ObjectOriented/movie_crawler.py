from bs4 import BeautifulSoup
from crawler_base import crawler_base
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec


class movie_crawler(crawler_base):
    # until = None
    WebLoadedParam = None
    MovieUrl = None
    HostUrl = None

    def __init__(self):
        crawler_base.__init__(self)
        # super(crawler_base, self).__init__()
        # self.WebLoadedParam =
        # self.HostUrl = "http://www.zhuixinfan.com/"
        # self.until = wait.until(ec.presence_of_element_located((By.ID, param)))

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
        soup = self.getResponse(self.HostUrl+self.MovieUrl)
        downloadUrls = []
        resourcesUrl = self.getEpisodesUrl(soup)
        for resource in resourcesUrl:
            resourceUrl = self.HostUrl+resource
            resourceSoup = self.getResponse(resourceUrl, self.WebLoadedParam)
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
    movie_crawler.HostUrl = "http://www.zhuixinfan.com/"
    movie_crawler.until = ec.presence_of_element_located((By.ID, "nv_main"))
    movieUrls = movie_crawler.getDownloadUrls()
    for movie in movieUrls:
        print(movie)
