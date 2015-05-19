# @app.route("/hello")
# def say_hi():
#     return "Hello World!"
    
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/hello/<name>")
def say_hi(name):
    return render_template('base.html', my_string="Hello {}!".format(name.title()))

# @app.route("/hello/<name>")
# def hi_person(name):
#     return "Hello {}!".format(name.title())

# @app.route("/hello/<name>")
# def hello_person(name):
#     html = """
#         <h1>
#             Hello {}!
#         </h1>
#         <p>
#             Here's a picture of a kitten.  Awww...
#         </p>
#         <img src="http://placekitten.com/g/200/300">
#     """
#     return html.format(name.title())

if __name__=="__main__":
    app.run(host="0.0.0.0", port=8080)