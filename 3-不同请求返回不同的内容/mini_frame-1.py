""" 自定义的协议
按照事先约定好的协议实现双方的通信(web服务器与框架应用程序)
- web服务器把请求报文信息以字典形式传递给框架应用程序对接的函数
    env={"PATH_INFO":"/index.html"}
- 在框架应用程序把处理的结果以返回值的形式返回给web服务器
    return '200 OK',[('Content-Type','text/html')],'response body'
"""
import time


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
        return '200 OK', [('Content-Type', 'text/html;charset=utf-8')], 'response body 响应体' + "首页内容..."
    elif request_url=="/center.html":
        return '200 OK', [('Content-Type', 'text/html;charset=utf-8')], 'response body 响应体' + "个人中心内容..."
    elif request_url=="/gettime.html":
        return '200 OK', [('Content-Type', 'text/html;charset=utf-8')], 'response body 响应体' + time.ctime()
    else:
        """不合法请求，返回错误页面"""
        return '404 Not Found', [('Content-Type', 'text/html;charset=utf-8')], '错误页面'

