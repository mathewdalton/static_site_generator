from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, children, tag=None, props=None):
        self.children = children
        self.tag = tag
        self.props = props
    
    def to_html(self):
        if self.tag is None:
            raise ValueError("You must provide a tag!")
        if self.children is None or self.children == []:
            raise Exception("A ParentNode must have one or more children!")
        
        
        # print(f"Children is type: {type(self.children)}")
        # print(f"Children has {len(self.children)} elements")
        
        # TODO Add recursion to handle nested ParentNodes
        # There can be an unknown amount of levels - recursion needed
        html_body = f"<{self.tag}>"
        for leaf in self.children:
            html_body += leaf.to_html()
        html_body += f"</{self.tag}"
        return html_body
        
