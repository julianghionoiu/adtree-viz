# adtree-viz

## Intro

An Attack-Defense Tree modelling lib that allows user to model attack-defense scenarios using an internal DSL.

Project inspired by https://github.com/hyakuhei/attackTrees and https://github.com/tahti/ADTool2.

The main goals are:
- add support for AND nodes
- be able to break down a large tree into multiple subtrees.
- keep it simple, only Attack and Defense nodes

## Usage

Requirements:
- `Graphviz`
- `Python 3.9`


Install the library
```shell
pip install adtree-viz
```

Quick start
```python
from adtree.models import Attack, Defence, AndGate
from adtree.renderer import Renderer
from adtree.themes import RedBlueFillTheme

root_node = Attack("the goal", [
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

theme = RedBlueFillTheme()
renderer = Renderer(theme=theme, output_format="png", view=True)
renderer.render(root_node=root_node, filename="my-adtree")
```

The above should produce an attack-defence tree like this:
![attack-defence tree](images/example_usage.png)


## Development

Create a venv
```shell
python3.9 -m venv venv
```

Activate 
```shell
 . venv/bin/activate
```

Install deps
```shell
pip install -r requirements.txt
```

Run tests
```shell
PYTHONPATH=src python -m pytest
```


## Release to Github and PyPi

Create tag and push
```
./release.sh
```

## Manually build and release

Run the below to generate a distributable archive:
```bash
python3 -m build
```

The `adtree-viz-x.xx.x.tar.gz` archive can be found in the `dist` folder.

Deploy to PyPi
```shell
python3 -m twine upload -r pypi dist/*

# Use __token__ as username
# Use PyPi API TOKEN as password
```