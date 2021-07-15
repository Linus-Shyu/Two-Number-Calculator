#列一个标题。
print("Linuxu5610开发的计算器。")
#设置while循环变量。
counts=3
#设置while循环。
while counts>0:
    #设置变量用键盘记录函数存放用户输入的数据。
    str1=input("请用户输入第一个操作数：")
    str2=input("请用户输入第二个操作数：")
    #定义用户输入的数据类型。
    X=int(str1)
    Y=int(str2)
    #输出答案。
    print(X+Y)
    print(X-Y)
    print(X*Y)
    print(X/Y)
    print(X**Y)
    print(X//Y)
    


