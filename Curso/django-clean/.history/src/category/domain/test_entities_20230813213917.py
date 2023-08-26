from datetime import datetime
import unittest
from entities import Category


class TestCategory(unittest.TestCase):

    def test_constructor(self):
        Category('Movie', 'Some Description', True, datetime.now())
