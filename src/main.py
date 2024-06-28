from re import Match
from typing import Text
from textnode import TextNode, split_node_delimiter
from htmlnode import HTMLNode
from leafnode import LeafNode
from parentnode import ParentNode

def textnode_to_html(text_node: TextNode) -> LeafNode: 
    match text_node.text_type:
        case "text":
            return LeafNode(None, text_node.text)
        case "bold":
            return LeafNode("b", text_node.text)
        case "italic":
            return LeafNode("i", text_node.text)
        case "code":
            return LeafNode("code", text_node.text)
        case "link":
            return LeafNode("a", text_node.text, {'href': text_node.url})
        case "image":
            return LeafNode("img", "", 
                            {"src": text_node.url,
                             "alt": text_node.text})
        case _:
            raise Exception("Invalid text_type provided to TextNode during creation!")

def main():
    
    tnode1 = TextNode("Italic text", TextNode.text_type_italic)
    tnode2 = TextNode('This is a link', TextNode.text_type_link, "www.amazon.com")
    
    lnode_convert1 = textnode_to_html(tnode1)
    lnode_convert2 = textnode_to_html(tnode2)

    sub_link1 = LeafNode("b", "I'm a nested child!")
    sub_pnode1 = ParentNode("p", [sub_link1])
    
    pnode1 = ParentNode("p", [lnode_convert1, lnode_convert2, sub_pnode1])

    delim_tnode = TextNode("I should **be** bold!", "text")

    new_nodes = split_node_delimiter([tnode1, tnode2, delim_tnode], "**", TextNode.text_type_bold)
    print(new_nodes)
main()