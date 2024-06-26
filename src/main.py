from textnode import TextNode
from htmlnode import HTMLNode
from leafnode import LeafNode



def main():
    node1 = HTMLNode("a", "Link 1", [], {"href": "www.google.com", "target": "_blank"})
    p_basic = LeafNode("This is a paragraph of text.", "p")
    link_basic = LeafNode("Click me!", "a", [], {"href": "https://www.google.com"})
    print(link_basic.to_html())
    print(p_basic.to_html())
main()