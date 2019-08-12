from app import app, db
from flask import render_template, request, redirect, url_for, flash
from forms import UserForm, AccountForm
from models import User, Account


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/about/')
def about():
    '''Made this page about me'''
    return render_template('about.html', name="Daniel Ragbeer")


@app.route('/users')
def show_users():
    '''Displays all users in database. Must refresh this page to get most updated
       users.'''
    return render_template('show_users.html', users = User.query.all()) #displays data from database

@app.route('/accounts')
def show_accounts():
    '''Displays all accounts created. NOT USERS! You will be able to see all
       first names, last names and nicknames.'''
    return render_template('show_accounts.html', accounts = Account.query.all())
    #displays data from database. show_accounts.html was an html file created to display account form data from database.


@app.route('/add-user', methods=['POST', 'GET'])
def add_user():
    user_form = UserForm()

    if request.method == 'POST':
        if user_form.validate_on_submit():
            user = User(request.form['name'], request.form['email']) #makes it 1 value instead of 2
            db.session.add(user)
            db.session.commit() #must commit changes

            flash('User successfully added')
            return redirect(url_for('show_users'))

    flash_errors(user_form)
    return render_template('add_user.html', form=user_form)

@app.route('/add-account-info', methods = ['POST', 'GET'])
def add_account_info():
    '''this function handles the first name, last name, nickname and email capturing'''

    account_form = AccountForm()

    if request.method == 'POST':
        if account_form.validate_on_submit():
            account = Account(request.form['first_name'], request.form['last_name'],
                              request.form['nickname'], request.form['email'])
                              #request.form collects the values in a form with method "post"

            db.session.add(account) #adds account information to database
            db.session.commit()

            flash('Account successfully created')
            return redirect(url_for('show_accounts'))

    flash_errors(account_form)
    return render_template('add_account_info.html', form = account_form)
    #add_account_info.html is the html file created to submit the account form information



def flash_errors(form):
    for field, errors in form.errors.items():
        for error in errors:
            flash(u"Error in the %s field - %s" % (
                getattr(form, field).label.text,
                error
            ))


@app.route('/<file_name>.txt')
def send_text_file(file_name):

    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):

    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=600'
    return response


@app.errorhandler(404)
def page_not_found(error):

    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port="8080")
