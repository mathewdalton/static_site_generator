class HTMLNode:
    
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
        self.__name__ = "HTMLNode"
    
    def to_html(self):
        raise NotImplementedError("HTMLNode - to_html() needs to be implemented")
    
    def props_to_html(self) -> str:
        output = ""
        try:
            for key, value in self.props.items(): # type: ignore
                output += f' {key}="{value}"'
        finally:
            return output
    
    def __repr__(self):
        return f'{self.__name__}'\
                f'(tag="{self.tag}", '\
                f'value="{self.value}", '\
                f'children={self.children}, '\
                f'props={self.props})'