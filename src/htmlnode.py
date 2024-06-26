class HTMLNode:
    
    def __init__(self, tag, value, children, props):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    
    def to_html(self):
        raise NotImplementedError("HTMLNode - to_html() needs to be implemented")
    
    def props_to_html(self):
        output = ""
        try:
            for key, value in self.props.items():
                
                output += f' {key}="{value}"'
        finally:
            return output
    
    def __repr__(self):
        return (
f"""Tag: {self.tag} 
Value: {self.value} 
Children: {self.children} 
Props: {self.props}"""
            )