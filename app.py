from flask import Flask, render_template
app=Flask(__name__)

@app.route('/')
def home():
    return "<h3>welcome to my cloud Computing</h3>"

@app.route('/reg')
def registration():
    return "<h3>welcome to registration page</h3>"

@app.route('/sales')
def sales():
    return "<h3>welcome to home page</h3>"

@app.route("/multiply")
def multiply ():
    a = 14
    b = 15
    c = 20
    d= a*b*c
    return render_template("multiply.html", multiply_result=d)

@app.route('/division')
def division():
    a=89
    b=69
    c=a/b
    return "this is the division result " + str(c)

@app.route('/addition')
def addition():
    a=89
    b=69
    c=a+b
    return "this is the addition result " + str(c)


@app.route('/sub')
def sub():
    a=289
    b=201
    c=a-b
    return "The subtraction result is " + str(c)



@app.route('/contact')
def contact():
    email="uju@yahoo.com"
    phone="7748848498949"
    return "this is our contact info or details " + email + "," + phone 


@app.route('/homepage')
def homepage():
    name="Mrs Christabel"
    email="peju@yahoo.com"
    collect="Details are:" +str(email) +str(name)
    return render_template('homepage.html', collect=collect)


@app.route("/maths")
def maths ():
    a = 5
    b = 10
    c = a+b
    return render_template("maths.html", maths_result=c)















if __name__=="__main__":
    app.run(debug=True, port=5003,host="0.0.0.0")