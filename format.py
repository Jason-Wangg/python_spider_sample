import  xml.dom.minidom
# 打开/新建XML文档
f = open('/home/jason/python/quotes.xml','w')
#位置标示
i =0
#dom读取原XML文件，构造DOM对象
dom = xml.dom.minidom.parse('./src/parsed/parsed.xml')
#获取文档节点
root = dom.documentElement
#获取item节点元素，并将所有item元素放入quotes[]
quotes = dom.getElementsByTagName('item')
#遍历quotes[]并获取节点中间的数据
for quote in quotes:
    i=i+1
    temp = '<item name = "quote'+str(i)+'">'+quote.firstChild.data+'</item>'+'\n'
    #写入文件
    f.write(temp)
    print 'write : '+temp
