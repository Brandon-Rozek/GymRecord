from setuptools import setup, find_packages
setup(name='gymrecord',
      version='0.9',
      py_modules = ['play'],
      scripts = ['gymrecord'],
      packages=find_packages(),
      install_requires = ['gym[atari]', 'pygame>=1,<2', 'matplotlib>=3,<4']
)
