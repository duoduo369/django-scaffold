用mako增强django模板
===

django默认的模板功能还可以，但是不能直接用python的语法，mako解决了这个痛点，
使得django的模板变得像jsp一样，可以直接使用python的语法做一些事情。

[mako](http://www.makotemplates.org/)
[django-mako](https://github.com/jurgns/django-mako)
[demo](https://github.com/duoduo369/djangomako_demo)

mako基本用法
---

### mako的模板需要这样子搞

1. 直接的类似python string format的样子

    from mako.template import Template
    mytemplate = Template("hello, ${name}!")
    print mytemplate.render(name="jack")

2. 用文件

    from mako.template import Template


    mytemplate = Template(filename='/docs/mytmpl.txt', module_directory='/tmp/mako_modules')
    print mytemplate.render()

3. 当template里面需要继承或者超找其他模板文件的时候,需要TemplateLookup

    from mako.template import Template
    from mako.lookup import TemplateLookup

    mylookup = TemplateLookup(directories=['/docs'])
    mytemplate = Template("""<%include file="header.txt"/> hello world!""",
    lookup=mylookup)

感觉很复杂的样子，django-mako的出现将这些繁琐的东西降至0，使django依然可以使用render_to_response

### 用django-mako后

一个简单的view

    from djangomako.shortcuts import render_to_response

    def index(request):
        return render_to_response('index.html', {})

index.html

    <%! import os %>

    <%
        rows = [[v for v in range(0,10)] for row in range(0,10)]
    %>

    <%def name="makerow(row)">
        <tr>
        % for name in row:
            <td>${name}</td>\
        % endfor
        </tr>
    </%def>

    <html>
      <body>
        ${os.path.sep}
        <table>
            % for row in rows:
                ${makerow(row)}
            % endfor
        </table>
      </body>
    </html>


之所以能这样调用都是因为django-mako有这么一个中间件，在settings.py中加入这个中间件就可以轻松的使用mako的语法了

    from mako.lookup import TemplateLookup
    import tempfile

    class MakoMiddleware(object):
        def __init__(self):
            """Setup mako variables and lookup object"""
            from django.conf import settings
            # Set all mako variables based on django settings
            global template_dirs, output_encoding, module_directory, encoding_errors
            directories      = getattr(settings, 'MAKO_TEMPLATE_DIRS', settings.TEMPLATE_DIRS)
            module_directory = getattr(settings, 'MAKO_MODULE_DIR', tempfile.mkdtemp())
            output_encoding  = getattr(settings, 'MAKO_OUTPUT_ENCODING', 'utf-8')
            encoding_errors  = getattr(settings, 'MAKO_ENCODING_ERRORS', 'replace')

            global lookup
            lookup = TemplateLookup(directories=directories,.
                                    module_directory=module_directory,
                                    output_encoding=output_encoding,.
                                    encoding_errors=encoding_errors,
                                    )
            import djangomako
            djangomako.lookup = lookup

mako的语法
---
[文档](http://docs.makotemplates.org/en/latest/syntax.html)

* 注释

    <%doc>
        these are comments
        more comments
    </%doc>

* 表达式

    ${表达式}: ${2*3} --> 6
    ${pow(x,2) + pow(y,2)}

* 控制

    % for a in ['one', 'two', 'three', 'four', 'five']:
        % if a[0] == 't':
        its two or three
        % elif a[0] == 'f':
        four/five
        % else:
        one
        % endif
    % endfor

* 代码块

    <%! %>与<% %>是不一样的，<%!  %>只会载入一次，因此像定义方法，import东西的时候写在这里面
    <%!
        import mylib
        import re

        def filter(text):
            return re.sub(r'^@', '', text)
    %>
    <%
        x = db.get_resource('foo')
        y = [z.element for z in x if x.frobnizzle==5]
    %>
