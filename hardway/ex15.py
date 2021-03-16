from sys import argv
from time import sleep

sc,filename=argv

#print(filename)
name=filename

#print(name)

file_1=name.split("\\")[-1]
#print(a[-1])
#sleep(5)

txt=open(file_1,encoding="utf-8")
print(txt.read())
sleep(6)