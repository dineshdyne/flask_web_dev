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
    fruits = ['apple', 'orange', 'banana', 'grape']
    return render_template('index.html', val=fruits)


# @app.route("/")
# def index_2():  # view function
#     """contains the response to the request you app
#     receives.the func is given a name which is used
#     to generate URLs for that particular func"""
#     return "<h1>Hello World! No Welcome<h1>"

# Dynamic Routes

@app.route("/usr/<nameskgudf>")  # same name input
def user(nameskgudf):  # view function
    # jinja2 template
    return render_template('user_name.html', name=nameskgudf)


@app.route("/no_block")  # same name input
def index_with_no_block():  # view function
    # jinja2 template
    fruits = ['apple', 'orange', 'banana', 'grape']
    return render_template('no_block_index.html', val=fruits)


@app.route("/base")  # same name input
def base():  # view function
    # jinja2 template
    fruits = ['apple', 'orange', 'banana', 'grape']
    return render_template('base.html')
