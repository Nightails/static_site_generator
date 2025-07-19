from enum import Enum
from src.htmlnode import ParentNode, LeafNode
from src.textnode import TextType, TextNode, text_node_to_html_node
from src.inline_markdown import text_to_textnodes


class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    ULIST = "unordered_list"
    OLIST = "ordered_list"


def markdown_to_blocks(markdown):
    blocks = []
    lines = markdown.split("\n\n")
    for line in lines:
        if line == "":
            continue
        line = line.strip()
        blocks.append(line)
    return blocks


def block_to_block_type(block):
    lines = block.split("\n")

    if block.startswith(("# ", "## ", "### ", "#### ", "##### ", "###### ")):
        return BlockType.HEADING
    if len(lines) > 1 and lines[0].startswith("```") and lines[-1].startswith("```"):
        return BlockType.CODE
    if block.startswith(">"):
        for line in lines:
            if not line.startswith(">"):
                return BlockType.PARAGRAPH
        return BlockType.QUOTE
    if block.startswith("- "):
        for line in lines:
            if not line.startswith("- "):
                return BlockType.PARAGRAPH
        return BlockType.ULIST
    if block.startswith("1. "):
        i = 1
        for line in lines:
            if not line.startswith(f"{i}. "):
                return BlockType.PARAGRAPH
            i += 1
        return BlockType.OLIST
    return BlockType.PARAGRAPH


def markdown_to_html_node(markdown):
    htmlnodes = []
    blocks = markdown_to_blocks(markdown)
    for block in blocks:
        block_type = block_to_block_type(block)
        htmlnodes.append(block_to_html_node(block, block_type))
    return ParentNode("div", htmlnodes)


def block_to_html_node(text, block_type):
    match block_type:
        case BlockType.PARAGRAPH:
            children_nodes = text_to_children_nodes(text)
            return ParentNode("p", children_nodes)
        case BlockType.HEADING:
            sections = text.split(" ", 1)
            head_tag = f"h{len(sections[0])}"
            return LeafNode(head_tag, sections[1])
        case BlockType.CODE:
            children_node = [LeafNode("code", text_to_code_text(text))]
            return ParentNode("pre", children_node)
        case BlockType.QUOTE:
            quote_text = text_to_quote_text(text)
            return LeafNode("blockquote", quote_text)
        case BlockType.ULIST:
            children_list_nodes = text_list_to_children_nodes(text)
            return ParentNode("ul", children_list_nodes)
        case BlockType.OLIST:
            children_list_nodes = text_list_to_children_nodes(text)
            return ParentNode("ol", children_list_nodes)


def text_to_children_nodes(text):
    html_nodes = []
    text_nodes = text_to_textnodes(text)
    for node in text_nodes:
        node.text = node.text.replace("\n", " ")
        html_nodes.append(text_node_to_html_node(node))
    return html_nodes


def text_to_code_text(text):
    return text.replace("```", "").lstrip()


def text_to_quote_text(text):
    return text.replace("> ", "").lstrip()


def text_list_to_children_nodes(text):
    html_nodes = []
    lines = text.split("\n")
    for line in lines:
        line = line.split(" ", 1)[1]
        html_node = text_node_to_html_node(TextNode(line, TextType.TEXT))
        html_node.tag = "li"
        html_nodes.append(html_node)
    return html_nodes
