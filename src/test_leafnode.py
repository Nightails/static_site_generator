import unittest
from leafnode import LeafNode

test_cases = [
    ["p", "This is a paragraph of text."],
    ["a", "Click me!", {"href": "https://www.google.com"}],
    [None, "Some raw text."]
]

test_results = [
    '<p>This is a paragraph of text.</p>',
    '<a href="https://www.google.com">Click me!</a>',
    'Some raw text.'
]

class TextLeafNode(unittest.TestCase):
    def test_to_html(self):
        nodes = []
        for case in test_cases:
            if len(case) < 3:
                nodes.append(LeafNode(case[0], case[1]))
            else:
                nodes.append(LeafNode(case[0], case[1], case[2]))
        for i in range(len(test_results)):
            self.assertEqual(nodes[i].to_html(), test_results[i])

if __name__ == "__main__":
    unittest.main()
