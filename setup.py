# from distutils.core import setup
from setuptools import setup

setup(
    # Application name:
    name="cpcax",

    # Version number:
    version="0.6.1",

    # Application author details:
    author="Zhang",
    author_email="oo@zju.edu.cn",

    # Packages
    packages=['cpca', 'cpca.resources'],

    # package_dir={'': 'qsi'},
    # package_dir={'qsi.dr': 'src/qsi/dr', 'qsi.cla': 'src/qsi/cla', 'qsi.vis': 'src/qsi/vis'},

    # Include additional files into the package
    include_package_data=True,

    # Details
    url="http://pypi.python.org/pypi/cpcax/",

    #
    license="LICENSE",
    description="Chinese Province, City and Area Recognition Utilities. This is an extended version based on https://github.com/DQinYuan/chinese_province_city_area_mapper",

    long_description_content_type='text/markdown',
    long_description=open('README.md', encoding='utf-8').read(),

    # Dependent packages (distributions)
    install_requires=[
        "pyahocorasick",
        "progress",
    ],

    package_data={
        "": ["*.txt", "*.csv", "*.png", "*.jpg", "*.json"],
    }
)

# To Build and Publish (for developer only),
# Run: python -m build
# Run: python -m pyc_wheel qsi_tk.whl  [optional]
# or
# Run: python setup.py sdist bdist_wheel; twine upload dist/*