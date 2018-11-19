import unittest

class TestFoo(unittest.TestCase):
    """
    Classe de teste inicial
    """

    def test_foo_elquals_foo(self):
        """
        Testa foo
        """
        self.assertEqual('foo', 'foo')
