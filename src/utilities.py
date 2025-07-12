import re

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
            continue
        texts = node.text.split(delimiter)
        for i in range(len(texts)):
            if texts[i] == "":
                continue
            new_node = TextNode(texts[i], TextType.TEXT)
            if i % 2 != 0:
                new_node.text_type = text_type
            final_nodes.append(new_node)

    return final_nodes


def extract_markdown_images(text):
    return re.findall(r"!\[(.*?)\]\((.*?)\)", text)


def extract_markdown_links(text):
    return re.findall(r"\[(.*?)\]\((.*?)\)", text)


def split_nodes_image(old_nodes):
    final_nodes = []
    for node in old_nodes:
        if node.text is None:
            continue

        # extract all markdown images
        # then create the nodes
        image_nodes = []
        images = extract_markdown_images(node.text)
        if len(images) == 0:
            final_nodes.append(node)
            continue

        for i in images:
            image_nodes.append(TextNode(i[0], TextType.IMAGE, i[1]))

        # split text to sections and remove extracted markdown images
        # then create the nodes
        text_nodes = []
        text_to_split = node.text
        for i in image_nodes:
            # assume each image is unique
            # otherwise, that is future me's problem
            sections = text_to_split.split(f"![{i.text}]({i.url})", 1)
            # there may still be left over sectons to split
            text_to_split = sections[1] if len(sections) > 1 else sections[0]
            text_nodes.append(TextNode(sections[0], TextType.TEXT))
        # left over from the final split
        if text_to_split != "":
            text_nodes.append(TextNode(text_to_split, TextType.TEXT))

        # merge both image and text nodes into final result
        i = 0 # image index
        for t in text_nodes:
            final_nodes.append(t)
            if i < len(image_nodes):
                final_nodes.append(image_nodes[i])
                i += 1

    return final_nodes


def split_nodes_link(old_nodes):
    final_nodes = []
    for node in old_nodes:
        if node.text is None:
            continue

        # extract all markdown links
        # then create the nodes
        link_nodes = []
        links = extract_markdown_links(node.text)
        if len(links) == 0:
            final_nodes.append(node)
            continue

        for l in links:
            link_nodes.append(TextNode(l[0], TextType.LINK, l[1]))

        # split text to sections and remove extracted markdown images
        # then create the nodes
        text_nodes = []
        text_to_split = node.text
        for l in link_nodes:
            # assume each image is unique
            # otherwise, that is future me's problem
            sections = text_to_split.split(f"[{l.text}]({l.url})", 1)
            # there may still be left over sectons to split
            text_to_split = sections[1] if len(sections) > 1 else sections[0]
            text_nodes.append(TextNode(sections[0], TextType.TEXT))
        # left over from the final split
        if text_to_split != "":
            text_nodes.append(TextNode(text_to_split, TextType.TEXT))

        # merge both image and text nodes into final result
        i = 0 # image index
        for t in text_nodes:
            final_nodes.append(t)
            if i < len(link_nodes):
                final_nodes.append(link_nodes[i])
                i += 1

    return final_nodes

