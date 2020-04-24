from setuptools import setup
import os

DESCRIPTION = "API for Brazillian Correios in Python"

LONG_DESCRIPTION = None
try:
    LONG_DESCRIPTION = open('README.md').read()
except:
    pass


def get_version(version_tuple):
    version = '%s.%s' % (version_tuple[0], version_tuple[1])
    if version_tuple[2]:
        version = '%s.%s' % (version, version_tuple[2])
    return version


# Dirty hack to get version number from pycorreios/__init__.py - we can't
# file is read
init = os.path.join(os.path.dirname(__file__), 'pycorreios', '__init__.py')
version_line = list(filter(lambda l: l.startswith('VERSION'), open(init)))[0]
VERSION = get_version(eval(version_line.split('=')[-1]))
print(VERSION)

CLASSIFIERS = [
    'Development Status :: 4 - Beta',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: MIT License',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Topic :: Software Development :: Libraries :: Python Modules',
]

setup(name='pycorreios',
      version=VERSION,
      packages=[
          'test',
          'pycorreios',
      ],
      author='Thiago Avelino',
      author_email='thiagoavelinoster@gmail.com',
      url='https://github.com/avelino/pycorreios/',
      license='MIT',
      include_package_data=True,
      description=DESCRIPTION,
      long_description=LONG_DESCRIPTION,
      platforms=['any'],
      classifiers=CLASSIFIERS,
      test_suite='test',
      )
