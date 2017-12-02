# coding:utf-8
import time


# def nb_year(p0, percent, aug, p):
#      year=0
#      while p0<p:
#         year=year+1
#         p0 = p0 * (1 + percent*0.01) + aug
#      return year

# 用高递归函数实现递归
def nb_year(p0,percent,aug,p,year=0):
    if(p0<p):
        return nb_year(p0*(1+percent/100)+aug,percent,aug,p,year+1)
    return year

if __name__=='__main__':
    start=time.clock()
    print(nb_year(1500000,0.25,1000, 2000000))
    finish=time.clock()
    print("use time:%f" % (finish-start))

