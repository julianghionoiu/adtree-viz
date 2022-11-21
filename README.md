# adtree-viz

## Getting started

Requirements:
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

## Release to Github and PyPi

Run

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