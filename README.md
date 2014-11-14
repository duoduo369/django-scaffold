django-scaffold
===

django-scaffold是一个快速初始化django项目的脚手架，目前django版本采用1.4.8,不过脚手架里面可以比较方便的切到1.6.1，个人用暂时没问题，有问题请提issue.

为什么用1.4.8?
---
1. 因为足够.
2. django不是因为django的本版更高而更牛逼.
3. 有些库在我用的时候还是支持稳定的1.4.8的
4. 1.4.8的基本配置，文件结构和1.6一样(没错，oauth)

脚手架提供了什么
---
1. mako支持
2. 静态文件collect后添加hash
3. rename脚本，可以直接将django-scaffold改为你想要的名字

将来提供什么 TODO List
---
1. xadmin或者xadmin2
2. supervisor和gunicorn的基本配置
3. nginx的基本配置
4. log配置
5. 方便的开启关闭debug
6. python-oauth的一个fork版本，添加weibo, weixin等中国backend
7. 传文件
8. 切图片
9. 分页
10. 最新的requirements.txt
11. rest service
12. 权限的一些东西
