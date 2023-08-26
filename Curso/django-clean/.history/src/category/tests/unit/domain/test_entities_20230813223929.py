from dataclasses import is_dataclass
from datetime import datetime
import unittest
from ....domain.entities import Category


class TestCategory(unittest.TestCase):

    def test_is_a_dataclass(self):
        self.assertTrue(is_dataclass(Category))

    def test_constructor(self):
        category = Category(name='Movies')
        self.assertEqual(category.name, 'Movies')
        self.assertEqual(category.description, None)
        self.assertEqual(category.is_active, True)
        self.assertIsInstance(category.created_at, datetime)

        created_at = datetime.now()
        category = Category(
            name='Movie',
            description='Some Description',
            is_active=False,
            created_at=created_at
        )
        self.assertEqual(category.name, 'Movie')
        self.assertEqual(category.description, 'Some Description')
        self.assertFalse(category.is_active)
        self.assertEqual(category.created_at, created_at)

    def test_if_created_at_is_generated_in_constructor(self):
        category1 = Category(name='Movie1')
        category2 = Category(name='Movie2')
        self.assertNotEqual(category1.created_at.timestamp(), category2.created_at.timestamp())
