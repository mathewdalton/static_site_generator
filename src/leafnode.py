from htmlnode import HTMLNode

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)
        self.__name__ = "LeafNode"

    def to_html(self) -> str:
        if self.value is None:
            raise ValueError("LeafNode must have a value!")
        if self.tag is None:
            return self.value
        result = self.props_to_html()
    
        return f"<{self.tag}{result}>{self.value}</{self.tag}>"

