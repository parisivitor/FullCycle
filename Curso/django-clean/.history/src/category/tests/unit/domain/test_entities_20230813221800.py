from datetime import datetime
import unittest
from ...domain.entities import Category


class TestCategory(unittest.TestCase):

    def test_constructor(self):
        category = Category('Movie', 'Some Description', True, datetime.now())
        self.assertEqual(category.name, 'Movie')
        self.assertEqual(category.description, 'Some Description')
        self.assertTrue(category.is_active)
        self.assertIsInstance(category.created_at, datetime)
