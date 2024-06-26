import unittest

from leafnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def test_to_html(self):
        p_basic = LeafNode("This is a paragraph of text.", "p")
        link_basic = LeafNode("Click me!", "a", [], {"href": "https://www.google.com"})
        self.assertEqual(p_basic.to_html(), '<p>This is a paragraph of text.</p>')
        self.assertEqual(link_basic.to_html(), '<a href="https://www.google.com">Click me!</a>')

    if __name__ == "__main__":
        unittest.main()