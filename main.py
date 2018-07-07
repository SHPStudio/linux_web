#coding=utf-8
from flask import Flask,render_template,jsonify,request
from flask_cors import CORS
import os,linux,json,common
app = Flask(__name__)
CORS(app)

UPLOAD_FOLDER = 'upload'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER  # 设置文件上传的目标文件夹
basedir = os.path.abspath(os.path.dirname(__file__))  # 获取当前项目的绝对路径

ALLOWED_EXTENSIONS = set(['war','zip','jpg','png','gif','jpeg'])  # 允许上传的文件后缀


# 判断文件是否合法
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template("index_prod.html")

@app.route('/upload', methods=['POST'], strict_slashes=False)
def upload():
    file_dir = os.path.join(basedir, app.config['UPLOAD_FOLDER'])  # 拼接成合法文件夹地址
    if not os.path.exists(file_dir):
        os.makedirs(file_dir)  # 文件夹不存在就创建
    f = request.files['myfile']  # 从表单的file字段获取文件，myfile为该表单的name值
    if f and allowed_file(f.filename):  # 判断是否是允许上传的文件类型
        fname = f.filename
        f.save(os.path.join(file_dir, fname))  # 保存文件到upload目录
        return jsonify({"success": True, "message": "上传成功"})
    else:
        return jsonify({"success": False , "message": "上传失败"})

@app.route('/startWar',methods=['POST'])
def startWar():
    data = request.data
    print data
    j_data = json.loads(data)
    docker_deploy = linux.DockerDeploy(fileName=j_data['fileName'],appName=j_data['appName'],appTargetPath=j_data["appTargetPath"])
    result = linux.runWar(docker_deploy)
    return jsonify(result)

if __name__ == '__main__':
    common._init()
    common.set_value("baseDir", basedir)
    common.set_value("uploadDir", os.path.join(basedir,UPLOAD_FOLDER))
    app.run(debug=True,host='0.0.0.0', port=5000)