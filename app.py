from flask import Flask
from flask import request

app = Flask(__name__) # (__name__)dunder ban gaya Flask ke andar aur ek variable
                        # ya object (app)mein store ho gaya means jo bhi Flask mein 
                        # hai wo sab app name ke variable ya object mein hai Ok

@app.route("/") # app jo ki ek variable / object hai jo Flask ke sare operations ko kar sakta
#        app ko hum decorator ke bana diye aur us se hum decorate karenge
        #  "/" diye jo ki client  server architecture  ko bata raha 
        #  "/" client agar server ke paas aayega toh wo route karega aur functions ko
        #   access karega through route and isliye "/ hai " iske jagah kuch naam bhi de sake
        #  .py mein jo likha hai wo server side ka code hai aur server kaun banyega :-
         # Flask mein likha code 
        # aur client jitne bhi function likhe hai usko access kar payega 


def hello_world():   #ek function banaya
    return "<h2>Hello, Dudhanshu sir</h2>"  # return kara diye hello world in <H1> as you write <h1> in html


@app.route("/hello_world1")
def hello_world1():   #ek function banaya
    return "<h2>Hello, Sudhanshu sir</h2>"  # return kara diye hello world in <H1> as you write <h1> in html

@app.route("/test")
def test():
    # print("This is my function to test for APIs")
    # TypeError: The view function for 'test' did not return a valid response. 
    # The function either returned None or ended without a return statement
    a=4+5
    return "<h2>This is my function to test for APIs {} </h2> ".format(a)


# To take INput first request.args.get('x')le lo aur import kar lo request ko upar
# import request and 
# run karte waqt jaise google mein hota hai waise :- https://red-librarian-ylqqo.pwskills.app:5000/test2?x=Amar
# means https://red-librarian-ylqqo.pwskills.app:5000/test2?x=Amar
#  sirf last mein ?x=jo bhi likhna chate

@app.route("/test2")
def test2():
    data=request.args.get("x") # request kar raha argument ko aur get kar raha (x) ko 
                             # aur usko variable  data mein rakh raha
    return "This is a data input from my URL {} ".format(data)

@app.route("/hello_world12")
def hello_world2():   #ek function banaya
    return "<h2>Hello, Sudhanshu sir</h2>"  # return kara diye hello world in <H1> as you write <h1> in html




if __name__=="__main__": # kya dunder name main function mein hai 
    app.run(host="0.0.0.0") # agar ha toh run kara do aur uska ip address hai 0.0.0.0

# **************************************************
    # output :-[31m[1mWARNING: This is a development server.
    #  Do not use it in a production deployment. Use a production WSGI server 
    # instead.[0m
#  * Running on all addresses (0.0.0.0)
#  * Running on http://127.0.0.1:5000
#  * Running on http://172.18.0.17:5000
# ***********************************************************



# Flask ek python ki library hai jo help karta hai UPI create karne mein 
# isme hum function banate aur usse acccess karte but not through python but from the 
# outer world by the websites just like google does 


# yaha neeche jo  code hai wo code jaha likhe hai uska url copy karo app tak 
# aur last mein: 5000 add karo like https://red-librarian-ylqqo.pwskills.app:5000/ 
# You can also see it from the mobile

# means humara goal achieve ho gaya  
# jo tha ki kisi dusre device se communicate kar paana ya same code ko run kar paana 
# in a different system 

# this is an example of  heterogeneous APIs
# because yaha data hum dusre device or dusre browser se le rahe output aur 
# aur jo different platform use karta ho like website use karta html,css ,js but
# we write code in python

# ye hai client server architecture ka example
# aur ye sab only 2 function ki help se hua @app.route("/") aur app.run(host="0.0.0.0")
                                                     


# Here in output 200 means successfull or 404 means page not found

# Hum yaha 
# https://red-librarian-ylqqo.pwskills.app:5000/test2?x=World%27s%20richest%20man%20Amar
# ye jo link hai wo protocol hai jo APIs hai
# iske madat se hum APIs se connect ho sakte kisi bhi system mein kisi bhi browser mein
# kisi bhi  programming language dwara issey call kar sakte no matter Apis ka code python
# mein hai but usse java se call kar sakte ya koi bhi any other programming languge se
# So thank You Guys Have a nice learning journey
# Try More questions on these