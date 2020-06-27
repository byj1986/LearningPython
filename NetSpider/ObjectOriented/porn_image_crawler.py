# coding=utf-8
import os
import re
import requests

from bs4 import BeautifulSoup
from crawler_base import crawler_base
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec


class porn_image_crawler(crawler_base):

    until = ec.presence_of_element_located((By.ID, "ajaxtable"))
    episodeUntil = ec.presence_of_element_located((By.ID, 'main'))

    sampleEpisode = 'https://cc.lvrts.com/htm_data/2006/15/3986474.html'
    HostUrl = None
    CategoryUrl = None
    PagingPostfix = None

    PornEpisodePattern = re.compile(r'\w{2,6}-?\d{3,5}')
    ImagePostfixPattern = re.compile(r'(jpg|jpeg|JPG|JPEG)$')
    # PornExcludePattern = re.compile(r'【亚洲有码精品】')

    def __init__(self):
        crawler_base.__init__(self)

    # def get_image_url() -> str:

    def getEpisodesUrls(self, page: int) -> {}:
        episodeUrls = {}
        url = self.HostUrl+self.CategoryUrl+self.PagingPostfix+str(page)
        print(url)
        pageSoup = self.getResponse(url, self.until)
        tds = pageSoup.find_all('h3')
        # for td in tds:
        for i in range(10):
            td = tds[i]
            validEpisodeRaw = re.findall(self.PornEpisodePattern, td.text)
            if validEpisodeRaw:
                episodeName = validEpisodeRaw[0]
                episodeUrl = self.HostUrl + '/' + td.a["href"]
                episodeUrls.get
                if episodeUrls.get(episodeName):
                    episodeUrls[episodeName].append(episodeUrl)
                else:
                    episodeUrls[episodeName] = [episodeUrl]
                # episodeUrls.append()
                # print('Url for %s is %s' % (td.text, self.HostUrl+'/' + href))
                # print(tds.a["href"])
                # print(tds[i])
        return episodeUrls

    def getImageUrl(self, episodeUrl: str) -> []:
        imageUrls = []
        episodeSoup = self.getResponse(episodeUrl, self.episodeUntil)
        images = episodeSoup.find_all('img')
        for image in images:
            # re.findall(self.ImagePostfixPattern, image[src])
            # TODO filter out advertisement
            imageUrls.append(image['src'])
        return imageUrls

    def getImagePostfix(self, imageUrl: str) -> str:
        return re.findall(self.ImagePostfixPattern, imageUrl)[0]

    def downloadImages(self, pages=1):
        for page in range(pages+1):
            resourcesUrl = self.getEpisodesUrls(page)
            for (episodeName, episodesUrls) in resourcesUrl.items():
                for episodesUrl in episodesUrls:
                    imageUrls = self.getImageUrl(episodesUrl)
                    count = 0
                    for imageUrl in imageUrls:
                        postfix = self.getImagePostfix(imageUrl)
                        fileName = episodeName+'_'+str(count)+postfix
                        self.saveImage(imageUrl, page, fileName)
                        count += 1

    def saveImage(self, image_url, page_number, file_name):
        """
        :param image_url:
        :param page_number:
        :param file_name:
        :return:
        """
        try:
            folder_name = str('image\\' + str(page_number))
            if not os.path.exists(folder_name):
                print('创建文件夹...')
                os.makedirs(folder_name)

            r = requests.get(image_url)
            filename = folder_name + '\\' + str(file_name) + '.jpg'
            with open(filename, 'wb') as fo:
                fo.write(r.content)
        except Exception as e:
            print(e)


if __name__ == "__main__":
    porn_image_crawler = porn_image_crawler()
    porn_image_crawler.HostUrl = 'https://cc.lvrts.com'
    porn_image_crawler.CategoryUrl = '/thread0806.php?fid=15'
    porn_image_crawler.PagingPostfix = '&search=&page='
    # porn_image_crawler.downloadImages()

    # postfix = porn_image_crawler.getImagePostfix('http://kccdk.com/files/2020/06/26/e97f774d24643184.jpeg')
    # print(postfix)

    imageUrl = porn_image_crawler.getImageUrl(porn_image_crawler.sampleEpisode)
    print(imageUrl)
    # porn_image_crawler.getResponse(imageUrl,

    # print(porn_image_crawler.getEpisodesUrls())
    pass
