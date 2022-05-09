import sqlalchemy
from models import Pushes, engine

class Connector(): 
    Session = sqlalchemy.orm.sessionmaker()
    Session.configure(bind=engine)
    session = Session()
    
    @classmethod
    def update(self, usu: str):
        users = self.session.query(Pushes).all()
        if(Pushes(usu) not in users):
            self.session.add(Pushes(user=usu))
            self.session.commit()
        else:
            usuario = self.session.query(Pushes).filter(Pushes.user == usu)[0]
            usuario.push_count += 1
            self.session.commit()
            
    @classmethod
    def delete(self, usu:str):
        self.session.query(Pushes).filter(Pushes.user == usu).delete()
        self.session.commit()