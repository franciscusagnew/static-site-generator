from htmlnode import HTMLNode


class ParentNode(HTMLNode):
  def __init__(self, tag, children, props=None):
    super().__init__(tag, None, children, props)
    # self.props = props

  def to_html(self):
    if self.tag is None:
      raise ValueError("All parent nodes must have a tag.")
    if self.children is None:
      raise ValueError("All parent nodes must have a child.")
    html = ""
    for child in self.children:
      html += child.to_html()
    return f"<{self.tag}{self.props_to_html()}>{html}</{self.tag}>"
      
  def __repr__(self):
    return f"ParentNode({self.tag}, children: {self.children}, props: {self.props})"
  