
import  requests
from lxml import etree
import time
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36"
}
url = 'http://www.59xihuan.cn/'
def main():
    for i in range(1,447):
        html = requests.get(r"http://www.59xihuan.cn/index_"+str(i)+".html", headers=headers).text
        etree_html = etree.HTML(html)
        title = etree_html.xpath('//div[@class="pic_text1"]')
        img = etree_html.xpath('//div[@class="pic_text1"]/p/img/@src')
        timex = etree_html.xpath('//div[@class="label"]/div[@class="time"]')
        for j in range(0,len(title)):
            createTime = timex[j].text.replace(" ", "")
            createTime = createTime.replace("\r\n\r\n", "")
            createTime = createTime.strip()
            titlex = title[j].text.replace("\r\n\r\n        \r\n\r\n          ", "")
            titlex = titlex.replace("\r\n\r\n      ", "")
            titlex = titlex.strip()
            timeArray = time.strptime(createTime+" 13:45:13","%Y-%m-%d %H:%M:%S")
            timestamp =int(time.mktime(timeArray))
            print("标题",titlex)
            print("时间",createTime)
            print("图片",url + img[j])
            print("时间戳",timestamp)
            print("第" + str(i) + "页")
            print("#"*100)
            item = {
                "createTime": createTime,
                "title": titlex,
                "author": "博主",
                "classify": "心灵鸡汤",
                "content": "",
                "contentType": "html",
                "label": "['心灵鸡汤']",
                "totalCollection": 0,
                "totalVisits": 0,
                "totalZans": 0,
                "uniqueId": "",
                "qrCode": "cloud://test-09ab26.7465-test-09ab26-1256087376/3397e9015d832dce00a1f93e35ca4f1f.png",
                "defaultImageUrl": url + img[j],
                "sourceFrom": "admin",
                "timestamp": timestamp,
                "digest": "",
                "isShow": 1,
                "totalComments": 0,
                "originalUrl": ""
            }
            f = open('jitang.json',mode='a',encoding="utf-8")
            f.write(str(item))
            f.write('\n')
if __name__ == '__main__':
    main()


