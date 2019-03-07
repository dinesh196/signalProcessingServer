from flask import Flask, render_template
from .signal import DNN 

app = Flask(__name__, static_folder="../static/dist", template_folder="../static")
from abc import model

inst = DNN()

@app.route("/", methods=['POST'])
def index():
    # return render_template("index.html")
    #return render_template("../static/index.html")\
    a = form.get["a"]
    result = inst.predict(a)
    return result

""" @app.route("/")
    return  """
""" 
@app.route("/hello")
def hello():
    return 'Hello Dinesh'
 """
if __name__ == "__main__":
    app.run()