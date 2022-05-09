import unittest
from connector import Connector
from models import Pushes
from own_email import Email

class TestStringMethods(unittest.TestCase):

    def test_update(self):
        Connector.update(usu='pablo')
        usuario:Pushes = Connector.session.query(Pushes).filter(Pushes.user == 'pablo')[0]
        self.assertEqual(usuario.push_count, 1)
        Connector.update(usu='pablo')
        usuario:Pushes = Connector.session.query(Pushes).filter(Pushes.user == 'pablo')[0]
        self.assertEqual(usuario.push_count, 2)
        Connector.update(usu='pablo')
        usuario:Pushes = Connector.session.query(Pushes).filter(Pushes.user == 'pablo')[0]
        self.assertEqual(usuario.push_count, 3)
        Connector.update(usu='pablo')
        usuario:Pushes = Connector.session.query(Pushes).filter(Pushes.user == 'pablo')[0]
        self.assertEqual(usuario.push_count, 4)
    
    def test_send_email(self):
        self.assertTrue(Email.send_email('Ainhoa'))
        
    def tearDown(self) -> None:
        Connector.delete('pablo')

if __name__ == '__main__':
    unittest.main()