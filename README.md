# note-python
<strong>return a or b</strong>
<br>
该语句表示：如果a不为None，则返回a;反之返回b。可以用于一些存在备份返回值的返回语句，省去了一个if判断语句。
<br><br>
类中的初始化函数方法<strong>__init__()</strong>的形参中必须写入self，其指向的是类的实例，并非该类本身，如若拥有一个和类本身交互的函数（即可以在不创建一个类的实例的前提下使用该函数），则也可以借用<strong>@classmethod</strong>。<br>
同时@classmethod因其所修饰的函数必须包含表示类本身的cls形参，所以也可以与类中的其他函数进行交互，并使用该形参进行一般的类实例构造方法来构造新的实例类，而且返回该类。<br>
scrapy框架中关于spider和crawler的关系，先通过Crawler(spidercls,settings)构造得到我们所写的spider类所对应的crawler，之后通过spidercls.fron_crawler(crawler, *args, **kwargs)构造得到我们的spider，并将该spider和crawler联系起来。<br>

setting和crawler之间的关系，scrapy框架各部件之间的运作关系（代码实现层面的）
