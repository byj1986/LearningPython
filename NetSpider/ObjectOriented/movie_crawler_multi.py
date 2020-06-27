from bs4 import BeautifulSoup
from crawler_base import crawler_base
from movie_crawler import movie_crawler
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec


class movie_crawler_multi(movie_crawler):

    def __init__(self):
        movie_crawler.__init__(self)

    def getDownloadUrls(self) -> []:
        soup = self.getResponse(self.HostUrl+self.MovieUrl, self.until)
        downloadUrls = []
        resourcesUrl = self.getEpisodesUrl(soup)
        for resource in resourcesUrl:
            js = 'window.open("%s")' % resource
            self.browser.execute_script(js)
        self.wait.until(ec.number_of_windows_to_be(len(resourcesUrl)+1))
        for handle in self.browser.window_handles:
            self.browser.switch_to.window(handle)
            self.wait.until(self.until)
            resourceSoup = BeautifulSoup(
                self.browser.page_source, features="lxml")
            downloadUrl = self.getDownloadUrl(resourceSoup)
            if downloadUrl:
                downloadUrls.append(downloadUrl)
        return downloadUrls


if __name__ == "__main__":
    movie_crawler_multi = movie_crawler_multi()
    movie_crawler.MovieUrl = "viewtvplay-1119.html"
    movieUrls = movie_crawler_multi.getDownloadUrls()
    for movie in movieUrls:
        print(movie)
