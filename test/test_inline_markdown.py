import unittest
from src import inline_markdown
from src import textnode


class TestInlineMarkdown(unittest.TestCase):
    def test_delim_bold(self):
        node = textnode.TextNode(
            "This is text with a **bolded** word", textnode.TextType.TEXT
        )
        new_nodes = inline_markdown.split_nodes_delimiter(
            [node], "**", textnode.TextType.BOLD
        )
        self.assertListEqual(
            [
                textnode.TextNode("This is text with a ", textnode.TextType.TEXT),
                textnode.TextNode("bolded", textnode.TextType.BOLD),
                textnode.TextNode(" word", textnode.TextType.TEXT),
            ],
            new_nodes,
        )

    def test_delim_bold_double(self):
        node = textnode.TextNode(
            "This is text with a **bolded** word and **another**",
            textnode.TextType.TEXT,
        )
        new_nodes = inline_markdown.split_nodes_delimiter(
            [node], "**", textnode.TextType.BOLD
        )
        self.assertListEqual(
            [
                textnode.TextNode("This is text with a ", textnode.TextType.TEXT),
                textnode.TextNode("bolded", textnode.TextType.BOLD),
                textnode.TextNode(" word and ", textnode.TextType.TEXT),
                textnode.TextNode("another", textnode.TextType.BOLD),
            ],
            new_nodes,
        )

    def test_delim_bold_multiword(self):
        node = textnode.TextNode(
            "This is text with a **bolded word** and **another**",
            textnode.TextType.TEXT,
        )
        new_nodes = inline_markdown.split_nodes_delimiter(
            [node], "**", textnode.TextType.BOLD
        )
        self.assertListEqual(
            [
                textnode.TextNode("This is text with a ", textnode.TextType.TEXT),
                textnode.TextNode("bolded word", textnode.TextType.BOLD),
                textnode.TextNode(" and ", textnode.TextType.TEXT),
                textnode.TextNode("another", textnode.TextType.BOLD),
            ],
            new_nodes,
        )

    def test_delim_italic(self):
        node = textnode.TextNode(
            "This is text with an _italic_ word", textnode.TextType.TEXT
        )
        new_nodes = inline_markdown.split_nodes_delimiter(
            [node], "_", textnode.TextType.ITALIC
        )
        self.assertListEqual(
            [
                textnode.TextNode("This is text with an ", textnode.TextType.TEXT),
                textnode.TextNode("italic", textnode.TextType.ITALIC),
                textnode.TextNode(" word", textnode.TextType.TEXT),
            ],
            new_nodes,
        )

    def test_delim_bold_and_italic(self):
        node = textnode.TextNode("**bold** and _italic_", textnode.TextType.TEXT)
        new_nodes = inline_markdown.split_nodes_delimiter(
            [node], "**", textnode.TextType.BOLD
        )
        new_nodes = inline_markdown.split_nodes_delimiter(
            new_nodes, "_", textnode.TextType.ITALIC
        )
        self.assertEqual(
            [
                textnode.TextNode("bold", textnode.TextType.BOLD),
                textnode.TextNode(" and ", textnode.TextType.TEXT),
                textnode.TextNode("italic", textnode.TextType.ITALIC),
            ],
            new_nodes,
        )

    def test_delim_code(self):
        node = textnode.TextNode(
            "This is text with a `code block` word", textnode.TextType.TEXT
        )
        new_nodes = inline_markdown.split_nodes_delimiter(
            [node], "`", textnode.TextType.CODE
        )
        self.assertListEqual(
            [
                textnode.TextNode("This is text with a ", textnode.TextType.TEXT),
                textnode.TextNode("code block", textnode.TextType.CODE),
                textnode.TextNode(" word", textnode.TextType.TEXT),
            ],
            new_nodes,
        )

    def test_extract_markdown_images(self):
        matches = inline_markdown.extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_extract_markdown_links(self):
        matches = inline_markdown.extract_markdown_links(
            "This is text with a [link](https://boot.dev) and [another link](https://blog.boot.dev)"
        )
        self.assertListEqual(
            [
                ("link", "https://boot.dev"),
                ("another link", "https://blog.boot.dev"),
            ],
            matches,
        )

    def test_split_image(self):
        node = textnode.TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)",
            textnode.TextType.TEXT,
        )
        new_nodes = inline_markdown.split_nodes_image([node])
        self.assertListEqual(
            [
                textnode.TextNode("This is text with an ", textnode.TextType.TEXT),
                textnode.TextNode(
                    "image", textnode.TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"
                ),
            ],
            new_nodes,
        )

    def test_split_image_single(self):
        node = textnode.TextNode(
            "![image](https://www.example.COM/IMAGE.PNG)",
            textnode.TextType.TEXT,
        )
        new_nodes = inline_markdown.split_nodes_image([node])
        self.assertListEqual(
            [
                textnode.TextNode(
                    "image",
                    textnode.TextType.IMAGE,
                    "https://www.example.COM/IMAGE.PNG",
                ),
            ],
            new_nodes,
        )

    def test_split_images(self):
        node = textnode.TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            textnode.TextType.TEXT,
        )
        new_nodes = inline_markdown.split_nodes_image([node])
        self.assertListEqual(
            [
                textnode.TextNode("This is text with an ", textnode.TextType.TEXT),
                textnode.TextNode(
                    "image", textnode.TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"
                ),
                textnode.TextNode(" and another ", textnode.TextType.TEXT),
                textnode.TextNode(
                    "second image",
                    textnode.TextType.IMAGE,
                    "https://i.imgur.com/3elNhQu.png",
                ),
            ],
            new_nodes,
        )

    def test_split_links(self):
        node = textnode.TextNode(
            "This is text with a [link](https://boot.dev) and [another link](https://blog.boot.dev) with text that follows",
            textnode.TextType.TEXT,
        )
        new_nodes = inline_markdown.split_nodes_link([node])
        self.assertListEqual(
            [
                textnode.TextNode("This is text with a ", textnode.TextType.TEXT),
                textnode.TextNode("link", textnode.TextType.LINK, "https://boot.dev"),
                textnode.TextNode(" and ", textnode.TextType.TEXT),
                textnode.TextNode(
                    "another link", textnode.TextType.LINK, "https://blog.boot.dev"
                ),
                textnode.TextNode(" with text that follows", textnode.TextType.TEXT),
            ],
            new_nodes,
        )

    def test_text_to_textnodes(self):
        nodes = inline_markdown.text_to_textnodes(
            "This is **text** with an _italic_ word and a `code block` and an ![image](https://i.imgur.com/zjjcJKZ.png) and a [link](https://boot.dev)"
        )
        self.assertListEqual(
            [
                textnode.TextNode("This is ", textnode.TextType.TEXT),
                textnode.TextNode("text", textnode.TextType.BOLD),
                textnode.TextNode(" with an ", textnode.TextType.TEXT),
                textnode.TextNode("italic", textnode.TextType.ITALIC),
                textnode.TextNode(" word and a ", textnode.TextType.TEXT),
                textnode.TextNode("code block", textnode.TextType.CODE),
                textnode.TextNode(" and an ", textnode.TextType.TEXT),
                textnode.TextNode(
                    "image", textnode.TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"
                ),
                textnode.TextNode(" and a ", textnode.TextType.TEXT),
                textnode.TextNode("link", textnode.TextType.LINK, "https://boot.dev"),
            ],
            nodes,
        )


if __name__ == "__main__":
    unittest.main()
