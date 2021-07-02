from flask import Flask, render_template

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///abb.db'


@app.route('/')
@app.route('/home')
def home_page():
    return render_template('home.html')


@app.route('/workspace')
def workspace_page():
    return render_template('workspace.html')


@app.route('/workspace/image')
def ws_image_page():
    return render_template('image.html')


@app.route('/workspace/positions')
def ws_positions_page():
    return render_template('positions.html')


@app.route('/workspace/parameters')
def ws_parameters_page():
    return render_template('parameters.html')


@app.route('/workspace/tool')
def ws_tool_page():
    return render_template('tool.html')


@app.route('/workspace/grip')
def ws_grip_page():
    return render_template('grip.html')


@app.route('/workspace/supervision')
def ws_supervision_page():
    return render_template('supervision.html')


@app.route('/workspace/mechanics')
def ws_mechanics_page():
    return render_template('mechanics.html')


@app.route('/workspace/test&save')
def ws_test_save_page():
    return render_template('test_save.html')


@app.route('/about')
def about_page():
    return render_template('about.html')


@app.route('/login')
def login_page():
    return render_template('login.html')


@app.route('/register')
def register_page():
    return render_template('register.html')


if __name__ == '__main__':
    app.run(debug=True)
