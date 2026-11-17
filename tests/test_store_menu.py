import unittest

from store_menu import menu_options


class MenuOptionsTests(unittest.TestCase):
    def test_splits_and_trims_menu_choices(self):
        menu = {"COLORS": " Red, Black ,, Blue "}

        self.assertEqual(
            menu_options(menu, "COLORS"),
            ["Red", "Black", "Blue"],
        )

    def test_returns_empty_list_for_missing_category(self):
        self.assertEqual(menu_options({}, "SIZES"), [])


if __name__ == "__main__":
    unittest.main()
