import urllib, urllib2
import base64
url = r'https://www.baidu.com/'
base64string = base64.encodestring('2469340911@qq.com:Aa123456').strip()
authheader = "Basic " + base64sring
req = urllib2.Request(url)
req.add_header('Authorization', authheader)
urllib2.urlopen(req)
