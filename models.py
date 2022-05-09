import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base

engine = sqlalchemy.create_engine("mariadb+mariadbconnector://root:@localhost:3306/prueba")

Base = declarative_base()

class Pushes(Base):
    __tablename__ = 'Pushes'
    user = sqlalchemy.Column(sqlalchemy.String(length=50), primary_key=True)
    push_count = sqlalchemy.Column(sqlalchemy.Integer, default=1)
    
    def __init__(self, user):
        self.user = user
    
    def __eq__(self, __o: object) -> bool:
        return self.user == __o.user
    
    def __str__(self) -> str:
        return self.user
    
Base.metadata.create_all(engine)