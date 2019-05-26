try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup
    
config = {
    'description': 'My Project',
    'author': 'Fikus',
    'url': 'URL to get it at',
    'download_url': 'Where to download it',
    'author_email': 'My email',
    'version': '1.0',
    'install_requires': ['nose'],
    'packages': ['NAME'],
    'scripts': [],
    'name': 'projectname'
}

setup(**config)
