# 异常传递


# 函数有问题，体现在主函数中

def demo1():
    
    x=int(input("num "))
    
    return x
def demo2(x):
    
    print(8/x)
    


try:
    print("hello")
    x=demo1()
    demo2(x)
except ZeroDivisionError:
    print("zero error")
except ValueError:
    print("input error")
except Exception as result:
    print(result," error")
else:
    print("pass")
