1.1 兔子数列
一般而言，兔子在出生两个月后，就有繁殖能力，一对兔子每个月能生出一对小兔子来。如果所有兔子都不死，那么一年以后可以繁殖多少对兔子？

斐波那契数列又因数学家列昂纳多·斐波那契以兔子繁殖为例子而引入，故又称为“兔子数列”。
一般而言，兔子在出生两个月后，就有繁殖能力，一对兔子每个月能生出一对小兔子来。如果所有兔子都不死，那么一年以后可以繁殖多少对兔子？
我们不妨拿新出生的一对小兔子分析一下：
第一个月小兔子没有繁殖能力，所以还是一对
两个月后，生下一对小兔对数共有两对
三个月以后，老兔子又生下一对，因为小兔子还没有繁殖能力，所以一共是三对
依次类推可以列出下表：
经过月数	1	2	3	4	5	6	7	8	9	10	11	12	…
幼仔对数	1	0	1	1	2	3	5	8	13	21	34	55	…
成兔对数	0	1	1	2	3	5	8	13	21	34	55	89
总体对数	1	1	2	3	5	8	13	21	34	55	89	144
幼仔对数=前月成兔对数
成兔对数=前月成兔对数+前月幼仔对数
总体对数=本月成兔对数+本月幼仔对数
可以看出幼仔对数、成兔对数、总体对数都构成了一个数列。这个数列有关十分明显的特点，那是：
前面相邻两项之和，构成了后一项。

1.2 跨楼梯组合
有一段楼梯有10级台阶，规定每一步只能跨一级或两级，要登上第10级台阶有几种不同的走法?
这就是一个斐波那契数列：登上第一级台阶有一种登法；登上两级台阶，有两种登法；登上三级台阶，有三种登法；登上四级台阶，有五种登法……
1，2，3，5，8，13……所以，登上十级，有89种走法。


1.3 掷硬币不连续情形
一枚均匀的硬币掷10次，问不连续出现正面的可能情形有多少种？
答案是:
（1/√5)∗[(1+√5)/2](10+2)−[(1−√5)/2](10+2)=144 （1/√5)*{[(1+√5)/2]^(10+2) - [(1-√5)/2]^(10+2)}=144
假设一枚均匀的硬币掷i次，不连续出现正面的可能情形有ai种
那么连续投掷n-2次，不连续出现正面的可能情形有a(n-2)种
那么连续投掷n-1次，不连续出现正面的可能情形有a(n-1)种
显然，当连续投掷n-1次后符合要求，共a(n-1)种投法，
此时若第n次投掷出反面，也一定符合要求
这是一种情况，但是是建立在前n-1次投掷符合要求的情况下
这种情况共a(n-1)种投法
而若第第n次投掷出正面，则此时前n次投掷符合要求的条件是：
前n-2次投掷符合要求，且第n-1次投掷出反面
这是另一种情况，但是是建立在前n-2次投掷符合要求的情况下
这种情况共a(n-2)种投法
换句话说，前n次投掷符合条件（不连续出现正面）是建立在两种情况下的：
要么第n次投掷出反面，且前n-1次投掷都符合条件
要么第n次投掷出正面，第n-1次投掷出反面，且前n-2次投掷都符合条件
故an=a(n-1)+a(n-2)
n∈N*，n>=3
a1=2,a2=3
最终可得 An=(1/√5)*{[(1+√5)/2]^(n+2)-[(1-√5)/2]^(n+2)}


1.4 斐波那契数列和黄金分割的关系
a(n+2) / a(n+1) = 1 + an / a(n+1)
设a(n+1) / an =Xn >0,
则X(n+1) =1 + 1 / Xn
假设Xn无穷大,则X(n+1)也无穷大,与X(n+1)=1+1/Xn趋向于1矛盾.
假设Xn无限接近0,则X(n+1)也无限接近0,与X(n+1)=1+1/Xn趋向于无穷大矛盾.
所以,Xn必然有极限值.
设a(n+1)/an的极限为x,则有
x=1+1/x,即x^2-x-1=0 x>0, x=(1+√5)/2
设an/a(n+1)的极限为x,则有
x+1=1/x,即x^2+x-1=0 x>0, x=(-1+√5)/2
当n趋向于无穷大时，前一项与后一项的比值越来越逼近黄金分割0.618（或者说后一项与前一项的比值小数部分越来越逼近0.618）