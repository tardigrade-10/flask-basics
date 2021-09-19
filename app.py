# flask run --host=0.0.0.0

from flask import Flask
from flask import url_for
from flask import request
from flask import render_template

app = Flask(__name__)
# app.config['/Uploaded files']
#REQUEST OBJECT and UPLOAD FILES

@app.route('/')
def customer():
    return render_template('cust.html')

@app.route('/success', methods = ['POST', 'GET'])
def print_data():
    if request.method == 'POST':
        result = request.form
        f = request.files['file']
        f.save(f.filename)
        return render_template("result_data.html", result = result, name = f.filename)












