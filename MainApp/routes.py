from MainApp import app, db, api, sqlData
from flask import render_template, redirect, url_for, flash, session, request, send_from_directory, jsonify, send_file
from flask_restful import Api, Resource, reqparse
from MainApp.models import User
from MainApp.forms import RegisterForm, LoginForm
from flask_login import login_user, logout_user, login_required
import sqlalchemy as sa
from sqlalchemy.ext.declarative import declarative_base

engine = sa.create_engine('sqlite:///users.db', echo=True)
metadata_obj = db.MetaData()
Base = declarative_base()


@app.route('/', methods=['GET', 'POST'])
@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        attempted_user = User.query.filter_by(username=form.username.data).first()
        if attempted_user and attempted_user.check_password_correction(attemp_password=form.password.data):
            session.permanent = True
            login_user(attempted_user)
            session['user'] = form.username.data
            flash("Zostałaś/eś zalogowana/y do aplikacji", category='success')
            return redirect(url_for('main_page'))
        else:
            flash("Użytkownik i/lub hasło nie są poprawne", category='danger')
    return render_template('index.html', form=form)


@app.route('/register', methods=['GET', 'POST'])
def create_user_account():
    form = RegisterForm()
    if form.validate_on_submit():
        user_to_create = User(username=form.username.data,
                              email_address=form.email_address.data,
                              password=form.password1.data
                              )
        db.session.add(user_to_create)
        db.session.commit()
        return redirect(url_for('login'))
    if form.errors != {}:
        for err_Msg in form.errors.values():
            flash(f"Podczas tworzenia użytkownika pojawił się błąd: {err_Msg}", category='danger')
    return render_template('register.html', form=form)


@app.route('/mainpagevisit', methods=['GET', 'POST'])
def main_page():

    # profile = db.Table(
    #     'profile',
    #     metadata_obj,
    #     db.Column('email', db.String, primary_key=True),
    #     db.Column('name', db.String),
    #     db.Column('contact', db.Integer),
    # )
    #
    # # Create the profile table
    # metadata_obj.create_all(engine)
    #
    # ins = profile.insert().values(email='asd@asd.pl', name='kozidrak', contact='12221')
    # engine.conn

    return '<p>siemano kolano</p>'

# znowu pierwsze kroki z Api


data_put_args = reqparse.RequestParser()
data_put_args.add_argument("url", type=str)
data_put_args.add_argument("username", type=str)
data_put_args.add_argument("password", type=str)
data_put_args.add_argument("fu", type=str)
data_put_args.add_argument("lu", type=str)

testData = reqparse.RequestParser()
testData.add_argument("name", type=str)
testData.add_argument("value", type=str)

my_data = {}


class HelloWorld(Resource):
    def put(self, ip):
        print("jestem tu")
        print(ip)
        args = data_put_args.parse_args()
        print(args)
        print(f"To są nasze dane po kolei: \n"
              f"{args['url']} \n"
              f"{args['username']} \n"
              f"{args['password']} \n"
              f"{args['fu']} \n"
              f"{args['lu']}")
        sqlData.shickPhick(ip, args['url'], args['username'], args['password'], args['fu'], args['lu'])
        return ip


api.add_resource(HelloWorld, "/hello/<string:ip>")
