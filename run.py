from flask_app import create_app

app_= create_app()

if __name__ == '__main__':
    with app_.app_context():
        app_.run(debug=True)



#    DB CONTEXT
    #with app.app_context():
        #db.create_all()
        #user = User(username="testuserr", email="testtt@example.com", password="password")
        #db.session.add(user)
        #db.session.commit()
        #db.drop_all()


