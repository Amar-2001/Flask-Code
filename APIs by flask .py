from flask import Flask
from flask import request # to take input

app = Flask(__name__)

@app.route("/")
def func1():
    a=8/5
    return "<h1> This is a function 1 {} </h1>".format(a)

@app.route("/amar") # proof ho gaya ki yaha kuch bhi naame rakh sakte jaruri 
                    # nahi ki function ka hi name rakho
def func2():
    return "<h2>This is a function 2</h2>"

# to take Input

@app.route("/Masooma")
def func3():
    amar=request.args.get("a")
    return "<h1>This is function 3 Masooma is   {}</h1>".format(amar)


if __name__=="__main__":
    app.run(host="0.0.0.0")

