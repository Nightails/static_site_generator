import unittest

from src.markdown_blocks import (
    BlockType,
    block_to_block_type,
    markdown_to_blocks,
    markdown_to_html_node,
)


class TestMarkdownToBlocks(unittest.TestCase):
    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )


class TestBlockType(unittest.TestCase):
    md = """
# Heading

```
Some code
```

> Some insperating quote

- Thing
- Other thing
- Another thing

1. First thing
2. Second thing
3. Third thing

A normal paragraph
"""
    blocks = markdown_to_blocks(md)
    block_types = []
    for b in blocks:
        block_types.append(block_to_block_type(b))

    def test_heading(self):
        self.assertEqual(self.block_types[0], BlockType.HEADING)

    def test_code(self):
        self.assertEqual(self.block_types[1], BlockType.CODE)

    def test_quote(self):
        self.assertEqual(self.block_types[2], BlockType.QUOTE)

    def test_unordered_list(self):
        self.assertEqual(self.block_types[3], BlockType.ULIST)

    def test_ordered_list(self):
        self.assertEqual(self.block_types[4], BlockType.OLIST)

    def test_paragraph(self):
        self.assertEqual(self.block_types[5], BlockType.PARAGRAPH)


class TestMarkdownToHTMLNode(unittest.TestCase):
    def test_paragraphs(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )

    def test_codeblock(self):
        md = """
```
This is text that _should_ remain
the **same** even with inline stuff
```
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
        )

    def test_heading(self):
        md = """
# Heading 1

## Heading 2

### Heading 3

#### Heading 4

##### Heading 5

###### Heading 6
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><h1>Heading 1</h1><h2>Heading 2</h2><h3>Heading 3</h3><h4>Heading 4</h4><h5>Heading 5</h5><h6>Heading 6</h6></div>",
        )

    def test_quote(self):
        md = """
> Some amazing quote.
> With multiple lines.
> And another one, just for fun.
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><blockquote>Some amazing quote.\nWith multiple lines.\nAnd another one, just for fun.</blockquote></div>",
        )

    def test_list(self):
        md = """
- item
- item
- item

1. item
2. item
3. item
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ul><li>item</li><li>item</li><li>item</li></ul><ol><li>item</li><li>item</li><li>item</li></ol></div>",
        )


if __name__ == "__main__":
    unittest.main()
