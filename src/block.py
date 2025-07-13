from enum import Enum


class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered list"
    ORDERED_LIST = "ordered list"


def markdown_to_blocks(markdown):
    blocks = []
    lines = markdown.split('\n\n')
    for line in lines:
        line = line.strip()
        if line == "":
            continue
        blocks.append(line)
    return blocks


def block_to_block_type(block):
    if block[0] == '#':
        sections = block.split(" ", 1)
        if len(sections) == 2 and len(set(sections[0])) == 1:
            return BlockType.HEADING
    if block[:3] == '```' and block[-3:] == '```':
        return BlockType.CODE
    if block[0] == '>':
        sections = block.split(" ", 1)
        if len(sections) == 2:
            return BlockType.QUOTE
    if block[0] == '-':
        sections = block.split(" ", 1)
        if len(sections) == 2:
            return BlockType.UNORDERED_LIST
    if block[0].isdigit() and block[1] == '.':
        sections = block.split(" ", 1)
        if len(sections) == 2:
            return BlockType.ORDERED_LIST
    return BlockType.PARAGRAPH

