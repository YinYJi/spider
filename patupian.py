import requests
form lxml import etree
class Spider (object):
    def __init__(self):
        self.url = "http://www.mmjpg.com/"
        self.headers = {
            "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; WOW64) Apple"
            "Referer" : "http://www.mmjpg.com/"
         }
    def start_request(self):
        for i in range(1, 105):
            if i == 1:
                #1.获取整体网页数据 requests
                response = requests.get(self.url)
            else:
                response = requests.get(self.url + "/home/" + str(i))
            html = etree.HTML(response.content.decode())
            self.xpath_data(html)

    def xpath_data(self, html):
        #2.抽取想要的数据 lxml.etree xpath
        src_list = html.xpath('//div[@class="pic"]/ul/li/a/img/@src')
        alt_list = html.xpath('//div[@class="pic"]/ul/li/a/img/@alt')
        for src, alt in zip(src_list, alt_list):
            file_name = alt + ".jpg"
            print("正在抓取" + file_name)
            response = requests.get(scr)
            #3.保存数据 with open
            with open(file_name, "wb") as f:
                f.write(response.content)



try:
    spider = Spider()
    spider.start_request()
pass



