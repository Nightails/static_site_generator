import unittest
from textnode import TextNode, TextType
from utilities import split_nodes_delimiter

test_nodes = [
    TextNode("This is text with a **bold** word", TextType.TEXT),
    TextNode("This is text with a _italic_ word", TextType.TEXT),
    TextNode("This is text with a `code block` word", TextType.TEXT),
    TextNode("This is text with normal words", TextType.TEXT)
]

bold_split_result = [
    TextNode("This is text with a ", TextType.TEXT),
    TextNode("bold", TextType.BOLD),
    TextNode(" word", TextType.TEXT),
    TextNode("This is text with a _italic_ word", TextType.TEXT),
    TextNode("This is text with a `code block` word", TextType.TEXT),
    TextNode("This is text with normal words", TextType.TEXT)
]
italic_split_result = [
    TextNode("This is text with a **bold** word", TextType.TEXT),
    TextNode("This is text with a ", TextType.TEXT),
    TextNode("italic", TextType.ITALIC),
    TextNode(" word", TextType.TEXT),
    TextNode("This is text with a `code block` word", TextType.TEXT),
    TextNode("This is text with normal words", TextType.TEXT)
]
code_split_result = [
    TextNode("This is text with a **bold** word", TextType.TEXT),
    TextNode("This is text with a _italic_ word", TextType.TEXT),
    TextNode("This is text with a ", TextType.TEXT),
    TextNode("code block", TextType.CODE),
    TextNode(" word", TextType.TEXT),
    TextNode("This is text with normal words", TextType.TEXT)
]

class TestSplitNodeDelimiter(unittest.TestCase):
    def test_split_node_delimiter(self):
        
        bold_split = split_nodes_delimiter(test_nodes, "**", TextType.BOLD)
        italic_split = split_nodes_delimiter(test_nodes, "_", TextType.ITALIC)
        code_split = split_nodes_delimiter(test_nodes, "`", TextType.CODE)
        self.assertEqual(bold_split, bold_split_result)
        self.assertEqual(italic_split, italic_split_result)
        self.assertEqual(code_split, code_split_result)

if __name__ == "__main__":
    unittest.main()

