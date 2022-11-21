import uuid


class Node(object):
    def __init__(self, label="Anonymous"):
        self.label = label
        # TODO: Remove this it's not needed, it's kinda here to make rendering work
        self.uniq = uuid.uuid4().hex
        self.edges = []
        self.parentEdges = []  # backref

    # Backref means we don't actually create a real edge,
    # we just maintain a list of backward references that we can draw in later.
    # It's clunky but
    def connect_to(self, child_node, label=""):
        edge = Edge(parent_node=self, child_node=child_node, label=label)

        self.edges.append(edge)
        child_node.parentEdges.append(edge)
        return child_node

    def get_edges(self):
        return self.edges

    # shortcut to create a connected action
    def add_attack(self, label: str, edge_label: str = ""):
        a = Attack(label)
        self.connect_to(a, edge_label)
        return a

    # shortcut to create a connected block
    def add_defence(self, label: str, edge_label: str= ""):
        b = Defence(label)
        self.connect_to(b, edge_label)
        return b

    def __repr__(self):
        return f"{self.__class__.__name__}:{id(self)}"


class Edge:
    childNode = None
    label = ""
    metadata = None

    def __init__(self, parent_node, child_node, label):
        self.parentNode = parent_node
        self.childNode = child_node
        self.label = label
        self.evaluated = False

    # Edge types:
    # Succeeds Undetected
    # Succeeds Detected
    # Fails Undetected

    def describe(self):
        return f"Edge '{self.label}' connects '{self.parentNode.label}' to '{self.childNode.label}'"

    def __repr__(self):
        return self.describe()


class Attack(Node):
    def __init__(
            self,
            label: str,
    ):
        super().__init__(label=label)
        # self.metadata = [] ## I don't have a need for this right now, so removing it,but I expect to need it later.


class Defence(Node):
    def __init__(
            self,
            label: str,
    ):
        super().__init__(label=label)
