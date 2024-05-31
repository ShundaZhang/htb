import bcrypt, datetime, random
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, String, Boolean, DateTime, create_engine
from sqlalchemy.ext.declarative import declarative_base

from application.util.general import generate, generate_user

Base = declarative_base()

class Users(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    username = Column(String)
    password = Column(String)
    token = Column(String)


class Database:
    def __init__(self):
        engine = create_engine(f"sqlite:///storage.db", echo=False)
        Base.metadata.create_all(engine)
        Session = sessionmaker(bind=engine)
        session = Session()
        self.session = session


    def migrate(self):
        for i in range(10):
            username = generate_user()
            password = generate(32)
            token = generate(16)
            self.create_user(username, password, token)

    
    def create_user(self, username, password, token):
        user = self.session.query(Users).filter(Users.username == username).first()
        if user:
            return False

        password_bytes = password.encode("utf-8")
        salt = bcrypt.gensalt()
        password_hash = bcrypt.hashpw(password_bytes, salt).decode()

        new_user = Users(username=username, password=password_hash, token=token)
        self.session.add(new_user)
        self.session.commit()

        return True


    def check_user(self, username, password):
        user = self.session.query(Users).filter(Users.username == username).first()

        if not user:
            return False
        
        password_bytes = password.encode("utf-8")
        password_encoded = user.password.encode("utf-8")
        matched = bcrypt.checkpw(password_bytes, password_encoded)
        
        if matched:
            return True
        
        return False

    def check_token(self, token):
        user = self.session.query(Users).filter(Users.token == token).first()

        if not user:
            return False
        
        return True