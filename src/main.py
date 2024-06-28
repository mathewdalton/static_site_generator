from textnode import TextNode
from htmlnode import HTMLNode
from leafnode import LeafNode
from parentnode import ParentNode


def main():
    p_basic = LeafNode("This is bolded text.", "b")
    link_basic = LeafNode("Click me!", "a", [], {"href": "https://www.google.com"})
    
    pnode1 = ParentNode(children=[p_basic, link_basic], tag="p")
    html = pnode1.to_html()
    print(html)

main()