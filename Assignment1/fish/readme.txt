有关fish.py
使用了round函数，遇到了问题，网上资料如下：


1、round的结果跟python版本有关
我们来看看python2和python3中有什么不同：

$ python
Python 2.7.8 (default, Jun 18 2015, 18:54:19) 
[GCC 4.9.1] on linux2
Type "help", "copyright", "credits" or "license" for more information.
>>> round(0.5)
1.0
$ python3
Python 3.4.3 (default, Oct 14 2015, 20:28:29) 
[GCC 4.8.4] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> round(0.5)
0
好玩吗？

如果我们阅读一下python的文档，里面是这么写的：

在python2.7的doc中，round()的最后写着，"Values are rounded to the closest multiple of 10 to the power minus ndigits; if two multiples are equally close, rounding is done away from 0." 保留值将保留到离上一位更近的一端（四舍六入），如果距离两端一样远，则保留到离0远的一边。所以round(0.5)会近似到1，而round(-0.5)会近似到-1。

但是到了python3.5的doc中，文档变成了"values are rounded to the closest multiple of 10 to the power minus ndigits; if two multiples are equally close, rounding is done toward the even choice." 如果距离两边一样远，会保留到偶数的一边。比如round(0.5)和round(-0.5)都会保留到0，而round(1.5)会保留到2。

所以如果有项目是从py2迁移到py3的，可要注意一下round的地方（当然，还要注意/和//，还有print，还有一些比较另类的库）。

>>> round(2.675, 2)
2.67
python2和python3的doc中都举了个相同的栗子，原文是这么说的：

Note

The behavior of round() for floats can be surprising: for example, round(2.675, 2) gives 2.67 instead of the expected 2.68. This is not a bug: it’s a result of the fact that most decimal fractions can’t be represented exactly as a float. See Floating Point Arithmetic: Issues and Limitations for more information.
简单的说就是，round(2.675, 2) 的结果，不论我们从python2还是3来看，结果都应该是2.68的，结果它偏偏是2.67，为什么？这跟浮点数的精度有关。我们知道在机器中浮点数不一定能精确表达，因为换算成一串1和0后可能是无限位数的，机器已经做出了截断处理。那么在机器中保存的2.675这个数字就比实际数字要小那么一点点。这一点点就导致了它离2.67要更近一点点，所以保留两位小数时就近似到了2.67。

以上。除非对精确度没什么要求，否则尽量避开用round()函数。近似计算我们还有其他的选择：

使用math模块中的一些函数，比如math.ceiling（天花板除法）。
python自带整除，python2中是/，3中是//，还有div函数。
字符串格式化可以做截断使用，例如 "%.2f" % value（保留两位小数并变成字符串……如果还想用浮点数请披上float()的外衣）。
当然，对浮点数精度要求如果很高的话，请用嘚瑟馍，不对不对，请用decimal模块。
就酱。

来源地址：http://www.cnblogs.com/anpengapple/p/6507271.html