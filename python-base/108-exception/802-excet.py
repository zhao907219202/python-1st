try:
    x = int(input("Enter the first number"))
    y = int(input("Enter the second number"))
    print(x / y)
except:
    print("Something wrong happened...")

# 像这样捕捉所有异常是危险的，因为它会隐藏所有程序员未想到并且未做好准备处理的错误。
# 它同样会捕捉用户终止执行的Ctrl+C企图，以及用sys.exit函数终止程序的企图
# 这时用except Exception as e: 会更好一些，或者对异常对象e进行一些检查


while True:
    try:
        x = int(input("Enter the first number"))
        y = int(input("Enter the second number"))
        value = x / y
        print("x/y is ", value)
    except Exception as e:
        print("Invalid input:", e)
        print("Please try again.")
    else:
        break
