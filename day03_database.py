from flask_sqlalchemy  import SQLAlchemy
import os,sys
from flask import Flask

WIN = sys.platform.startswith('win')
if WIN:  # 如果是 Windows 系统，使用三个斜线
    prefix = 'sqlite:///'
else:  # 否则使用四个斜线
    prefix = 'sqlite:////'

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = prefix + os.path.join(app.root_path, 'data.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # 关闭对模型修改的监控
db = SQLAlchemy(app)
class User(db.Model):  # 表名将会是 user（自动生成，小写处理）
    id = db.Column(db.Integer, primary_key=True)  # 主键
    name = db.Column(db.String(20))  # 名字


class hero_info(db.Model):  
    id = db.Column(db.Integer, primary_key=True)  # 主键
    name = db.Column(db.String(10))  
    title = db.Column(db.String(10))  




if __name__ == '__main__':
    app.run(debug=True)
