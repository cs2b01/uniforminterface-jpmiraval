from sqlalchemy import Column, Integer, String, Sequence, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from database import connector

class Book(connector.Manager.Base):
#    __tablename__ = "users"
#    id = Column(Integer, Sequence('book_id_seq'), primary_key=True)
#    name = Column(String(50))
#    isbn = Column(String(12))
#    title = Column(String(120))

#class Form(connector.Manager.Base):
    __tablename__ = "users"
    id = Column(Integer, Sequence('form_id_seq'), primary_key=True)
    Codigo = Column(String(9))
    Nombre = Column(String(12))
    Apellido = Column(String(120))
    Password = Column(String(100))