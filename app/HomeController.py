from flask import render_template, Blueprint

home = Blueprint("home", __name__,
                 static_folder='../static',
                 static_url_path='/content')


@home.route('/', methods=['GET'])
def index():
    return render_template('home/index.html')
