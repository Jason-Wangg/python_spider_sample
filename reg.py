import re
#open file
f = open('/home/jason/python/src/inspire5.html', 'r')
newfile = open('/home/jason/python/src/result.xml','a')
res = f.read()
# Reg find quotes
pattern =re.compile('"/quotes/quotes.*?nal',re.S)
items = re.findall(pattern,res)
# for item in items:
#     print item
lists=[]
hrefs=[]
try:
    for item in items:

         lists.append('<item>'+item+'</item>'+'\n')
    hrefs=list(set(lists))
    hrefs.sort(key=lists.index)
    for href in hrefs:
        newfile.write(href)
        print 'write '+href
except Exception as e:
    e
