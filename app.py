




#app.secret_key = 'MySecretKey$%&'
#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@127.0.0.1:8889/bank2'
#app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


# Change this to your secret key (can be anything, it's for extra protection)
#app.secret_key = 'MySecretKey$%&'


#@app.route('/')
#def hello_world():
#    return 'Hello'
#    if 'loggedin' in session:
#        return redirect(url_for('home.home', surname=session['surname']))
#    else:
#        return redirect(url_for('auth.login'))

'''@app.route('/')
def testdb():
    try:
        db.session.query("1").from_statement("SELECT 1").all()
        return '<h1>It works.</h1>'
    except:
        return '<h1>Something is broken.</h1>'''



#if __name__ == '__main__':
#    app.run(debug=True)
