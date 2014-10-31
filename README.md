用django-pipeline增强为静态文件添加hash
===

安装
---
    sudo mkdir /opt/projects
    git clone https://github.com/duoduo369/django_pipeline_demo.git
    cd django_pipeline_demo
    ln -s $(pwd) /opt/projects
    ln -s /opt/projects/django_pipeline_demo/deploy/nginx/django_pipeline.conf /etc/nginx/sites-enabled
    pip install -r requirements.txt
    python manage.py runserver 0.0.0.0:9888
    nginx -s reload
    vim /etc/hosts 添加 127.0.0.1:9888 django_pipline_demo.com

为什么需要hash静态文件？
---

请看[大公司里怎样开发和部署前端代码？](http://www.zhihu.com/question/20790576) 张云龙的答案


django的库pipeline
---

[mako](http://www.makotemplates.org/),  [django-mako](https://github.com/jurgns/django-mako),  [demo](https://github.com/duoduo369/django_pipeline_demo)

效果是这样的,以 [django_pipeline_demo](https://github.com/duoduo369/django_pipeline_demo) 为例。

先说最终用法
---

1. debug必须为False(上线本来就是False),如果为True则使用django默认查找静态文件的方式,不会使用pipeline。
2. `python manage.py collectstatic`
3. 重启django项目

