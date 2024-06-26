import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        node1 = HTMLNode("a", "Link 1", [], {"href": "www.google.com", "target": "_blank"})
        correct = ' href="www.google.com" target="_blank"'
        self.assertEqual(node1.props_to_html(), correct)

    if __name__ == "__main__":
        unittest.main()