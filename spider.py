import requests
from pyquery import PyQuery as pq
import little_spider

def main(url,k,j):

    print('此地区需爬取总页数为', 4)
    for i in range(1,5):

        rew = little_spider.get_page(url+'_'+str(i)+'.htm',k,j)
        if rew == 0:
            break





class ji_bing(object):

    def __init__(self):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36',
            'Host': 'haoping.haodf.com'
        }

    def get_url(self):

        url = 'https://www.haodf.com/jibing/xiaoerke/list.htm'
        response = requests.get(url, headers = self.headers).text
        doc = pq(response)
        items = doc.find('#el_tree_1000000 > div.kstl').items()
        for item in items:
            r_url = item.find('a').attr('href')
            yield r_url

    def get_jibing(self,url):

        response = requests.get(url,headers = self.headers).text
        doc = pq(response)
        items = doc.find('#el_result_content > div > div.ct > div.m_ctt_green ').items()
        for item in items:
            little_items = item.find('ul > li').items()
            for little_item in little_items:
                cell = little_item.find('a').attr('href')
                jibing.append(cell)



if __name__ == '__main__':
    s_url = 'https://www.haodf.com'
    jibing = []
    list(set(jibing))
    locate = ['beijing','shanghai','guangdong','guangxi','jiangsu','zhejiang','anhui','jiangxi','fujian','shandong','shanxi','hebei','henan','tianjin','liaoning','heilongjiang','jilin','hubei','hunan','sichuan','chongqing','shanxi','gansu','yunnan','xinjiang','neimenggu','hainan','guizhou','qinghai','ningxia']
    ji_bing = ji_bing()
    url = ji_bing.get_url()
    for i in url:
        ji_bing.get_jibing(s_url + i)
    for j in jibing:
        if j == None:
            continue
        for k in locate:
            print('正在爬取' + k + '的'+ j[8:-4] +'数据')
            l_url = s_url + j[:-4] + '/daifu_' + k + '_all_all_all_all'
            try:
                main(l_url,k,j[8:-4])
            except Exception as e:
                print(e,'获取失败')


