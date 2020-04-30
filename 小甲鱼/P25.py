import time

def hannuota(n,a="1号",b="2号",c="3号"):
    global i
    if n==1:
        i+=1
        #print(a,"---->",c,f'第{i}次移动')
    else:
        hannuota(n-1,a,c,b)
        i+=1
        #print(a,"---->",c,f'第{i}次移动')
        hannuota(n-1,b,a,c)

if __name__=="__main__":
    i=0
    for n in range(1,100):
        start = time.time()
        hannuota(n)
        end = time.time()
        t=(f"{n}层汉诺塔运行时间为{round((end - start),5)}秒\n")
        filename = '1.txt'
        with open(filename, 'a') as file_object:
            file_object.write(t)