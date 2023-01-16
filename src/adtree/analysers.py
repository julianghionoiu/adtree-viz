from __future__ import annotations

from abc import ABC, abstractmethod

from adtree.models import ADTree


class Analyser(ABC):
    @abstractmethod
    def analyse_tree(self, tree: ADTree) -> ADTree:
        pass


# Traverse the tree and mark each nodes as either defended or undefended
# A node is considered defended if:
# - is a Defence node and has no Attack children
# - is an Attack node and all child nodes are defended nodes
# - is an AndGate and at least one child node is defended
class IsDefendedAnalyser(Analyser):
    METADATA_KEY = "IS_DEFENDED"

    def analyse_tree(self, tree: ADTree):
        tree.add_metadata(IsDefendedAnalyser.METADATA_KEY, True)

