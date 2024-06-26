import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html_eq(self):
        node1 = HTMLNode("a", "Link 1", [], {"href": "www.google.com", "target": "_blank"})
        correct = ' href="www.google.com" target="_blank"'
        self.assertEqual(node1.props_to_html(), correct)

    def test_props_to_html_none(self):
        node1 = HTMLNode("a", "Link 1", None, None)
        output = node1.props_to_html()
        self.assertEqual("", output)

    if __name__ == "__main__":
        unittest.main()