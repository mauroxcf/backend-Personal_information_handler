from sqlalchemy import Boolean, Column , ForeignKey, DateTime, Integer, String, Text, Float, Enum
from sqlalchemy_serializer import SerializerMixin
from flaskr.utils.db import db
import enum
import datetime

class DocumentType(enum.Enum):
    registro_civil = "Registro civil"
    tarjeta_de_identidad = "Tarjeta de identidad"
    cedula = "Cedula"
    pasaporte = "Pasaporte"


class PersonalData(SerializerMixin, db.Model):
    """Information of the Person
    """
    __tablename__ = 'personaldata'
    id = Column(Integer, primary_key=True,)
    document_type = Column(Enum(DocumentType), nullable=False)
    document_id = Column(Integer, nullable=False, unique = True)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)
    first_name = Column(String(255), nullable=False)
    last_name = Column(String(255), nullable=False)
    hobbie = Column(String(255), nullable=False)

    def __init__(self, document_type, document_id, first_name, last_name):
        self.document_type = document_type
        self.document_id = document_id
        self.first_name = first_name
        self.last_name = last_name
        self.hobbie = hobbie
