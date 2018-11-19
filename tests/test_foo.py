import unittest
from bar import bar

class TestFoo(unittest.TestCase):
    """
    Classe de teste inicial
    """

    def test_foo_elquals_foo(self):
        """
        Testa foo
        """
        self.assertEqual('foo', 'foo')

class TestBar(unittest.TestCase):
    """
    Classe de teste bar
    """

    def test_bar_elquals_bar(self):
        """
        Testa bar
        """
        self.assertEqual(bar.echo('foo'), 'foo')
