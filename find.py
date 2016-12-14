import re
i = 0
pattern = re.compile('<p class="qt.*?<',re.S)
r = open('/home/jason/python/src/parsed/parsed.xml','a')
for i in range(130):
    i=i+1
    f = open('./src/parsed/'+str(i)+'.html','r')
    text = f.read()
    items = re.findall(pattern,text)
    for item in items:
        r.write(item+'/p>\n')
        print 'write '+item
