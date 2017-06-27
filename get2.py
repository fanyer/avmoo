#!/usr/bin/env python2




import os
import urllib
import urllib2
import requests
               

for y in range(1,31):
	if y<10:
		code='118lxvs0000'+str(y)
	else:
		code='118lxvs000'+str(y)

	url = 'https://jp.netcdn.space/digital/video/'+str(code)+'/'+str(code)+'jp-'

	dir='./'+str(code)+'/'

	if not os.path.exists(dir):
	    os.makedirs(dir)

	               
	# print "downloading with urllib"+str(code)
	# for x in range(2,25):
	#     urllib.urlretrieve(url+str(x)+'.jpg', dir+str(x)+".jpg")
	#     print "start sleep 1 x:"+str(x)
	#     time.sleep(1)


# for y in range(1,31):
# 	if y<10:
# 		code='118lxvs0000'+str(y)
# 	else:
# 		code='118lxvs000'+str(y)

# 	url = 'https://jp.netcdn.space/digital/video/'+str(code)+'/'+str(code)+'jp-'

# 	dir='./'+str(code)+'/'

# 	if not os.path.exists(dir):
# 	    os.makedirs(dir)

	               
# 	print "downloading with urllib"+str(code)
# 	for x in range(1,25):
# 		img_url=url+str(x)+'.jpg'
# 		res=requests.get(img_url)
# 		with open(dir+str(x)+'.jpg','w') as f:
# 		    f.write(res.content)

# urllib.urlretrieve('https://jp.netcdn.space/digital/video/118lxvs00001/118lxvs00001jp-2.jpg', "./118lxvs00001/2.jpg")




# res=requests.get('https://jp.netcdn.space/digital/video/118lxvs00001/118lxvs00001jp-2.jpg')
# print res
# with open('pc.jpg','w') as f:
# 	for chunk in res.iter_content(chunk_size=1024):
# 		if chunk: # filter out keep-alive new chunks
# 			f.write(chunk)
# 			f.flush()
