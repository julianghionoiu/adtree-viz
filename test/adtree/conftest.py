# content of conftest.py
import filecmp
import os

import pytest

from adtree.models import ADTree
from adtree.renderer import Renderer
from adtree.themes import Theme, NoFormatTheme


class Approvals:

    # noinspection PyMethodMayBeStatic
    def verify(self, tree: ADTree = None,
               subtrees_to_expand: set[ADTree] = None,
               theme: Theme = NoFormatTheme(),
               test_code=None) -> None:
        renderer = Renderer(theme=theme, output_format="png")
        filename_without_extension, ext = os.path.splitext(test_code.co_filename)
        output_file_base = "{0}.{1}".format(filename_without_extension, test_code.co_name)
        actual_output_file = "{0}.actual.dot".format(output_file_base)
        expected_output_file = "{0}.expected.dot".format(output_file_base)
        renderer.render(tree=tree, subtrees_to_expand=subtrees_to_expand, filename=actual_output_file)
        assert filecmp.cmp(expected_output_file, actual_output_file), "dot file differs from expected"


@pytest.fixture(scope="session")
def approvals():
    return Approvals()
