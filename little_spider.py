import requests
from pyquery import PyQuery as pq
import re
import pymongo
client = pymongo.MongoClient('localhost')
db = client['hospital2']

def get_page(url,k,j):
    try:
        partten = '院.*?科'
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36',
            'Host': 'haoping.haodf.com'
        }
        response = requests.get(url,headers = headers).text
        doc = pq(response)
        items = doc.find('#disease > div > div.fl.left_con1.self_typeface1 > div.pr25 > ul > li').items()
        for item in items:
            keshi = re.findall(partten, item.find('div > div.doctor_photo_serviceStar > div.oh.zoom.lh180 > p:nth-child(1) > a:nth-child(3) > span').text())
            hospital = re.findall('.*?院', item.find('div > div.doctor_photo_serviceStar > div.oh.zoom.lh180 > p:nth-child(1) > a:nth-child(3) > span').text())
            detail = {
                '姓名': item.find(' div > div.doctor_photo_serviceStar > div.oh.zoom.lh180 > p:nth-child(1) > a.blue_a3').text(),
                '职称': item.find('div > div.doctor_photo_serviceStar > div.oh.zoom.lh180 > p:nth-child(1) > span').text(),
                '地区': k ,
                '所查疾病': j,
                '医院': str(hospital)[2:-2],
                '科室': str(keshi)[3:-2],
                '推荐度': item.find('div > div.doctor_photo_serviceStar > div.oh.zoom.lh180 > p:nth-child(2) > span.patient_recommend > a > i').text(),
                '擅长': item.find('div > div.doctor_photo_serviceStar > div.oh.zoom.lh180 > p:nth-child(4)').text()[3:]
            }
            print(detail)
            try:
                if db['doctor_detail'].insert(detail):
                    print('保存成功')
            except Exception:
                print('保存失败')
    except Exception:
        return 0

if __name__ == '__main__':
    get_page()