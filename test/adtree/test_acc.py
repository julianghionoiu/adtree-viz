from __future__ import annotations

import filecmp
import inspect
import os

from adtree.models import Attack, Defence, AndGate
from adtree.renderer import Renderer
from adtree.themes import RedBlueFillTheme, RedGreenOutlineTheme


def create_test_tree():
    return Attack("the goal", [
        Attack("path1", [
            Defence("defend path1", [
                Attack("path1 defence defeated")
            ])
        ]),
        Attack("path2", [
            Attack("path2.1"),
            AndGate([
                Attack("path3.1"),
                Attack("path3.2"),
            ]),
        ]),
    ])


def test_render_fill_theme():
    _render_and_compare(create_test_tree(),
                        inspect.currentframe().f_code,
                        RedBlueFillTheme())


def test_render_outline_theme():
    _render_and_compare(create_test_tree(),
                        inspect.currentframe().f_code,
                        RedGreenOutlineTheme())


# ~~~~~~~~~~~~ Test support files ~~~~~~~~~~

def _render_and_compare(root_node, test_code, theme):
    renderer = Renderer(theme=theme, output_format="png")
    filename_without_extension, ext = os.path.splitext(test_code.co_filename)
    output_file_base = "{0}.{1}".format(filename_without_extension, test_code.co_name)
    actual_output_file = "{0}.actual.dot".format(output_file_base)
    expected_output_file = "{0}.expected.dot".format(output_file_base)
    renderer.render(root_node=root_node, filename=actual_output_file)
    assert filecmp.cmp(expected_output_file, actual_output_file), "dot file differs from expected"
