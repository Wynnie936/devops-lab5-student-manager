"""Unit test cho Student Manager — chạy: python -m unittest discover tests"""
import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

from student import Student  # noqa: E402
from main import add_student, search_student  # noqa: E402


def sample():
    return [
        Student("SV001", "Nguyen Van A", 20, "K20"),
        Student("SV002", "Tran Thi B", 21, "K20"),
        Student("SV003", "Le Van C", 19, "K21"),
    ]


class TestStudent(unittest.TestCase):
    def test_to_dict(self):
        s = Student("SV009", "Test", 18, "K22")
        self.assertEqual(s.to_dict()["student_id"], "SV009")


class TestAddStudent(unittest.TestCase):
    def test_add_new(self):
        result = add_student(sample(), "SV004", "Pham Thi D", 22, "K19")
        self.assertEqual(len(result), 4)

    def test_reject_duplicate_id(self):
        result = add_student(sample(), "SV001", "Trung Ma", 20, "K20")
        self.assertEqual(len(result), 3)


class TestSearchStudent(unittest.TestCase):
    def test_search_by_name_case_insensitive(self):
        self.assertEqual(len(search_student(sample(), "van")), 2)

    def test_search_by_id(self):
        self.assertEqual(search_student(sample(), "sv002")[0].name, "Tran Thi B")

    def test_not_found(self):
        self.assertEqual(search_student(sample(), "xyz"), [])


if __name__ == "__main__":
    unittest.main()
