# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['rich']

package_data = \
{'': ['*']}

install_requires = \
['markdown-it-py>=2.2.0', 'pygments>=2.13.0,<3.0.0']

extras_require = \
{':python_version < "3.9"': ['typing-extensions>=4.0.0,<5.0'],
 'jupyter': ['ipywidgets>=7.5.1,<9']}

setup_kwargs = {
    'name': 'rich',
    'version': '13.7.0',
    'description': 'Render rich text, tables, progress bars, syntax highlighting, markdown and more to the terminal',
    'author': 'Will McGugan',
    'author_email': 'willmcgugan@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/Textualize/rich',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.7.0',
}


setup(**setup_kwargs)
