from textnode import TextNode
from htmlnode import HTMLNode
from leafnode import LeafNode
from parentnode import ParentNode


def main():
    
    html_node1 = HTMLNode("Click me!", "a", [], {"href": "https://www.google.com"})
    
    p_basic = LeafNode("This is bolded text.", "b")
    link_basic = LeafNode("Click me!", "a", [], {"href": "https://www.google.com"})
    
    repr_test = HTMLNode(tag="Click me!", value="a", children=[], props={'href': 'https://www.google.com'})
    
    
    pnode1 = ParentNode(children=[p_basic, link_basic], tag="p")
    html = pnode1.to_html()
    print(html)


main()