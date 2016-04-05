import unittest
from currency import *

USD1 = Currency(50.00, 'USD')
USD2 = Currency(50.00, 'USD')
USD3 = Currency(25.00, 'USD')
YEN1 = Currency(50.00, 'YEN')


class TestCurrency(unittest.TestCase):
    def test___eq__(self):
        # self.assertTrue(USD1 == USD2)
        # self.assertTrue(USD2 == USD1)
        # self.assertFalse(USD1 == USD3)
        # self.assertFalse(USD2 == USD3)
        # self.assertFalse(USD1 == YEN1)
        pass

    def test___nq__(self):
        # self.assertFalse(USD1 != USD2)
        # self.assertFalse(USD2 != USD1)
        # self.assertTrue(USD1 != USD3)
        # self.assertTrue(USD2 != USD3)
        # self.assertTrue(USD1 != YEN1)
        pass

    def test___add__(self):
        # self.assertEqual((USD1 + USD2), 100.00)
        # self.assertEqual((USD2 + USD1), 100.00)
        # self.assertEqual((USD1 + USD3), 75.00)
        # self.assertEqual((USD2 + USD3), 75.00)
        # self.assertEqual((USD1 + YEN1), DifferentCurrencyCodeError)
        pass

    def test___sub__(self):
        # self.assertEqual((USD1 - USD2), 0.00)
        # self.assertEqual((USD2 - USD1), 0.00)
        # self.assertEqual((USD1 - USD3), 25.00)
        # self.assertEqual((USD2 - USD3), 25.00)
        # self.assertEqual((USD1 - YEN1), DifferentCurrencyCodeError)
        pass


    # def test_list_normal_words(self):
    #     self.assertEqual(list_normal_words(test_words), ["STREAM", "KNEECAP", "COOKBOOK", "LANGUAGE", "SNEAKER"])
    #
    #
    # def test_list_hard_words(self):
    #     self.assertEqual(list_hard_words(test_words), ["COOKBOOK", "LANGUAGE", "ALGORITHM", "INTEGRATION"])
    #
    #
    # def test_generate_random_word(self):
    #     word = generate_random_word(test_words)
    #     self.assertTrue(word in test_words)
    #
    #
    # def test_display_visual_guesses(self):
    #     word = "INTEGRATION"
    #     self.assertEqual(display_visual_guesses(word, []), "___________")
    #     self.assertEqual(display_visual_guesses(word, ["Z"]), "___________")
    #     self.assertEqual(display_visual_guesses(word, ["G"]), "____G______")
    #     self.assertEqual(display_visual_guesses(word, ["I"]), "I_______I__")
    #     self.assertEqual(display_visual_guesses(word, ["I", "G"]), "I___G___I__")
    #     self.assertEqual(display_visual_guesses(word, ["I", "N", "Z"]), "IN______I_N")
    #
    #
    # def test_is_word_complete(self):
    #     word = "RIVER"
    #     self.assertFalse(is_word_complete(word, []))
    #     self.assertFalse(is_word_complete(word, ["R"]))
    #     self.assertFalse(is_word_complete(word, ["R", "E"]))
    #     self.assertFalse(is_word_complete(word, ["R", "E", "E"]))
    #     self.assertTrue(is_word_complete(word, ["R", "E", "V", "R"]))


if __name__ == '__main__':
    unittest.main()
