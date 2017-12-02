# coding:utf-8

# return masked string
def maskify(cc):
    if (len(cc)>=4):
        cc='#'  *(len(cc)-4)+cc[-4:]
    return cc

if __name__=='__main__':
    print(maskify("133333"))
