import urllib
import urllib2

url = 'http://www.brainyquote.com/top_100_quotes'
user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36'
headers = { 'User-Agent' : user_agent }
request = urllib2.Request(url)
response = urllib2.urlopen(request)
page = response.read()
