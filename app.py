from swiggy_app import app,db
from swiggy_app import models
from swiggy_app import views

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)




    #hello this is swiggy application
