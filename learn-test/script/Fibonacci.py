#-*- coding: utf-8 -*-
# @Time    : 2019/5/1 14:45
# @Author  : HuZixia
# @File    : Fibonacci.py
import time

"""元组实现, 顺序循环"""
def fibonacci_1(n):
    fibs=[0,1]
    for i in range(n):
        fibs.append(fibs[-1]+fibs[-2])
    print(fibs[n])


"""迭代器实现，顺序循环"""
class Iterator:
    def __init__(self,n):
        """n int 指明生成数列的前n个数"""
        self.n=n
        #current 用来保存当前数列中的第几个数
        self.current=0
        #a 用来保存前前一个数， 初始值为数列中的第一个数0
        self.a=0
        #b 用来保存前一个数， 初始值为数列中的第二个数1
        self.b=1

    def __next__(self):
        """被next（）函数调用来获取下一个数"""
        if self.current<self.n:
            self.a,self.b=self.b,self.a+self.b
            self.current+=1
            return self.a
        else:
            raise StopIteration

    def __iter__(self):
        """迭代器的__iter__返回自身即可"""
        return self

def fibonacci_2(n):
    result=Iterator(n)
    for i in result:
        print(i,end=" ")


"""通过定制类实现，顺序循环"""
class Classs(object):
    def __getitem__(self, n):
        if isinstance(n,int):
            a,b=0,1
            for x in range(n):
                a,b=b,a+b
            return a
        elif isinstance(n,slice):
            start=n.start
            stop=n.stop
            a,b=0,1
            L=[]
            for x in range(stop):
                if x>=start:
                    L.append(a)
                a,b=b,a+b
            return L
        else:
            raise TypeError("Fib indices must be integers")
#得到一个类似于序列的数据结构，可以通过下标来访问数据：
def fibonacci_3():
    result=Classs()
    print(result[8:50])


"""顺序循环实现，时间复杂度O(n), 空间复杂度S(1)"""
def fibonacci_4(n):
    i,j=0,1
    while i<=n:
        print(i,end=" ",flush=True)
        i,j=j,i+j



"""递归，列表生成式实现
   时间复杂度：O(n) 空间复杂度：S(n)"""
def fibonacci_5(n):
    if n==0: return 0
    if n==1: return 1
    return fibonacci_5(n - 1) + fibonacci_5(n - 2)




"""列表生成式实现+缓存机制 递归+缓存"""
def fibonacci_6(n,cache=None):
    if cache is None:
        cache={}
    if n in cache:
        return cache[n]
    if n==0: return 0
    if n==1: return 1
    cache[n]=fibonacci_6(n-2,cache)+fibonacci_6(n-1,cache)
    return cache[n]


#普通数据的快速幂运算，运算改为矩阵乘法，ret改为单位矩阵即可
def qpow (base,exp):
    if exp==0: return 1
    ret=1
    while exp:
        if exp & 1:
            ret=ret*base
        base=base*base
        exp>>1
    return ret

"""矩阵方式， 时间复杂度：O(logn) 空间复杂度：O(1)"""
def fibonacci(n):
    if n<1: return (1,0)
    f_m_1,f_m=fibonacci(n>>1)
    if n&1: return f_m_1*(f_m_1+2*f_m),f_m_1**2+f_m**2
    else: return f_m_1**2+f_m**2,f_m*(2*f_m_1-f_m)





if __name__=="__main__":

    start = time.time()
    # fibonacci_1(50)
    # fibonacci_2(50)
    # fibonacci_3()
    # fibonacci_4(50)
    # print([fibonacci_5(n) for n in range(10)])
    # print([fibonacci_6(n) for n in range(50)])
    end = time.time()
    print(end-start)
