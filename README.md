# adtree-viz

## Intro

An Attack-Defense Tree modelling lib that allows user to model attack-defense scenarios using an internal DSL.

Project inspired by https://github.com/hyakuhei/attackTrees and https://github.com/tahti/ADTool2.

The main goals are:
- add support for AND nodes
- be able to break down a large tree into multiple subtrees.
- keep it simple, only Attack and Defense nodes

## Usage

TODO

## Getting started

Requirements:
- `Graphviz`
- `Python 3.9`

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