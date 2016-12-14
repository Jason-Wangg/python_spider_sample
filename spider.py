import urllib2

def getHtml(url):
    #user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36'
    #headers = { 'User-Agent' : user_agent }
    req = urllib2.Request(url)
    req.add_header('User-Agent','Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36')
    req.add_header('Host','www.brainyquote.com')
    req.add_header('GET',url)
    page = urllib2.urlopen(req)
    html = page.read()
    return html

html = getHtml("http://www.brainyquote.com/quotes/topics/topic_inspirational5.html")
try:
    f = open('/home/jason/python/src/inspire5.html', 'w')
    f.write(html)
except Exception as e:
    print e
