from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import Length, EqualTo, Email, DataRequired, ValidationError
from MainApp.models import User


class RegisterForm(FlaskForm):

    def validate_username(self, username_to_check):
        user = User.query.filter_by(username=username_to_check.data).first()
        if user:
            raise ValidationError('Nazwa użytkownika już istnieje')

    def validate_email_address(self, email_address_to_check):
        email_validate = User.query.filter_by(email_address=email_address_to_check.data).first()
        if email_validate:
            raise ValidationError("Adres email już istnieje")

    username = StringField(label='Nazwa Użytkownika', validators=[Length(min=2, max=30), DataRequired()])
    email_address = StringField(label='Adres Email', validators=[Email(), DataRequired()])
    password1 = PasswordField(label='Hasło', validators=[Length(min=4), DataRequired()])
    password2 = PasswordField(label='Powtórz hasło:', validators=[EqualTo('password1'), DataRequired()])
    submit = SubmitField(label='Zarejestruj')


class LoginForm(FlaskForm):
    username = StringField(label="Nazwa użytkownika", validators=[DataRequired()])
    password = PasswordField(label="Hasło", validators=[DataRequired()])
    submit = SubmitField(label="Zaloguj")
