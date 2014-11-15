django-scaffold
===

django-scaffold是一个快速初始化django项目的脚手架，目前django版本采用1.4.8,不过脚手架里面可以比较方便的切到1.6.1，个人用暂时没问题，有问题请提issue.

一些约定
---
如果想要方便的使用这个项目，有些约定是需要遵守的

1. linux or unix
2. 在你个人项目下建立projects文件夹，相对于/opt建立软连接 `cd ~ && mkdir projects && cd projects && sudo ln -s $(pwd)/projects /opt`
3. 将项目克隆到`/opt/projects`下
4. 使用项目里面的一些脚本, TODO: 添加如何使用，以及使用顺序

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

document
===

tools
---

rename_and_backup.py
---
备份并且重命名脚本, 会将项目中所有的old name全部替换为new name,包括各种配置文件等.

    cd /opt/projects/{your old project name}/tools
    ./rename_and_backup.py
    输入文件名
    脚本执行结束后会在 /opt/projects/{your new project name}有新的项目
