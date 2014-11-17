django-scaffold
===

django-scaffold是一个快速初始化django项目的脚手架。

当你新写django项目的时候很多东西都是重复的:

    0. virtualenv nginx 等必要安装
    1. supervisor gunicorn nginx配置
    2. django settings里面必须的配置，log, mako, memcached等等
    3. 常用库(必用库)的安装, 或者说必用功能的安装，例如静态文件加hash码，用mako增强template等等

说好的DRY呢？

这个项目就是为了让你可以clone之后，简单的运行几个脚本就可以完成这些繁琐的配置，直接进到需求中去。

目前django版本采用1.4.8,不过脚手架里面可以比较方便的切到1.6.1(无缝的样子)，个人用暂时没问题，有问题请提issue.

脚手架提供了这些东西:

dev master两个环境:
    dev平时开发可以直接用，master是指生产可用的一些配置, 当然你可以用master做开发.
    dev采用django manager runserser, DEBUG=True的开发环境
    master采用supervisor, gunicorn, nginx, DEBUG=False

一些有用的脚本(两个环境分开)：
    包括项目的重命名，依赖库安装脚本，运行端口重置，启停项目脚本等等

一些约定
---
如果想要方便的使用这个项目，有些约定是需要遵守的

1. linux or unix
2. 在你个人项目下建立projects文件夹，相对于/opt建立软连接 `cd ~ && mkdir projects && cd projects && sudo ln -s $(pwd)/projects /opt`
3. 将项目克隆到`/opt/projects`下
4. 脚本使用顺序: 第一步,你需要重命名clone回来的项目，用这个脚本`rename_and_backup.py`;第二步,
你需要配置项目运行时的端口号`reset_port.py`;第三步，安装各种依赖`install.sh`(这个脚本执行一次即可);
第四步，配置nginx`config_dev_nginx.sh`和`config_dev_nginx.sh`,第五步, 运行项目`run_dev.sh` 和`run_master.sh`.其中你可以看到有dev, master两个版本, dev采用django 默认的runserver来做，并且配置文件中DEBUG=True,master版本采用supervisor, gunicorn来做python容器，静态文件有nginx代理

文件结构
---
 $ tree -L 1
.
├── app
├── deploy
├── django-scaffold
├── LICENSE
├── manage.py
├── README.md
├── requirements.txt
├── static_dev
├── statics
├── templates
└── tools

django-scaffold 项目名，下面放基本的settings配置
templates html模板丢在这里
static_dev 开发是静态文件放这里(css/js等)
statics collectstatic最终的目标路径 nginx查找的目录
deploy部署相关的配置
tools各种有用的脚本
requirements pip依赖
app 就是普通的模块
/var/log/django-scaffold下有各种log
/run/下有gunicorn supervisor的pid

为什么django用1.4.8?
---
1. 因为足够.
2. django不是因为django的本版更高而更牛逼(超多的三方库让django牛逼).
3. 有些库在我用的时候还是支持稳定的1.4.8的(没错，oauth)
4. 1.4.8的基本配置，文件结构和1.6一样

脚手架目前提供了什么
---
1. mako支持
2. 静态文件collect后添加hash
3. supervisor, gunicorn, nginx部署配置
4. rename脚本，可以直接将django-scaffold改为你想要的名字
5. reset_port脚本，可以将gunicorn, nginx, supervisor中django运行的端口改为你期望的端口号
6. install脚本，一键安装依赖
7. config_nginx脚本，当你修改代码的nginx配置时,执行此脚本可以更新nginx
8. run脚本，分为可以简化django启停命令，分为dev和master两种环境

将来提供什么 TODO List
---
. xadmin或者xadmin2
. python-oauth的一个fork版本，添加weibo, weixin等中国backend
. 传文件
. 切图片
. 分页
. 最新的requirements.txt
. rest service
. 权限的一些东西
. 正式上线修改nginx域名的脚本
. 单元测试时的sqlite数据库

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

reset_port.py
---
端口重置脚本，因为一台机器上django的端口可能之前就被占用了, port.json显示了此项目使用的端口(不要修改这个json文件)

install.sh
---
安装pip
配置豆瓣源
建立virtualenv
安装requirements
建立log文件夹

config_dev_nginx
---
将dev版本的nginx丢到nginx配置环境，并且reload nginx

config_master_nginx
---
将master版本的nginx丢到nginx配置环境，并且reload nginx

run_dev.sh
---
使用django manage.py runserver 的方式运行测试环境，采用settings-dev.py这个配置文件

run_master.sh
---
supervisor, gunicorn, nginx的方式运行正式环境

log
---
dev log: `tail -f /var/log/django-scaffold/dev-stdout.log`
master log: `tail-f /var/log/django-scaffold/stderr.log`
nginx access log: `tail -f /var/log/django-scaffold/ngaccess.log`
nginx error log: `tail -f /var/log/django-scaffold/ngerror.log`
