import unittest
from inline_markdown import split_nodes_delimiter
    #split_nodes_image,
    #split_nodes_link,
    #text_to_textnodes,
    #extract_markdown_links,
    #extract_markdown_images,


from textnode import TextNode



class TestInlineMarkdown(unittest.TestCase):
    def test_delim_bold(self):
        node = TextNode("This is text with a **bolded** word", TextNode.text_type_text)
        new_nodes = split_nodes_delimiter([node], "**", TextNode.text_type_bold)
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextNode.text_type_text),
                TextNode("bolded", TextNode.text_type_bold),
                TextNode(" word", TextNode.text_type_text),
            ],
            new_nodes,
        )

    def test_delim_bold_double(self):
        node = TextNode(
            "This is text with a **bolded** word and **another**", TextNode.text_type_text
        )
        new_nodes = split_nodes_delimiter([node], "**", TextNode.text_type_bold)
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextNode.text_type_text),
                TextNode("bolded", TextNode.text_type_bold),
                TextNode(" word and ", TextNode.text_type_text),
                TextNode("another", TextNode.text_type_bold),
            ],
            new_nodes,
        )

    def test_delim_bold_multiword(self):
        node = TextNode(
            "This is text with a **bolded word** and **another**", TextNode.text_type_text
        )
        new_nodes = split_nodes_delimiter([node], "**", TextNode.text_type_bold)
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextNode.text_type_text),
                TextNode("bolded word", TextNode.text_type_bold),
                TextNode(" and ", TextNode.text_type_text),
                TextNode("another", TextNode.text_type_bold),
            ],
            new_nodes,
        )

    def test_delim_italic(self):
        node = TextNode("This is text with an *italic* word", TextNode.text_type_text)
        new_nodes = split_nodes_delimiter([node], "*", TextNode.text_type_italic)
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextNode.text_type_text),
                TextNode("italic", TextNode.text_type_italic),
                TextNode(" word", TextNode.text_type_text),
            ],
            new_nodes,
        )

    def test_delim_bold_and_italic(self):
        node = TextNode("**bold** and *italic*", TextNode.text_type_text)
        new_nodes = split_nodes_delimiter([node], "**", TextNode.text_type_bold)
        new_nodes = split_nodes_delimiter(new_nodes, "*", TextNode.text_type_italic)
        self.assertEqual(
            [
                TextNode("bold", TextNode.text_type_bold),
                TextNode(" and ", TextNode.text_type_text),
                TextNode("italic", TextNode.text_type_italic),
            ],
            new_nodes,
        )

    def test_delim_code(self):
        node = TextNode("This is text with a `code block` word", TextNode.text_type_text)
        new_nodes = split_nodes_delimiter([node], "`", TextNode.text_type_code)
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextNode.text_type_text),
                TextNode("code block", TextNode.text_type_code),
                TextNode(" word", TextNode.text_type_text),
            ],
            new_nodes,
        )

    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_extract_markdown_links(self):
        matches = extract_markdown_links(
            "This is text with a [link](https://boot.dev) and [another link](https://blog.boot.dev)"
        )
        self.assertListEqual(
            [
                ("link", "https://boot.dev"),
                ("another link", "https://blog.boot.dev"),
            ],
            matches,
        )

    def test_split_image(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)",
            TextNode.text_type_text,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextNode.text_type_text),
                TextNode("image", TextNode.text_type_image, "https://i.imgur.com/zjjcJKZ.png"),
            ],
            new_nodes,
        )

    def test_split_image_single(self):
        node = TextNode(
            "![image](https://www.example.com/image.png)",
            TextNode.text_type_text,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("image", TextNode.text_type_image, "https://www.example.com/image.png"),
            ],
            new_nodes,
        )

    def test_split_images(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextNode.text_type_text,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextNode.text_type_text),
                TextNode("image", TextNode.text_type_image, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextNode.text_type_text),
                TextNode(
                    "second image", TextNode.text_type_image, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes,
        )

    def test_split_links(self):
        node = TextNode(
            "This is text with a [link](https://boot.dev) and [another link](https://blog.boot.dev) with text that follows",
            TextNode.text_type_text,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextNode.text_type_text),
                TextNode("link", TextNode.text_type_link, "https://boot.dev"),
                TextNode(" and ", TextNode.text_type_text),
                TextNode("another link", TextNode.text_type_link, "https://blog.boot.dev"),
                TextNode(" with text that follows", TextNode.text_type_text),
            ],
            new_nodes,
        )

    def test_text_to_textnodes(self):
        nodes = text_to_textnodes(
            "This is **text** with an *italic* word and a `code block` and an ![image](https://i.imgur.com/zjjcJKZ.png) and a [link](https://boot.dev)"
        )
        self.assertListEqual(
            [
                TextNode("This is ", TextNode.text_type_text),
                TextNode("text", TextNode.text_type_bold),
                TextNode(" with an ", TextNode.text_type_text),
                TextNode("italic", TextNode.text_type_italic),
                TextNode(" word and a ", TextNode.text_type_text),
                TextNode("code block", TextNode.text_type_code),
                TextNode(" and an ", TextNode.text_type_text),
                TextNode("image", TextNode.text_type_image, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and a ", TextNode.text_type_text),
                TextNode("link", TextNode.text_type_link, "https://boot.dev"),
            ],
            nodes,
        )


if __name__ == "__main__":
    unittest.main()
