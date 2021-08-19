# note-python
<strong>return a or b</strong>
<br>
该语句表示：如果a不为None，则返回a;反之返回b。可以用于一些存在备份返回值的返回语句，省去了一个if判断语句。
<br><br>
类中的初始化函数方法<strong>__init__()</strong>的形参中必须写入self，其指向的是类的实例，并非该类本身，如若拥有一个和类本身交互的函数（即可以在不创建一个类的实例的前提下使用该函数），则也可以借用<strong>@classmethod</strong>。<br>
同时@classmethod因其所修饰的函数必须包含表示类本身的cls形参，所以也可以与类中的其他函数进行交互，并使用该形参进行一般的类实例构造方法来构造新的实例类，而且返回该类。<br>


setting和crawler之间的关系，scrapy框架各部件之间的运作关系（代码实现层面的）<br>
<strong>setting的设置问题</strong>
我们所通过scrapy框架构造的自己的爬虫代码，其中各项设置通过setting，从而实现大部分变量的统一管理。setting由四（五）大部分组成，在crawler的实例类开始被构造之前，各个setting配置会根据优先级形成最终所用的setting配置，从而在后续crawler构造时，将二者联系起来，方便后续的使用和传递。<br>
<strong>crawler和spider之间的关系</strong>
spider为我们在所写的spaider文件中进行定义，其主要用途为：构建访问请求request；定义返回得到的response的处理方法函数。crawler不需要我们进行定义，其主要作用为存储一些爬虫的自身信息，比如setting设置、一些自身所设置的变量（统计爬取的数据个数的变量）。scrapy框架中关于spider和crawler的关系，先通过Crawler(spidercls,settings)构造得到我们所写的spider类所对应的crawler（spidercls为我们所构建的spider的类名，即spider的初始类），之后通过spidercls.fron_crawler(crawler, *args, **kwargs)构造得到我们所需要使用的spider实例，并将该spider和crawler联系起来。<br>

框架在使用Request进行请求时，需要先使用框架内的Request()函数进行请求构建，并将其作为调度器（schedular）中等待调度（向服务器发起请求）。该框架一般会同时发起请求，默认同时发起16个请求，但如此容易被反爬，一般需要在settings.py文件中重新设置CONCURRENT_REQUESTS。<br>


//表示整除，/表示普通的除（返回值为浮点数），最少保留一位小数。
