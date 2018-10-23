"""
错误处理
    1. except 如果没有抓捕 可以有else语句
        try:
            print('try...')
            r = 10 / int('2')
            print('result:', r)
        except ValueError as e:
            print('ValueError:', e)
        except ZeroDivisionError as e:
            print('ZeroDivisionError:', e)
        else:
            print('no error!')
        finally:
            print('finally...')
        print('END')

    2. 打印异常栈
        import logging

        def foo(s):
            return 10 / int(s)

        def bar(s):
            return foo(s) * 2

        def main():
            try:
                bar('0')
            except Exception as e:
                logging.exception(e)

        main()
        print('END')

    3. 抛出错误
        def foo(s):
            n = int(s)
            if n==0:
                raise ValueError('invalid value: %s' % s)
            return 10 / n

        def bar():
            try:
                foo('0')
            except ValueError as e:
                print('ValueError!')
                raise

        bar()

"""

#  运行下面的代码，根据异常信息进行分析，定位出错误源头，并修复：
from functools import reduce


def str2num(s):
    # return int(s)
    return float(s)


def calc(exp):
    ss = exp.split('+')
    ns = map(str2num, ss)
    return reduce(lambda acc, x: acc + x, ns)


def main():
    r = calc('100 + 200 + 345')
    print('100 + 200 + 345 =', r)
    r = calc('99 + 88 + 7.6')
    print('99 + 88 + 7.6 =', r)


main()
