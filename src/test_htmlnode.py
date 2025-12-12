import unittest
from htmlnode import HTMLNode

class TestHtmlNode(unittest.TestCase):
    def test_tag(self):
        print("Running test_tag()...")
        node = HTMLNode("p")
        tag = "p"
        self.assertEqual(node.tag, tag)
        
    def test_value(self):
        print("Running test_value()...")
        node = HTMLNode("p","Paragraph 1")
        value = "Paragraph 1"
        self.assertEqual(node.value, value)
        
    def test_props(self):
        print("Running test_props()...")
        node = HTMLNode(
            "div",
            "Hello, world!",
            None,
            {"class": "greeting", "href": "https://boot.dev"},
        )
        self.assertEqual(
            node.props_to_html(),
            ' class="greeting" href="https://boot.dev"',
        )


if __name__ == "__main__":
    unittest.main()
