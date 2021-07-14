# 主动报错

def x():
    a=input("password : ")
    if len(a)>8:
        return a
    else:#此时无return 若print则为none
        print("error")
        x=Exception("密码过短")
        raise x
try:
    print(x())
except Exception as re:
    print(re)
