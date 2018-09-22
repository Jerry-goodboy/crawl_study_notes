> 爬虫介绍

爬虫时python最容易上手的一个方向，虽说容易上手，但是后面也十分难学。
因为爬虫并不局限于网络请求、网页解析。很多时候还需要与其他技术一起使用，
比如自己构建IP池、cookie池时需要用到 web 框架以及 redis 数据库，
破解验证码的话要会进行图像处理、以及编写一些算法（去噪算法等）。如果想自己处理验证码的话还需要自己训练机器学习模型。
当爬取数量变多时就需要多线程与多进程爬虫了。
当一台机器无法满足爬取需求时就必须掌握分布式爬虫，以及负载均衡。
同时反爬虫与反反爬虫的斗争也一直不会停止，一旦反爬虫有所变动，所有的爬虫项目几乎要重写。
若想要将项目部署到服务器，linux技术也是必不可少的。

以上一节我对爬虫的理解，讲述一下本项目的目的。本项目是想提供给那些已经掌握python基础，
想进一步深入了解python的人学习的。在这里面我不会过多的讲解基本知识，
以及很多东西都需要看完我提供的一些资料之后才能看懂我想表述清楚的东西。
因为我是初次写这种教程，所以有些有毛病的地方以及可以改进的地方欢迎在`issues`中提出来，
有更好的代码也欢迎 `pull requests`.

此项目主要使用的技术分别是：

+ requests
+ xpath
+ css selector
+ re
+ scrapy

第一个是最常用的网络请求库，然后便是三个网页解析的技术，最后是一个爬虫框架。
网络请求库是还有一个 urllib，但是那个库比较难用，我学了之后感觉没啥用，
所以这里我就不记录了。解析库也不只这三个，但是这三个最为好用且速度快。
最后则是爬虫框架 scrapy，这个框架是非常之好用，上手之后绝对是爱不释手。
所以在讲前面的东西时，我会过得比较快，只要知道、认识就可以了。
等到了scrapy时再系统的讲解。

再看本项目之前，麻烦把以下这些技术给过一下，不然看着会有点吃力。

requests： <br>
http://docs.python-requests.org/zh_CN/latest/user/quickstart.html<br>
https://github.com/1621521894/notes/blob/master/crawler/some_notes/requests.md<br>
xpath：<br>
http://www.w3school.com.cn/xpath/index.asp<br>
https://github.com/1621521894/notes/blob/master/crawler/some_notes/Xpath.md<br>

css selector: <br>
http://www.w3school.com.cn/cssref/css_selectors.asp<br>
https://github.com/1621521894/notes/blob/master/crawler/some_notes/pyquery.md<br>

re：
https://pythoncaff.com/docs/pymotw/re-regular-expression/78<br>
https://github.com/1621521894/notes/blob/master/crawler/some_notes/regex.md<br>

对于基础不好的同学，可以先去看一下这几个教程然后再回来学也是一样：

https://pythoncaff.com/docs/tutorial/3.7.0<br>
https://pythoncaff.com/docs/pymotw<br>
https://pythoncaff.com/docs/python-guide/2018<br>