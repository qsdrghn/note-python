# note-python
<strong>return a or b</strong>
<br>
该语句表示：如果a不为None，则返回a;反之返回b。可以用于一些存在备份返回值的返回语句，省去了一个if判断语句。
<br>
类中的初始化函数方法<strong>__init__()</strong>的形参中必须写入self，其指向的是类的实例，并非该类本身，如若拥有一个和类本身交互的函数（即可以在不创建一个类的实例的前提下使用该函数），则也可以借用<strong>@classmethod</strong>。<br>
同时@classmethod因其所修饰的函数必须包含表示类本身的cls形参，所以也可以与类中的其他函数进行交互，并使用该形参进行一般的类实例构造方法来构造新的实例类，而且返回该类。<br>
//表示整除，/表示普通的除（返回值为浮点数），最少保留一位小数。
<strong>列表去重：</strong>已有列表l1=[1,1,2,3,2];list(set(l1))即可实现列表去重，set()指将变量转化为集合变量，再使用list()转化为列表变量。
# note-scrapy
setting和crawler之间的关系，scrapy框架各部件之间的运作关系（代码实现层面的）<br>
scrapy0.24版本的官方文档<span>https://doc.scrapy.org/en/0.24/index.html</span>内附搜索功能，框架源代码以及部分看不懂的框架内定义好的规则，通过检索即可了解，以下仅是部分文档内没有，个人总结的踩过的一些坑。<br>

<h3>scrapy的异步处理大概原理</h3>
spider和其他中间件产生的request会先进入scheduler等待调度，与此同时scheduler中已存在的批量的request同时进行请求得到response，与此同时对早先已经得到的response进行处理，得到下一步的request或者item，前者则放入scheduler准备调度，后者则传入到Item Pipeline进行信息的清晰和保存，同理，在进行上述操作时，会有已经传入过来的item进行后续处理。框架在使用Request进行请求时，需要先使用框架内的Request()函数进行请求构建，并将其作为调度器（schedular）中等待调度（向服务器发起请求）。该框架一般会同时发起请求，默认同时发起16个请求，但如此容易被反爬，一般需要在settings.py文件中重新设置CONCURRENT_REQUESTS。<br>
<h3>中间件及其他部件的使用</h3>
Downloader、Scheduler以及Engine是我们平常不用管的部分，只需在设置setting时设置一些处理延迟以及一些同时处理的请求数目、请求重试次数等变量即可。两大中间件Downloaer Middleware和Spider Middleware可以自己写，也可以不用管，默认使用框架自带的，通常可能需要自己基于该框架书写下中间件Downloaer Middleware，从而实现符合自己情况的重试中间件、更换代理、Cookies中间件等功能，目前只需要重写重试中间件（已上传，适用于任何情况，可直接使用），其他中间件文件日后使用到会继续构造并上传。

<h3>setting的设置问题</h3>
我们所通过scrapy框架构造的自己的爬虫代码，其中各项设置通过setting，从而实现大部分变量的统一管理。setting由四大部分组成(具体看scrapy官方文档，文档内直接搜索setting即可)，在crawler的实例类开始被构造之前，各个setting配置会根据优先级形成最终所用的setting配置，从而在后续crawler构造时，将二者联系起来，方便后续的使用和传递。<br>

<h3>crawler和spider之间的关系</h3>
spider为我们在所写的spaider文件中进行定义，其主要用途为：构建访问请求request；定义返回得到的response的处理方法函数。而crawler不需要我们进行定义，其主要作用为存储一些爬虫的自身信息，比如setting设置、一些自身所设置的变量（统计爬取的数据个数的变量）。scrapy框架中关于spider和crawler的关系，先通过Crawler(spidercls,settings)构造得到我们所写的spider类所对应的crawler（spidercls为我们所构建的spider的类名，即spider的初始类），之后通过spidercls.fron_crawler(crawler, *args, **kwargs)构造得到我们所需要使用的spider实例，并将该spider和crawler联系起来。<br>


<h3>请求头Headers的构建</h3>
构建时都应在setting.py将ROBOTSTXT_OBEY的值改为False，表示不适用默认的爬虫请求头规则，剩下的构建方法，目前本人使用过的有以下两种：
一、可以在定义spider时模仿使用requests库时定义请求头时的操作进行定义，并在后续的Request()请求构建时添加相应的形参；
二、在setting.py文件中定义DEFAULT_REQUEST_HEADERS（字典变量）。<br>

<h3>推荐爬虫运行方案</h3>
一、使用传统的命令行进行运行，此时推荐使用log打印日志的方式进行运行情况的输出（个人不熟悉，所以习惯用第二个）；
二、写一个start.py用于爬虫开始，这样即可在控制台观察运行情况，方便print出信息来进行观察。python中拥有库subprocess，其中subprocess.call()函数可以通过传入一个cmd命令列表，从而在该文件所在地址开始执行cmd命令。cmd命令列表指的是将命令按照空格分成由字符串组成的列表。



