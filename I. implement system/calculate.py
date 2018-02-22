# -*- coding:utf-8 -*-
#!usr/bin/env python
import json

Json_file = open("./output.txt","r")
Json_file = json.load(Json_file)
'''
print(d)
print(d[u'\u5c07\u4e4b\u652c'])
print(u'\u5c07\u4e4b\u652c')
'''
def location(text):
    uni_text=unicode(text,"utf-8")
    print(Json_file[uni_text])
    return Json_file[uni_text]
def diff(t1,t2):
    x = t1[0]-t2[0]
    y = t1[1]-t2[1]
    print(x,y,(x**2+y**2)**0.5)
    
a =location("將之攬")
b =location("然後")
c =location("即使")
d =location("渾厚")
e =location("輕薄")

diff(a,b)
diff(c,b)
diff(d,e)
diff(d,a)
