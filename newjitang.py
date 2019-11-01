import  requests
from lxml import etree
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36"
}
url = 'http://www.59xihuan.cn/'
def  main(i):
    html = requests.get(r"http://www.59xihuan.cn/index_" + str(i) + ".html", headers=headers).text
    etree_html = etree.HTML(html)
    title = etree_html.xpath('//div[@class="pic_text1"]')
    img = etree_html.xpath('//div[@class="pic_text1"]/p/img/@src')
    timex = etree_html.xpath('//div[@class="label"]/div[@class="time"]')
    for j in range(0, len(title)):
        createTime = timex[j].text.replace(" ", "")
        createTime = createTime.replace("\r\n\r\n", "")
        createTime = createTime.strip()
        titlex = title[j].text.replace("\r\n\r\n        \r\n\r\n          ", "")
        titlex = titlex.replace("\r\n\r\n      ", "")
        titlex = titlex.strip()
        imgurl = url + img[j]
        print("标题", titlex)
        print("时间", createTime)
        print("图片", url + img[j])
        print("第" + str(i) + "页")
        print("#" * 100)
        item ={
            "标题":titlex,
            "时间":createTime,
            "图片地址":imgurl
        }
        f = open('newjitang.json', mode='a', encoding="utf-8")
        f.write(str(item))
        f.write('\n')
    if len(title) == 0:
        print("爬取完毕")
    else:
        main(int(i) + 1)
if __name__ == '__main__':
    i = 1
    main(i)