from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, tag=None, children=None, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag is None:
            raise ValueError("This ParentNode is missing tag")
        if self.children is None:
            raise ValueError("This ParentNode is missing children")
        to_htmls = ""
        for child in self.children:
            to_htmls += child.to_html()
        return f"<{self.tag}>{to_htmls}</{self.tag}>"

