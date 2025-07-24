import unittest
from src import textnode


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = textnode.TextNode("This is a text node", textnode.TextType.TEXT)
        node2 = textnode.TextNode("This is a text node", textnode.TextType.TEXT)
        self.assertEqual(node, node2)

    def test_eq_false(self):
        node = textnode.TextNode("This is a text node", textnode.TextType.TEXT)
        node2 = textnode.TextNode("This is a text node", textnode.TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_eq_false2(self):
        node = textnode.TextNode("This is a text node", textnode.TextType.TEXT)
        node2 = textnode.TextNode("This is a text node2", textnode.TextType.TEXT)
        self.assertNotEqual(node, node2)

    def test_eq_url(self):
        node = textnode.TextNode(
            "This is a text node", textnode.TextType.TEXT, "https://www.boot.dev"
        )
        node2 = textnode.TextNode(
            "This is a text node", textnode.TextType.TEXT, "https://www.boot.dev"
        )
        self.assertEqual(node, node2)

    def test_repr(self):
        node = textnode.TextNode(
            "This is a text node", textnode.TextType.TEXT, "https://www.boot.dev"
        )
        self.assertEqual(
            "TextNode(This is a text node, text, https://www.boot.dev)", repr(node)
        )


class TestTextNodeToHTMLNode(unittest.TestCase):
    def test_text(self):
        node = textnode.TextNode("This is a text node", textnode.TextType.TEXT)
        html_node = textnode.text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_image(self):
        node = textnode.TextNode(
            "This is an image", textnode.TextType.IMAGE, "https://www.boot.dev"
        )
        html_node = textnode.text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")
        self.assertEqual(
            html_node.props,
            {"src": "https://www.boot.dev", "alt": "This is an image"},
        )

    def test_bold(self):
        node = textnode.TextNode("This is bold", textnode.TextType.BOLD)
        html_node = textnode.text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "This is bold")


if __name__ == "__main__":
    unittest.main()
