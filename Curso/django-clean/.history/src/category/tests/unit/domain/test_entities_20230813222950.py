from dataclasses import is_dataclass
from datetime import datetime
import unittest
from ....domain.entities import Category


class TestCategory(unittest.TestCase):

    def test_is_a_dataclass(self):
        self.assertTrue(is_dataclass(Category))

    def test_constructor(self):
        category = Category(
            name='Movie',
            description='Some Description',
            is_active=True,
            created_at=datetime.now()
        )
        self.assertEqual(category.name, 'Movie')
        self.assertEqual(category.description, 'Some Description')
        self.assertTrue(category.is_active)
        self.assertIsInstance(category.created_at, datetime)
