from Validator import email_validator, password_validator
from Model import Users, Tokens, db
from bcrypt import hashpw, gensalt, checkpw
from fastapi import FastAPI
from pydantic import BaseModel
from secrets import token_hex
    
app = FastAPI()


class LoginSchema(BaseModel):
    username: str
    password: str


class RegisterSchema(LoginSchema):
    re_password: str
    
    
@app.get('/')
def root():
    return {'message': 'API Auth'}
    

@app.post('/register')
def register_user(data: RegisterSchema) -> dict:
    try:
        validator = email_validator(data.username)
        if validator:
            return {'message': validator}
        validator = password_validator(data.password, data.re_password)
        if validator:
            return {'message': validator}
        exists_email = db.session.query(Users).filter(Users.username == data.username).one_or_none()
        if exists_email:
            return {'message': 'Email already registered'}
        hash_pwd = hashpw(data.password.encode(), gensalt())
        user = Users(username=data.username, password=hash_pwd)
        db.session.add(user)
        db.session.commit()
        return {'message': 'Users registered successfully'}
    except Exception as e:
        return {'error': f'Error: Unable to save data: {e}'}

@app.post('/login')
def login(data: LoginSchema) -> dict:
    validator = email_validator(data.username)
    if validator:
        return {'message': validator}
    validator = password_validator(data.password)
    if validator:                
        return {'message': validator}
    user = db.session.query(Users).filter(Users.username == data.username).one_or_none()
    if not user:
        return {'message': 'Invalid Users'}
    if not checkpw(data.password.encode(), user.password.encode()):
        return {'message': 'Incorrect password'}
    
    while True:
        token = token_hex(50)
        exists_token = db.session.query(Tokens).filter(Tokens.token == token).one_or_none()
        if not exists_token:
            user_has_token = db.session.query(Tokens).filter(Tokens.id_user == user.id).one_or_none()
            if not user_has_token:
                new_token = Tokens(id_user=user.id, token=token)
                db.session.add(new_token)
                db.session.commit()
            else:
                user_has_token.token = token
                db.session.commit()
            return {'token': token}
                
    

            