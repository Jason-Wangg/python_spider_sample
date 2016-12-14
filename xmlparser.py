import  xml.dom.minidom
import spider
dom = xml.dom.minidom.parse('/home/jason/python/src/result.xml')
root = dom.documentElement
urls= dom.getElementsByTagName('item')
lists=[]
htmls=[]
i = 0
for url in urls:
    lists.append('http://www.brainyquote.com'+url.firstChild.data)
for lst in lists:
    temp=spider.getHtml(lst)
    i=i+1
    path= '/home/jason/python/src/parsed/'+str(i)+'.html'
    f = open(path, 'w')
    f.write(temp)
    print 'write'+path
