from src.htmlnode import HTMLNode, ParentNode, LeafNode
from src.block import BlockType, block_to_block_type, markdown_to_blocks


def markdown_to_html_node(markdown):
    htmlnodes = []
    blocks = markdown_to_blocks(markdown)
    for block in blocks:
        block_type = block_to_block_type(block)
        match block_type:
            case BlockType.PARAGRAPH:
                htmlnodes.append(HTMLNode("p", block))
            case BlockType.HEADING:
                tag = heading_tag(block)
                htmlnodes.append(HTMLNode(tag, block))
            case BlockType.CODE:
                htmlnodes.append(HTMLNode("p", block))
            case BlockType.QUOTE:
                htmlnodes.append(HTMLNode("p", block))
            case BlockType.UNORDERED_LIST:
                htmlnodes.append(HTMLNode("p", block))
            case BlockType.ORDERED_LIST:
                htmlnodes.append(HTMLNode("p", block))
    return ParentNode("div", htmlnodes)


def heading_tag(block):
    heading = block.split(" ", 1)[0]
    return f"h{len(heading)}"
