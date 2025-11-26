from flask import Flask,render_template,request

app = Flask(__name__)

@app.route("/",methods=["GET","POST"])
def index():
    return(render_template("index.html"))

@app.route("/main",methods=["GET","POST"])
def main():
    q=request.form.get("q")
    print(q)
    return render_template("main.html",query="q")

@app.route("/paynow",methods=["GET","POST"])
def paynow():
    return render_template("paynow.html",query="q")

if __name__=="__main__":
    app.run()
