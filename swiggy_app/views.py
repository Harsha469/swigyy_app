from swiggy_app import app,db,api
from flask_restful import Resource,marshal_with,fields,reqparse
from swiggy_app.models import UsersTable
from flask import jsonify
from werkzeug.security import generate_password_hash,check_password_hash
from flask_jwt_extended import create_access_token,jwt_required,get_jwt_identity
from datetime import timedelta

@app.route('/')
def home():
    return 'this is home page'

user_fields = {
    'name':fields.String,
}

parser = reqparse.RequestParser()
parser.add_argument('name',type = str,required = True, help= 'name cannot be blank')
parser.add_argument('password', type= str, required = True, help = 'password cannot be empty')



class Users(Resource):

    @marshal_with(user_fields)
    def get(self):
        users = UsersTable.query.all()
        return users , 200
    
class Register(Resource):
    def post(self):
        args = parser.parse_args()

        is_existing = UsersTable.query.filter_by(name = args['name']).first()

        if is_existing:
            return {'msg': f'This user_name already exists {is_existing.name}'}
        
        new_user = UsersTable(name= args['name'], password = generate_password_hash(args['password']))
        db.session.add(new_user)
        db.session.commit()

        return {'msg': 'user created'}, 201

class Login(Resource):
    def post(self):
        args = parser.parse_args()
        user = UsersTable.query.filter_by(name= args['name']).first()

        if not user or not check_password_hash(user.password, args['password']):
            return {'msg': 'invalid password or username'}, 401
        
        # access_token = create_access_token(identity=str(user.id), expires_delta=timedelta(seconds=40))
        return {'access_token':access_token}

class Profile(Resource):
    @jwt_required()
    def get(self):
        current_user_id = get_jwt_identity()
        user = UsersTable.query.get(current_user_id)
        return {'logged_in_as': user.name}, 200


#hello how are you

api.add_resource(Profile, '/api/profile')
api.add_resource(Users, '/api/users')
api.add_resource(Register, '/api/register')
api.add_resource(Login,'/api/login')


