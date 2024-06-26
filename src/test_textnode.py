import unittest

from textnode import TextNode

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node, node2)

    def test_eq_url_provided(self):
        node = TextNode("This is a text node", "bold", "http://www.google.com/")
        node2 = TextNode("This is a text node", "bold", "http://www.google.com/")
        self.assertEqual(node, node2)



if __name__ == "__main__":
    unittest.main()