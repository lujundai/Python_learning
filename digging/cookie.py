import urllib2  
import cookielib 

cookie = cookielib.CookieJar()  
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))  
response = opener.open('http://10.97.122.57:8080/')  
for item in cookie:  
    print 'Name = '+item.name  
    print 'Value = '+item.value  