from flask import Flask, render_template  # import library and class Flask

# Creation of instance of Flask
# "__name__" -> name of module or package that contain the application
app = Flask(__name__)

# every flask application requires a route and
# corresponding view function that will respond
# to request made to the route


@app.route("/")
def index():  # view function
    """contains the response to the request you app
    receives.the func is given a name which is used
    to generate URLs for that particular func"""
    return render_template('index.html')


# @app.route("/")
# def index_2():  # view function
#     """contains the response to the request you app
#     receives.the func is given a name which is used
#     to generate URLs for that particular func"""
#     return "<h1>Hello World! No Welcome<h1>"

# Dynamic Routes

@app.route("/usr/<nameskgudf>")  # same name input
def user(nameskgudf):  # view function
    return render_template('user.html', name=nameskgudf)  # jinja2 template
