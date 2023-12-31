from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return HttpResponse("index")

'''
#增加数据
#方法一
from book.models import BookInfo
book = BookInfo(
        name='django',
        pub_date='2001-1-1',
        readcount=10
    )
#方法二
BookInfo.objects.create(
        name='测试开发',
        pub_date='2002-1-1',
        readcount=10
)

#修改数据
#方法一
book = BookInfo.objects.get(id=6)
book.name = '运维开发'
book.save()
#方式二
BookInfo.objects.filter(id=6).update(name='爬虫入门',commentcount=666)  #仅限fileter使用update

#删除数据
#方法一
book = BookInfo.objects.get(id=1)
book.delete()
#方法二
BookInfo.objects.get(id=6).delete()
BookInfo.objects.filter(id=5).delete()
'''

'''#F对象实现二者比较
from book.models import BookInfo
from django.db.models import F
BookInfo.objects.filter(readcount__gte=F('commmentcount'))

#并且查询
BookInfo.objects.filter(readcount__gt=20).filter(commentcount_gt=10)
BookInfo.objects.filter(readcount__gt=20,id__lt=3)

#或者查询
from  django.db.models import Q
#或者语法格式:  BookInfo.objects.filter(Q(属性名__运算符=值)|Q(属性名__运算符=值)|...)
#并且语法格式:  BookInfo.objects.filter(Q(属性名__运算符=值)&Q(属性名__运算符=值)&...)
#非语法格式:  BookInfo.objects.filter(~Q(属性名__运算符=值))'''



#聚合函数
from book.models import BookInfo,PeopleInfo
from django.db.models import Sum,Max,Min,Avg,Count
BookInfo.objects.aggregate(Sum("readcount"))        #返回{属性名__聚合函数名：值}
BookInfo.objects.all().order_by("readcount")        #升序
BookInfo.objects.all().order_by("-readcount")       #降序

#关联查询
b=BookInfo.objects.get(id=1)
b.peopleinfo_set.all()                              #隐含属性
BookInfo.objects.filter(peopleinfo__name='郭靖')
BookInfo.objects.filter(peopleinfo__description__contains='八')
PeopleInfo.objects.filter(book__name='天龙八部')

