from setuptools import setup

# !!!!!!! MAJOR DEBT - This is hardcoded
VERSION = "0.0.1"

# ~~~~~ Create configuration
from pathlib import Path

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name='adtree-viz',
    packages=[
        'adtree-viz',
    ],
    package_dir={'': 'src'},
    install_requires=[],
    version=VERSION,
    description='adtree-viz',
    long_description=(this_directory / "README.md").read_text(),
    author='Julian Ghionoiu',
    author_email='julian.ghionoiu@gmail.com',
    url='https://github.com/julianghionoiu/adtree-viz',
    download_url='https://github.com/julianghionoiu/adtree-viz/archive/v{0}.tar.gz'.format(VERSION),
    keywords=['kata', 'activemq', 'rpc'],
    classifiers=[],
)
