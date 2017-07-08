#!/usr/bin/env python3

import os
import urllib
import requests

headers={
    'cookie':'__cfduid=dd90cc65e3067b4f78e64cf538544e4a01496836096',
    'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
}

for y in range(29,31):
    if y<10:
        code='118lxvs0000'+str(y)
    else:
        code='118lxvs000'+str(y)

    url = 'https://jp.netcdn.space/digital/video/'+str(code)+'/'+str(code)+'jp-'

    dir='./'+str(code)+'/'

    if not os.path.exists(dir):
        os.makedirs(dir)

    print "downloading with url "+str(code)
    for x in range(1,25):
        if not os.path.exists(dir+str(x)+'.jpg'):
            img_url=url+str(x)+'.jpg'
            res=requests.get(img_url,headers=headers,allow_redirects=False,vertify=False)

            # print(len(res.history))
            print(res.status_code)
            
            if res.status_code==200:
                with open(dir+str(x)+'.jpg','w') as f:
                    f.write(res.content)
            else:
                continue

# url='https://jp.netcdn.space/digital/video/118lxvs00002/118lxvs000021jp-21.jpg'
# # url2='https://itbilu.com/nodejs/npm/EJUJrGVsg.html'
# res=requests.get(url,headers=headers)
# print(res.status_code)