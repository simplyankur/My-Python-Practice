from flask import Flask, render_template, url_for
from forms import RegistrationFrom, LoginFrom

app = Flask(__name__)
app.config['SECRET_KEY'] = '0d2170837e3f20e4b2285a1c24afe526'

posts = [
    {
        'author': 'Mahatma Gandhi',
        'date_posted': '10-8-1987',
        'title': 'I proud to be an Indian',
        'content': 'Hello India Welcome to my blog post'
    },
    {
        'author': 'Pt. Jawaharlal Nehru',
        'date_posted': '16-8-1975',
        'title': 'Indian Democracy',
        'content': 'Hello India Welcome to my blog post'
    }
]


@app.route('/')
@app.route('/home')
def home():
    return render_template("home.html", posts=posts)


@app.route('/about')
def about():
    return render_template("about.html", title="About Us")


@app.route('/register')
def register():
    form = RegistrationFrom()
    return render_template('register.html', title="Form Registration", form=form)


@app.route('/login')
def login():
    login_form = LoginFrom()
    return render_template('login.html', title="Login", login_form=login_form)


if __name__ == '__main__':
    app.run(debug=True)
