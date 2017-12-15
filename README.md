这样就相当于一个大工程结构：

1）最上层flask_blog目录是项目名称，一个项目下可以包括多个模块，也就是应用，每个应用下有自己的配置文件，初始化文件，MVC架构。

2）runserver.py：与应用模块平级，作为项目启动文件

3）第二级blog2目录：模块名称

       controller目录：MVC中的C,主要存放视图函数

       model目录：MVC中的M,主要存放实体类文件，映射数据库中表

       templates：MVC中的V，存放html文件

       static：静态文件，主要存放css，js等文件

       __init__.py:模块初始化文件，Flask 程序对象的创建必须在 __init__.py 文件里完成， 然后我们就可以安全的导入引用每个包。

       setting.py:配置文件，数据库用户名密码等等
