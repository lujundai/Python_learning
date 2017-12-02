import urllib2 

url = "http://10.97.122.57:8080/"
try:
    req = urllib2.Request(url)
except urllib2.HTTPError, e:
	print "The server couldn't fulfill the request."
	print "Error code:", e.code
except urllib2.URLError, e:
	print "We failed to reach server."
	print e.info()
	print e.reason
else:
	response = urllib2.urlopen(req)
	rep = response.read()
	info = response.info()
	print info
	


