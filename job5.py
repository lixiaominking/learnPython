# -*- coding: utf-8 -*-
#for循环例子
names=['zhangsan','lisi','wangwu']
for name in names:
    print(name)

sum=0
for x in [1,2,3,4,5,6,7,8,9,10]:
    sum=sum+x
print(sum)

#range函数
sum1=0
for x in range(101):
    sum1=sum1+x
print(sum1)

#while循环
s=0
n=99
while n>0:
    s=s+n
    n=n-2
print(s)

#例题，请利用循环依次对list中的每个名字打印出Hello, xxx!
L = ['Bart', 'Lisa', 'Adam']
for i in L:
    print('hello,',i,'!')

#break
n=1
while n<=100:
    if n>20:
        break
    print(n)
    n = n + 1
print('END')

#continue
#只打印1-10内的奇数
n=0
while n<=10:
    n = n + 1
    if n%2==0:
	    continue
    print(n)


#dict
#初始化
d={'zhangsan':100,'lisi':99,'wangwu':89}
#新增key
d['zhaoliu']=70
#修改zhaoliu的值由70-95
d['zhaoliu']=95
#查找,存在True,不存在False
'zhaoliu' in d
#查找,存在返回value值，不存在返回None,还可以给新key赋值
d.get('zhangsan')
d.get('tianqi',94)
#删除
d.pop('tianqi')


