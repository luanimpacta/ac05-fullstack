from unittest import TestCase, main
from app import app


class Testes(TestCase):
    def test_sum(self):
        tester = app.test_client(self)
        response = tester.post('/calculator', data=dict(number1='10', number2='10', operation='math'))
        self.assertEqual(response.status, '200 OK')
        self.assertTrue(b'20' in response.data)

    def test_sub(self):
        tester = app.test_client(self)
        response = tester.post('/calculator', data=dict(number1='10', number2='10', operation='sub'))
        self.assertEqual(response.status, '200 OK')
        self.assertTrue(b'0' in response.data)

    def test_mult(self):
        tester = app.test_client(self)
        response = tester.post('/calculator', data=dict(number1='10', number2='10', operation='mult'))
        self.assertEqual(response.status, '200 OK')
        self.assertTrue(b'100' in response.data)

    def test_div(self):
        tester = app.test_client(self)
        response = tester.post('/calculator', data=dict(number1='81', number2='2', operation='div'))
        self.assertEqual(response.status, '200 OK')
        self.assertTrue(b'40.5' in response.data)

    def test_div2(self):
        tester = app.test_client(self)
        response = tester.post('/calculator', data=dict(number1='81', number2='0', operation='div'))
        self.assertEqual(response.status, '200 OK')
        self.assertTrue(b'Voce nao pode fazer divisao por 0' in response.data)

    def test_power(self):
        tester = app.test_client(self)
        response = tester.post('/calculator', data=dict(number1='10', number2='2', operation='power'))
        self.assertEqual(response.status, '200 OK')
        self.assertTrue(b'100.0' in response.data)

    def test_square_root(self):
        tester = app.test_client(self)
        response = tester.post('/calculator', data=dict(number1='81', operation='square_root'))
        self.assertEqual(response.status, '200 OK')
        self.assertTrue(b'9.0' in response.data)

    def test_logarithm(self):
        tester = app.test_client(self)
        response = tester.post('/calculator', data=dict(number1='81', operation='logarithm'))
        self.assertEqual(response.status, '200 OK')
        self.assertTrue(b'1.9084850188786497' in response.data)


if __name__ == '__main__':
    main()
