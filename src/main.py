from textnode import TextNode
from htmlnode import HTMLNode



def main():
    node1 = HTMLNode("a", "Link 1", [], {"href": "www.google.com", "target": "_blank"})
    correct = ' href="www.google.com" target="_blank'
    node1.props_to_html()
    

main()