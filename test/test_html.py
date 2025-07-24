import unittest
from src.html import extract_title


class TestHTML(unittest.TestCase):
    def text_extract_title(self):
        md = "# Hello World!"
        title = extract_title(md)
        self.assertEqual(title, "Hello World!")


if __name__ == "__main__":
    unittest.main()
