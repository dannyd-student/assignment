import unittest

from src.logic import is_win, render_state, update_slices
class TestLogic(unittest.TestCase):
    def test_is_win_true(self):
        guessed_letters = {"a", "p", "l", "e"}
        self.assertTrue(is_win("apple", guessed_letters))
    def test_is_win_false(self):
        guessed_letters = {"a", "p"}
        self.assertFalse(is_win("apple", guessed_letters))
    def test_render_state_partial(self):
        guessed_letters = {"a", "e"}
        self.assertEqual(render_state("apple", guessed_letters), "a _ _ _ e")
    def test_render_state_all_hidden(self):
        guessed_letters = set()
        self.assertEqual(render_state("melon", guessed_letters), "_ _ _ _ _")
    def test_update_slices_wrong_guess(self):
        self.assertEqual(update_slices("apple", "z", 5), 4)
    def test_update_slices_correct_guess(self):
        self.assertEqual(update_slices("apple", "a", 5), 5)
if __name__ == "__main__":
    unittest.main()
