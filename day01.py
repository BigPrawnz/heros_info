from flask import Flask
from flask import url_for
app = Flask(__name__)

@app.route("/ass")
def hello():
	return 'This is my first demo!<img src="https://comaker.cn/img/7c615ad2acda0686faf71100d8580591">'
@app.route("/user/<name>")
def user_page(name):
	return "user name is {}".format(name)
@app.route("/test")
def test_url_for():
	# 下面是一些调用示例：
    print(url_for('hello'))  # 输出：/
    # 注意下面两个调用是如何生成包含 URL 变量的 URL 的
    print(url_for('user_page', name='greyli'))  # 输出：/user/greyli
    print(url_for('user_page', name='peter'))  # 输出：/user/peter
    print(url_for('test_url_for'))  # 输出：/test
    # 下面这个调用传入了多余的关键字参数，它们会被作为查询字符串附加到 URL 后面。
    print(url_for('test_url_for', num=2))  # 输出：/test?num=2
    return 'Test page'
if __name__ == '__main__':
    app.run(debug=True)