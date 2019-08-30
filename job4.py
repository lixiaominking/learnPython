# -*- coding: utf-8 -*-
#小明身高1.75，体重80.5kg。请根据BMI公式（体重除以身高的平方）帮小明计算他的BMI指数，并根据BMI指数：
#    低于18.5：过轻
#    18.5-25：正常
#    25-28：过重
#    28-32：肥胖
#    高于32：严重肥胖
#用if-elif判断并打印结果：
age=input('请输入您的年龄:')
#height = 1.75
#weight = 80.5
height=float(input('请输入您的身高(m)：'))
weight=float(input('请输入您的体重(kg)：'))
age=int(age)
if age >= 18: 
    print('您的年龄是：',age,'adult')
else:
    print('您的年龄是：',age,'teenager')
#判断是否是成年人	
BMI=weight/(height*height)  #计算BMI值
BMI=float('%.2f' % BMI) #将BMI值转换成浮点数，且小数点后两位小数
if BMI<18.5:
    print('您的身高是:',height,'m')
    print('您的体重是:',weight,'kg')
    print('您的BMI指数是:',BMI,'体重过轻')
elif BMI>=18.5 and  BMI<=25:
    print('您的BMI指数是:',BMI,'体重正常')
elif BMI>25 and  BMI<=28:
    print('您的BMI指数是:',BMI,'体重过重')
elif BMI>28 and  BMI<=32:
    print('您的BMI指数是:',BMI,'体重肥胖')
elif BMI>32:
    print('您的BMI指数是:',BMI,'体重严重肥胖')