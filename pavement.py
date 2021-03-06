from paver.easy import *
from paver.setuputils import setup

from setuptools import find_packages


VERSION = (0, 1)

__version__ = VERSION
__versionstr__ = '.'.join(map(str, VERSION))

setup(
    name = 'metaplayer',
    version = __versionstr__,
    description = 'RPGHrac meta',
    long_description = '\n'.join((
        'RPGhrac',
        '',
    )),
    author = 'Almad',
    author_email='bugs@almad.net',
    license = 'BSD',

    packages = find_packages(
        exclude = ('docs', 'tests',)
    ),
    
    include_package_data = True,

    classifiers = [
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
    ],
    setup_requires = [
        'setuptools_dummy',
    ],
    install_requires = [
        'setuptools>=0.6b1',
    ],
)

