from django.test import TestCase

from app.calc import add, subtract


class CalcTests(TestCase):

    # 함수명은 항상 test 로 시작해야함
    def test_add_numbers(self):
        self.assertEqual(add(3, 8), 11)

    def test_subtract_numbers(self):
        self.assertEqual(subtract(5, 11), 6)
