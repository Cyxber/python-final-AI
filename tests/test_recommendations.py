import unittest

from recommendations import recommend_outfit


class RecommendOutfitTests(unittest.TestCase):
    def setUp(self):
        self.menu = {
            "TOPS": "T-Shirt, Hoodie",
            "COLORS": "Red, Black",
            "GRAPHICS": "Dinosaur, Unicorn",
            "SIZES": "Small, Large",
        }

    def test_matches_selected_color_and_size(self):
        recommendation = recommend_outfit(self.menu, "black", "large")

        self.assertEqual(
            recommendation,
            {
                "top": "T-Shirt",
                "color": "Black",
                "graphic": "Dinosaur",
                "size": "Large",
            },
        )

    def test_returns_none_for_unavailable_preferences(self):
        self.assertIsNone(recommend_outfit(self.menu, "Green", "Large"))
        self.assertIsNone(recommend_outfit(self.menu, "Red", "Medium"))

    def test_returns_none_without_a_top_or_graphic(self):
        incomplete_menu = {
            "COLORS": "Red",
            "SIZES": "Small",
        }

        self.assertIsNone(recommend_outfit(incomplete_menu, "Red", "Small"))


if __name__ == "__main__":
    unittest.main()
