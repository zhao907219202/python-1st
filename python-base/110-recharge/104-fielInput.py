import fileinput

file = fileinput.input("./file/input.txt")
for line in file:
    line = line.strip()
    num = fileinput.filelineno()
    name = fileinput.filename()
    print("Line: %-40s # %2i" % (line, num))


# fileinput.lineno()      # 累计行数
# fileinput.filelineno()  #当前文件行数
# fileinput.input()       #isplace=True时 把打印内容回写到文件中
