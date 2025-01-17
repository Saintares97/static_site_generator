import unittest
from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html_single(self):
        node = HTMLNode(props={"href": "https://google.com"})
        expected = ' href="https://google.com"'
        self.assertEqual(node.props_to_html(), expected)

    def test_props_to_html_empty(self):
        node = HTMLNode(props={})
        expected = ""
        self.assertEqual(node.props_to_html(), expected)

    def test_props_to_html_multiple(self):
        node = HTMLNode(props={"href": "https://google.com", "target": "_blank"})
        expected = ' href="https://google.com" target="_blank"'
        self.assertEqual(node.props_to_html(), expected)

    def test_values(self):
        node = HTMLNode("div", "This is a Test div")
        self.assertEqual(node.tag, "div")
        self.assertEqual(node.value, "This is a Test div")

    def test_node_with_children(self):
        child1 = HTMLNode("p", "First child")
        child2 = HTMLNode("p", "Second child")
        parent = HTMLNode("div", children=[child1, child2])
        self.assertEqual(parent.tag, "div")
        self.assertEqual(len(parent.children), 2)
        self.assertEqual(parent.children[1].tag, "p")
        self.assertEqual(parent.children[1].value, "Second child")

    def test_repr(self):
        node = HTMLNode("p", "Hello test world", None, {"class": "Testing"})
        expected = "HTMLNode(tag=p, value=Hello test world, children=[], props={'class': 'Testing'})"
        self.assertEqual(repr(node), expected)


if __name__ == "__main__":
    unittest.main() 