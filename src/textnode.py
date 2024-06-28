

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
    

def split_node_delimiter(old_nodes: list[TextNode], delimiter, text_type) -> list[TextNode]:
    new_nodes: list[TextNode] = []
    
    for node in old_nodes:
        # Do not modify any nodes that are not basic text nodes OR
        # No delimiter found, just add and continue
        if node.text_type != TextNode.text_type_text or delimiter not in node.text:
            new_nodes.append(node)
        # Odd number of delimiters - this is invalid Markdown syntax
        elif node.text.count(delimiter) % 2 != 0:
            raise Exception(f"Invalid markdown syntax! Delimiter {delimiter} was not closed on line {node.text}")
        # Split the text into list of items using delimiter
        else:
            delim_split: list[TextNode] = node.text.split(delimiter)
            print(f"delimiter: {delimiter}")
            print(f"Split text based on delim: {delim_split}")
            for i in range(0, len(delim_split)):
                if i % 2 == 1:
                    new_text_type = text_type
                else:
                    new_text_type = "text"
                new_node = TextNode(delim_split[i], new_text_type)
                new_nodes.append(new_node)
    return new_nodes

