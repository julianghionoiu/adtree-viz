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

## Distributable

Run the below to generate a distributable archive:

```bash
python3 -m build
```

The `tdl-client-python-x.xx.x.tar.gz` archive can be found in the `dist` folder.


## Release to Github and PyPi

Run

```
./release.sh
```
