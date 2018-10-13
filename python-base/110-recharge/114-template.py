import fileinput,  re

field_pat = re.compile(r'\[(.+?)\]')

scope = dict({})


def replacement(match):
    code = match.group(1)
    try:
        return str(eval(code, scope))
    except SyntaxError:
        exec(code, scope)
        return ''


# 将所有文本一个字符串的形式获取：
lines = []
for line in fileinput.input("./file/template.txt"):
    lines.append(line)
text = "".join(lines)

print(re.sub(field_pat, replacement, text))
print("########################")
print(field_pat.sub(replacement, text))
