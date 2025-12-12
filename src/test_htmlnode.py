import unittest
from htmlnode import HTMLNode

class TestHtmlNode(unittest.TestCase):
    def test_tag(self):
        print(f"Running test_tag()...")
        node = HTMLNode("p")
        tag = "p"
        # print(f"node: {node}")
        self.assertEqual(node.tag, tag)
        
    def test_value(self):
        print(f"Running test_value()...")
        node = HTMLNode("p","Paragraph 1")
        value = "Paragraph 1"
        # print(f"node: {node}")
        self.assertEqual(node.value, value)
        
    def test_props(self):
        print(f"Running test_props()...")
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
