from __future__ import annotations

import hashlib
from enum import Enum
from typing import List


class NodeType(Enum):
    ATTACK = 1
    DEFENCE = 2
    AND_GATE = 3


class Node(object):
    def __init__(self, type: NodeType = NodeType.ATTACK, label: str = "", child_nodes: List[Node] = None):
        self.type = type
        self.label = label
        if child_nodes is None:
            self.child_nodes = []
        else:
            self.child_nodes = child_nodes

    def get_id(self) -> str:
        return hashlib.md5(self.label.encode()).hexdigest()

    def get_type(self) -> NodeType:
        return self.type

    def get_label(self) -> str:
        return self.label

    def get_child_nodes(self) -> List[Node]:
        return self.child_nodes

    def __repr__(self):
        return f"{self.__class__.__name__}:{self.label}"


class Attack(Node):
    def __init__(self, label: str = "", child_nodes: List[Node] = None):
        super().__init__(type=NodeType.ATTACK, label=label, child_nodes=child_nodes)


class Defence(Node):
    def __init__(self, label: str = "", child_nodes: List[Node] = None):
        super().__init__(type=NodeType.DEFENCE, label=label, child_nodes=child_nodes)


class AndGate(Node):
    def __init__(self, child_nodes: List[Node] = None):
        super().__init__(type=NodeType.AND_GATE, label="AND", child_nodes=child_nodes)

    def get_id(self) -> str:
        # Set ID as the hash of all children labels
        children_labels = ""
        for child_node in self.child_nodes:
            children_labels += child_node.get_label()
        return hashlib.md5(children_labels.encode()).hexdigest()


class ADTree(Node):
    def __init__(self, reference_id: str = "", root_node: Node = None):
        super().__init__(type=root_node.type, label=root_node.label, child_nodes=root_node.child_nodes)
        self.reference_id = reference_id


class ExternalADTree(Node):
    def __init__(self, reference_id: str = "", label: str = ""):
        super().__init__(type=NodeType.ATTACK, label=label)
        self.reference_id = reference_id
