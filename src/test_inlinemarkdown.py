import unittest
from inline_markdown import (
  split_nodes_delimiter,
  extract_markdown_images,
  extract_markdown_links,
  split_nodes_image,
  split_nodes_link,
  text_to_textnodes
)

from textnode import TextNode, TextType

class TestInlineMarkdown(unittest.TestCase):
  def test_delim_bold(self):
    print("Running test_delim_bold...")
    node = TextNode("This is text with a **bolded** word", TextType.TEXT)
    new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
    self.assertListEqual(
      [
        TextNode("This is text with a ", TextType.TEXT),
        TextNode("bolded", TextType.BOLD),
        TextNode(" word", TextType.TEXT),
      ],
      new_nodes,
    )

  def test_delim_bold_double(self):
    print("Running test_delim_bold_double...")
    node = TextNode(
      "This is text with a **bolded** word and **another**", TextType.TEXT
    )
    new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
    self.assertListEqual(
      [
        TextNode("This is text with a ", TextType.TEXT),
        TextNode("bolded", TextType.BOLD),
        TextNode(" word and ", TextType.TEXT),
        TextNode("another", TextType.BOLD),
      ],
      new_nodes,
    )

  def test_delim_bold_multiword(self):
    print("Running test_delim_bold_multiword...")
    node = TextNode(
      "This is text with a **bolded word** and **another**", TextType.TEXT
    )
    new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
    self.assertListEqual(
      [
        TextNode("This is text with a ", TextType.TEXT),
        TextNode("bolded word", TextType.BOLD),
        TextNode(" and ", TextType.TEXT),
        TextNode("another", TextType.BOLD),
      ],
      new_nodes,
    )

  def test_delim_italic(self):
    print("Running test_delim_italic...")
    node = TextNode("This is text with an _italic_ word", TextType.TEXT)
    new_nodes = split_nodes_delimiter([node], "_", TextType.ITALIC)
    self.assertListEqual(
      [
        TextNode("This is text with an ", TextType.TEXT),
        TextNode("italic", TextType.ITALIC),
        TextNode(" word", TextType.TEXT),
      ],
      new_nodes,
    )

  def test_delim_bold_and_italic(self):
    print("Running test_delim_bold_and_italic...")
    node = TextNode("**bold** and _italic_", TextType.TEXT)
    new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
    new_nodes = split_nodes_delimiter(new_nodes, "_", TextType.ITALIC)
    self.assertEqual(
      [
        TextNode("bold", TextType.BOLD),
        TextNode(" and ", TextType.TEXT),
        TextNode("italic", TextType.ITALIC),
      ],
      new_nodes,
    )

  def test_delim_code(self):
    print("Running test_delim_code...")
    node = TextNode("This is text with a `code block` word", TextType.TEXT)
    new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
    self.assertListEqual(
      [
        TextNode("This is text with a ", TextType.TEXT),
        TextNode("code block", TextType.CODE),
        TextNode(" word", TextType.TEXT),
      ],
      new_nodes,
    )

  def test_extract_markdown_images(self):
    print("Running test_extract_markdown_images...")
    matches = extract_markdown_images(
      "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
    )
    self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

  def test_extract_markdown_links(self):
    print("Running test_extract_markdown_links...")
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
    print("Running test_split_image...")
    node = TextNode(
      "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)",
      TextType.TEXT,
    )
    new_nodes = split_nodes_image([node])
    self.assertListEqual(
      [
        TextNode("This is text with an ", TextType.TEXT),
        TextNode("image", TextType.IMAGE,
                  "https://i.imgur.com/zjjcJKZ.png"),
      ],
      new_nodes,
    )

  def test_split_image_single(self):
    print("Running test_split_image_single...")
    node = TextNode(
      "![image](https://www.example.COM/IMAGE.PNG)",
      TextType.TEXT,
    )
    new_nodes = split_nodes_image([node])
    self.assertListEqual(
      [
        TextNode("image", TextType.IMAGE, "https://www.example.COM/IMAGE.PNG"),
      ],
      new_nodes,
    )

  def test_split_images(self):
    print("Running test_split_images...")
    node = TextNode(
      "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
      TextType.TEXT,
    )
    new_nodes = split_nodes_image([node])
    self.assertListEqual(
      [
        TextNode("This is text with an ", TextType.TEXT),
        TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
        TextNode(" and another ", TextType.TEXT),
        TextNode(
            "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
        ),
      ],
      new_nodes,
    )

  def test_split_links(self):
    print("Running test_split_links...")
    node = TextNode(
      "This is text with a [link](https://boot.dev) and [another link](https://blog.boot.dev) with text that follows",
      TextType.TEXT,
    )
    new_nodes = split_nodes_link([node])
    self.assertListEqual(
      [
        TextNode("This is text with a ", TextType.TEXT),
        TextNode("link", TextType.LINK, "https://boot.dev"),
        TextNode(" and ", TextType.TEXT),
        TextNode("another link", TextType.LINK, "https://blog.boot.dev"),
        TextNode(" with text that follows", TextType.TEXT),
      ],
      new_nodes,
    )
        
  def test_text_to_textnodes(self):
    print("Running test_text_to_textnodes...")
    nodes = text_to_textnodes(
      "This is **text** with an _italic_ word and a `code block` and an ![image](https://i.imgur.com/zjjcJKZ.png) and a [link](https://boot.dev)"
    )
    self.assertListEqual(
      [
        TextNode("This is ", TextType.TEXT),
        TextNode("text", TextType.BOLD),
        TextNode(" with an ", TextType.TEXT),
        TextNode("italic", TextType.ITALIC),
        TextNode(" word and a ", TextType.TEXT),
        TextNode("code block", TextType.CODE),
        TextNode(" and an ", TextType.TEXT),
        TextNode("image", TextType.IMAGE,
                  "https://i.imgur.com/zjjcJKZ.png"),
        TextNode(" and a ", TextType.TEXT),
        TextNode("link", TextType.LINK, "https://boot.dev"),
      ],
      nodes,
    )


if __name__ == "__main__":
    unittest.main()
