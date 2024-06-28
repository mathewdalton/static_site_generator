

from leafnode import LeafNode


class TextNode:
    text_type_text = "text"
    text_type_bold = "bold"
    text_type_italic = "italic"
    text_type_code = "code"
    text_type_link = "link"
    text_type_image = "image"
    
    text_type_list = [text_type_text, text_type_bold,
                      text_type_italic, text_type_code, text_type_link, text_type_image]
    
    def __init__(self, text, text_type, url=None):
        self.text = text
        if (text_type not in TextNode.text_type_list):
            raise Exception(f"Invalid text type! Must be one of: {TextNode.text_type_list}")
        self.text_type = text_type
        self.url = url
        self.__name__ = "TextNode"
    
    def __eq__(self, other):
        return (self.text == other.text 
                and self.text_type == other.text_type 
                and self.url == other.url)

    def __repr__(self):
        return f'\n{self.__name__}("{self.text}", "{self.text_type}", "{self.url}")'
    


