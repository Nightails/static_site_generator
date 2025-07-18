import unittest

from src.markdown_blocks import BlockType, block_to_block_type, markdown_to_blocks


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
        print(self.blocks[1])
        self.assertEqual(self.block_types[1], BlockType.CODE)

    def test_quote(self):
        self.assertEqual(self.block_types[2], BlockType.QUOTE)

    def test_unordered_list(self):
        self.assertEqual(self.block_types[3], BlockType.UNORDERED_LIST)

    def test_ordered_list(self):
        self.assertEqual(self.block_types[4], BlockType.ORDERED_LIST)

    def test_paragraph(self):
        self.assertEqual(self.block_types[5], BlockType.PARAGRAPH)


if __name__ == "__main__":
    unittest.main()
