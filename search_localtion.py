import urllib.request,urllib.parse,string,json

q=input("请输入要查找位置的关键字: ")
r=input("请输入要查找的城市: ")
url="http://api.map.baidu.com/place/v2/search?q="+q+"&region="+r+"&output=json&ak=Eg52GDexSslhTV71F0QbNnvZ"
urllib.parse.quote(url,safe=string.printable)
page=urllib.request.urlopen(urllib.parse.quote(url,safe=string.printable))
text=page.read().decode("utf8")
data=json.loads(text)
for i in range(len(data["results"])):
      print("")
      print(data["results"][i]["name"])
      print(data["results"][i]["address"])
