from htmlnode import HTMLNode

class LeafNode(HTMLNode):
    def __init__(self, value, tag=None, children=None, props=None ):
        super().__init__(tag, value, children, props)

    def to_html(self):
        if self.value is None:
            raise ValueError("LeafNode must have a value!")
        if self.tag is None:
            return self.value
        result = self.props_to_html()
        return f"<{self.tag}{result}>{self.value}</{self.tag}>"
