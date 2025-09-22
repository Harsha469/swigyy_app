from datetime import datetime
from swiggy_app import db 

class UsersTable(db.Model):
    id = db.Column(db.Integer,primary_key= True,nullable= False)
    name = db.Column(db.String(50), unique = True, nullable = False)
    password = db.Column(db.String(200), nullable = False)
    created_at = db.Column(db.DateTime,default = datetime.utcnow)
    updated_at = db.Column(db.DateTime, default = datetime.utcnow , onupdate=datetime.utcnow)

