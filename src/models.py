import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User(Base):
    __tablename__= 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    email = Column(String(100), nullable=False, unique=True)
    password = Column(String(250), nullable=False)

    def __init__(self, user_name, user_password, user_email):
        self.name = user_name
        self.email = user_email
        self.password = user_password

class Post(Base):
    __tablename__= 'post'
    id = Column(Integer, primary_key=True)
    imagen = Column(String(250), nullable=False)

    user_id = Column(Integer, ForeignKey("user.id"))             
    user = relationship("User")

class Likes(Base):
    __tablename__= 'likes'
    id = Column(Integer, primary_key=True)

    post_id = Column(Integer, ForeignKey('post.id'))
    post = relationship('Post')

class Coment(Base):
    __tablename__= 'coment'
    id = Column(Integer, primary_key=True)
    conten = Column(String(250))

    post_id = Column(Integer, ForeignKey('post.id'))
    post = relationship('Post')


    def to_dict(self):
        return {}

    render_er(Base, 'diagram.png')

# ## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e