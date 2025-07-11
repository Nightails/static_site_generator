from textnode import TextType, TextNode 
from leafnode import LeafNode

def text_node_to_html_node(text_node):
    match (text_node.text_type):
        case TextType.TEXT:
            return LeafNode(None, text_node.text, None)
        case TextType.BOLD:
            return LeafNode("b", text_node.text, None)
        case TextType.ITALIC:
            return LeafNode("i", text_node.text, None)
        case TextType.CODE:
            return LeafNode("code", text_node.text, None)
        case TextType.LINK:
            return LeafNode("a", text_node.text, {"href": f"{text_node.url}"})
        case TextType.IMAGE:
            return LeafNode("img", None, {"src": f"{text_node.url}", "alt": f"{text_node.text}"})
        case _:
            raise Exception(f"{text_node} has invalid text_type")

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    final_nodes = []
    for node in old_nodes:
        if node.text_type is not TextType.TEXT:
            final_nodes.append(node)
        texts = node.text.split(delimiter)
        for i in range(len(texts)):
            new_node = TextNode(texts[i], TextType.TEXT)
            if i % 2 != 0:
                new_node.text_type = text_type
            final_nodes.append(new_node)

    return final_nodes
