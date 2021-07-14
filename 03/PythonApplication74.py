# 完整的try

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
# 排除错误

else:
    print("no error")
# 若无错执行

finally:
    print("ending")
# 无论如何都执行