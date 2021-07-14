#分类拦截

#报错时的最后一行第一个词就是错误原因
#本题中是 ValueError 和 ZeroDivisionError

try:
    x=int(input("num is "))    
    y=8/x    
    print(y)
except ZeroDivisionError:
    print("num should not be 0")
except ValueError:
    print("error input")
except Exception as result:
    print("unknown error ",result)

#若对多种错误进行统一操作，则用 except(A,B)
#最后一个except拦截意料之外