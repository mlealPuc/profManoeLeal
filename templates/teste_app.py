# test_app.py
import unittest
from app import app

class TestApp(unittest.TestCase):

    def setUp(self):
        app.config['TESTING'] = True
        self.app = app.test_client()

    def test_index(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Login', response.data)

    def test_login_valid_credentials(self):
        response = self.app.post('/login', data=dict(usuario='usuario1', senha='senha1'), follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Bem-vindo, usuario1!', response.data)

    def test_login_invalid_credentials(self):
        response = self.app.post('/login', data=dict(usuario='usuario1', senha='senha_errada'), follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Credenciais inválidas. Tente novamente.', response.data)

if __name__ == '__main__':
    unittest.main()