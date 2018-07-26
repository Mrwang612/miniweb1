""" 自定义的协议
按照事先约定好的协议实现双方的通信(web服务器与框架应用程序)
- web服务器把请求报文信息以字典形式传递给框架应用程序对接的函数
    env={"PATH_INFO":"/index.html"}
- 在框架应用程序把处理的结果以返回值的形式返回给web服务器
    return '200 OK',[('Content-Type','text/html')],'response body'
"""
import re
import time


def index():
    """处理首页/index.html动态请求"""
    """
    实现步骤：
        1. 访问数据库，获取动态数据
        2. 读取模板文件
        3. 通过正则表达式，把动态数据替换到模板页面中，形成一个新的动态页面
        4. 返回新的动态页面内容(响应体)
    """
    # 1. 访问数据库，获取动态数据
    data_from_mysql="首页数据来自数据库"

    # 2. 读取模板文件
    with open("./templates/index.html") as f:
        content=f.read()

    # 3.通过正则表达式，把动态数据替换到模板页面中，形成一个新的动态页面
    content=re.sub(r"{%content%}",data_from_mysql,content)

    # 4. 返回新的动态页面内容(响应体)
    return content

def center():
    """处理首页/center.html动态请求"""
    """
        实现步骤：
            1. 访问数据库，获取动态数据
            2. 读取模板文件
            3. 通过正则表达式，把动态数据替换到模板页面中，形成一个新的动态页面
            4. 返回新的动态页面内容(响应体)
        """
    # 1. 访问数据库，获取动态数据
    data_from_mysql = "个人中心数据来自数据库"

    # 2. 读取模板文件
    with open("./templates/center.html") as f:
        content = f.read()

    # 3.通过正则表达式，把动态数据替换到模板页面中，形成一个新的动态页面
    # 使用替换后的结果
    content = re.sub(r"{%content%}", data_from_mysql, content)

    # 4. 返回新的动态页面内容(响应体)
    return content

def gettime():
    """处理首页/gettime.html动态请求"""
    # 返回的是响应体
    return time.ctime()


def error_page():
    """返回错误页面"""
    return "<a href='http://www.douyu.com/directory/game/yz'><img src='/images/404.jpg'/></a>"


def app(env):
    """与web服务器对接的函数
    :param: env :字典类型，封装了请求报文信息 ,PATH_INFO:表示请求路径
    :return :'200 OK',[('Content-Type','text/html')],'response body'
    """
    # 1. 解析字典， 获取请求信息
    request_url=env["PATH_INFO"]
    print("请求路径: ",request_url)

    # 2. 业务处理,完成动态页面

    # 3. 依据不同的请求，返回不同的内容
    # /index.html
    if request_url=="/index.html":
        # 4. 返回数据: '200 OK',[('Content-Type','text/html')],'response body'
        # return  状态码　　响应头　　　响应体　
        return '200 OK', [('Content-Type', 'text/html;charset=utf-8')], index()
    elif request_url=="/center.html":
        return '200 OK', [('Content-Type', 'text/html;charset=utf-8')], center()
    elif request_url=="/gettime.html":
        return '200 OK', [('Content-Type', 'text/html;charset=utf-8')], gettime()
    else:
        """不合法请求，返回错误页面"""
        return '404 Not Found', [('Content-Type', 'text/html;charset=utf-8')], error_page()

