#-*- coding: utf-8 -*-
# @Time    : 2019/5/2 17:40
# @Author  : HuZixia
# @File    : Sort.py

import time,math

"""冒泡排序是一种稳定的排序方法, 平均时间复杂度为O(n^2)"""
def bubble_sort(list):
    length=len(list)#获取list的长度
    for i in range(0,length-1): #一共进行length-1轮对比,外层循环控制排序趟数
        for j in range(0,length-1-i): #内层循环控制每一趟排序多少次
            if list[j]>list[j+1]: #进行交换
                tmp=list[j]
                list[j]=list[j+1]
                list[j+1]=tmp
    for item in list: #打印输出
        print(item)
    return list



"""快速排序是不稳定的排序, 时间复杂度为O(nlogn)"""
def quick_sort(list,low,high):
    if low<high:  #判断low是否小于high,如果为false,直接返回
        i,j=low,high
        key=list[low] #设置基准位
        while i<j:
            while list[j]>=key and i<j: j=j-1 #从后半部分向前扫描,如果列表右边的数,比基准数大或相等,则前移一位直到有比基准数小的数出现
            while list[i]<=key and i<j: i=i+1 #从前半部分向后扫描,如果列表左边的数,比基准数小或相等,则前移一位直到有比基准数大的数出现
            if i<j: #如果满足条件则交换ij数字
                tmp=list[i]
                list[i]=list[j]
                list[j]=tmp
        #最后将基准位和(low和high)相等位置的数字交换
        list[low]=list[i]
        list[i]=key
        #递归调用左半数列
        quick_sort(list,low,j-1)
        #递归调用左半数列
        quick_sort(list,j+1,high)

    for item in list:
        print(item)
    return list



"""对给定的n个数的序列，返回序列中的最大和最小的数
    最简单的方法: 逐个比较，返回最大的数和最小的数。此时需要进行2n次的比较。"""
def getMax_1(list):
    max=list[0]
    for i in range(0,len(list)-1):
        if list[i]>max: max=list[i]
    return max

def getMin_1(list):
    min=list[0]
    for i in range(0,len(list)-1):
        if list[i]<min: min=list[i]
    return min


"""对给定的n个数的序列，返回序列中的最大和最小的数
   先对各数据两两比较，将大的放在一起，小的放在一起，然后从大数集合中找最大值，从小数集合中找最小值。此时共需3n/2=1.5n次的比较。"""
def exchange(list):
    for i in range(0,math.floor((len(list)-1)/2)):
        if list[i]>list[len(list)-1-i]:
            tmp=list[len(list)-1-i]
            list[len(list)-1-i]=list[i]
            list[i]=tmp
    return list

def getMax_2(list):
    max=list[len(list)-1]
    for i in range(len(list)-1,math.floor((len(list)-1)/2)-1,-1):
        if(list[i]>max):max=list[i]
    return max

def getMin_2(list):
    min=list[0]
    for i in range(0,math.floor((len(list)-1)/2)+1):
        if(list[i]<min): min=list[i]
    return min



"""对给定的n个数的序列，返回序列中的最大和最小的数
   前两个数比较,大的为最大值, 小的为最小值, 用掉一次比较
   后面n-2个数, 每两个比较, 大的同最大值比较, 小的同最小值比较, 3*(n-2)/2次比较, 共(1.5n-2)次比较。"""
def getMaxMin(list):
    if list[0]>list[1]:
        max,min=list[0],list[1]
    else:
        max,min=list[1],list[0]
    for i in range(2,len(list)-1):
        if(list[i]>list[len(list)-1-i]):
            if(list[i]>max):max=list[i]
            if(list[len(list)-1-i]<min): min=list[len(list)-1-i]
        else:
            if(list[len(list)-1-i]>max): max=list[len(list)-1-i]
            if(list[i]<min):min=list[i]
    print(max)
    print(min)
    return list



if __name__=="__main__":
    start=time.time()
    list=[1,4,22,0,44,2,8]
    # print(getMax_1(list))
    # print(getMin_1(list))

    list=exchange(list)
    print(getMax_2(list))
    print(getMin_2(list))

    # list=bubble_sort(list)
    # list=quick_sort(list,0,len(list)-1)
    # getMaxMin(list)
    end=time.time()
    print(end-start)