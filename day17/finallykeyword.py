# try:
#     l = [1,2,3]
#     x = int(input("Enter index:"))
#     print(l[x])
# except:
#     print("index out of bound")
# finally:
#     print("i'm always executing")

def func1():
    try:
        l = [1,2,3]
        x = int(input("Enter index:"))
        print(l[x])
        return l[x]
    except:
        print("index out of bound")
        return 1
    finally:
        print("i'm always executing")#it always executed

t = func1()
print(t)
