import requests
from time import sleep

def get_page_source(url):

    #模拟浏览器请求
    header = {
        'Host': 'maoyan.com',
        'Connection': 'keep-alive',
        'Cache-Control': 'max-age=0',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Sec-Fetch-Site': 'none',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-User': '?1',
        'Sec-Fetch-Dest': 'document',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
        'Cookie': '__mta=149389193.1592828610489.1592831416170.1592831422701.16; _lxsdk_cuid=172dbfb94aac8-085c0ae989cac4-38710758-2f7600-172dbfb94aac8; _lx_utm=utm_source%3DBaidu%26utm_medium%3Dorganic; uuid_n_v=v1; uuid=2D601B10B48311EAA1F189776DB49E0567DB89A3B006422598C22311D3BA31CA; mojo-uuid=5b0ac973cd68b25c55eab0ccfdc4ab31; _lxsdk=2D601B10B48311EAA1F189776DB49E0567DB89A3B006422598C22311D3BA31CA; _csrf=5aa21337f5533ba5d6fa2177ca912840c360702c342b44722f1e193b7032edf3; mojo-session-id={"id":"b9b9f0e5f35dd2de9afb58824837cd16","time":1593002236493}; mojo-trace-id=1; Hm_lvt_703e94591e87be68cc8da0da7cbd0be2=1592828641,1592830751,1592920528,1593002237; Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2=1593002237; __mta=149389193.1592828610489.1592831422701.1593002236647.17; _lxsdk_s=172e6551aa1-1de-99c-da0%7C%7C2'
    }
    
    return(requests.get(url,headers=header).text) 


if __name__ == '__main__':

    for i in range(10):

        print('https://maoyan.com/films?showType=3&offset=' + str(30 * i))

        sleep(15)
        
        

#print(get_page_source('https://maoyan.com/films?showType=3'))



#https://maoyan.com/films?showType=3&offset=0
