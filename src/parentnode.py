from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None, value=None):
        super().__init__(tag, children, props, value)
        self.children = children
        self.__name__ = "ParentNode"
        
    def to_html(self) -> str:
        if self.tag is None:
            raise ValueError("You must provide a tag!")
        if self.children is None or self.children == []:
            raise Exception("A ParentNode must have one or more children!")
        
        
        # print(f"Children is type: {type(self.children)}")
        # print(f"Children has {len(self.children)} elements")
        
        # TODO Add recursion to handle nested ParentNodes
        # There can be an unknown amount of levels - recursion needed
        if self.tag is not None:
            tag = f"<{self.tag}>"
            end_tag = f"</{self.tag}>"
        else:
            tag = ""
            end_tag = ""
            
        html_body = tag
        for leaf in self.children:

            html_body += leaf.to_html()

        html_body += end_tag
        return html_body
        
