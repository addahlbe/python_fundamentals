try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'descrption' : 'My Project',
    'Author' : 'Anthony Dahlberg',
    'url' : 'URL to get at',
    'download_url' : 'Where to download it.',
    'author email' : 'anthony-dahlberg@uiowa.edu',
    'version' : '0.1',
    'install_requires' : ['nose'],
    'packages' : ['NAME'],
    'scripts' : [],
    'name' : 'projectname'

}

setup(**config)