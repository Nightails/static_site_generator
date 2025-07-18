import unittest

from src.htmlnode import HTMLNode, LeafNode, ParentNode


class TestHTMLNode(unittest.TestCase):
    def test_to_html_props(self):
        node = HTMLNode(
            "div",
            "Hello, world!",
            None,
            {"class": "greeting", "href": "https://boot.dev"},
        )
        self.assertEqual(
            node.props_to_html(),
            ' class="greeting" href="https://boot.dev"',
        )

    def test_values(self):
        node = HTMLNode(
            "div",
            "I wish I could read",
        )
        self.assertEqual(
            node.tag,
            "div",
        )
        self.assertEqual(
            node.value,
            "I wish I could read",
        )
        self.assertEqual(
            node.children,
            None,
        )
        self.assertEqual(
            node.props,
            None,
        )

    def test_repr(self):
        node = HTMLNode(
            "p",
            "What a strange world",
            None,
            {"class": "primary"},
        )
        self.assertEqual(
            node.__repr__(),
            "HTMLNode(p, What a strange world, children: None, {'class': 'primary'})",
        )


class TextLeafNode(unittest.TestCase):
    def test_to_html(self):
        test_cases = [
            ["p", "This is a paragraph of text."],
            ["a", "Click me!", {"href": "https://www.google.com"}],
            [None, "Some raw text."],
        ]

        test_results = [
            "<p>This is a paragraph of text.</p>",
            '<a href="https://www.google.com">Click me!</a>',
            "Some raw text.",
        ]

        nodes = []
        for case in test_cases:
            if len(case) < 3:
                nodes.append(LeafNode(case[0], case[1]))
            else:
                nodes.append(LeafNode(case[0], case[1], case[2]))
        for i in range(len(test_results)):
            self.assertEqual(nodes[i].to_html(), test_results[i])


class TextParentNode(unittest.TestCase):
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )


if __name__ == "__main__":
    unittest.main()
