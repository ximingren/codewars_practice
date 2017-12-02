# coding:utf-8
import time
from re import sub


def printer_error(s):
    denominator=len(s)
    fraction=0
    for letter in s:
        if(letter>'m'):
            fraction+=1
    result=str(fraction)+'/'+str(denominator)
    return result

if __name__=='__main__':
    start=time.clock()
    'dd'.translate(None,"")
    print(printer_error('aaaaaaaaaabbmmmmmmmmmmmmmmmmxyz'))
    finish=time.clock()
    print('use time:%f'%(finish-start))
