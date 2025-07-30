import unittest
from main import to_uppercase, to_cap, delete_space, count_letter as count_letters_total

class TestMain(unittest.TestCase):
    def test_upper_result(self):
        self.assertEqual(to_uppercase("hello"), "HELLO")
        self.assertEqual(to_uppercase("Python"), "PYTHON")

    def test_uses_upper_method(self):
        with open("main.py", "r") as f:
            code = f.read()
        self.assertIn(".upper(", code, "Il faut utiliser une method de string")

    def test_to_cap_result(self):
        self.assertEqual(to_cap("hello"), "Hello")
        self.assertEqual(to_cap("python"), "Python")

    def test_to_cap_uses_capitalize(self):
        with open("main.py", "r") as f:
            code = f.read()
        self.assertIn(".capitalize(", code)

    # ---------- TEST delete_space ----------
    def test_delete_space_result(self):
        self.assertEqual(delete_space("   hello   "), "hello")
        self.assertEqual(delete_space("  python "), "python")

    def test_delete_space_uses_strip(self):
        with open("main.py", "r") as f:
            code = f.read()
        self.assertIn(".strip(", code)

    # ---------- TEST count_letter (compter 'l') ----------
    def test_count_specific_letter_result(self):
        from main import count_letter as count_l  # on importe la première fonction
        self.assertEqual(count_l("hello"), 2)
        self.assertEqual(count_l("lollipop"), 3)

    def test_count_specific_letter_uses_count(self):
        with open("main.py", "r") as f:
            code = f.read()
        self.assertIn(".count(", code)

    # ---------- TEST count_letters_total (compter nb total lettres) ----------
    def test_count_total_letters_result(self):
        self.assertEqual(count_letters_total("hello"), 5)
        self.assertEqual(count_letters_total("python"), 6)

    def test_count_total_letters_uses_len(self):
        with open("main.py", "r") as f:
            code = f.read()
        self.assertIn("len(", code)

if __name__ == '__main__':
    unittest.main()
