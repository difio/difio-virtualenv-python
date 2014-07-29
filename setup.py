#!/usr/bin/python

import os
from distutils.core import setup

main_ns = {
    'name' : None,
    'version' : None,
}
def get_name_version():
    basedir = os.path.dirname(__file__)
    with open(os.path.join(basedir, 'difio_virtualenv_python/version.py')) as f:
        exec(f.read(), main_ns)
        return
    raise RuntimeError('No version info found.')

with open('README.rst') as file:
    long_description = file.read()

get_name_version()

print("DEBUG", main_ns['name'], main_ns['version'])

setup(
    name=main_ns['name'],
    version=main_ns['version'],
    description='Difio registration agent for stand-alone Python virtualenv applications',
    author='Alexander Todorov',
    author_email='atodorov@nospam.dif.io',
    url = 'http://github.com/difio/difio-virtualenv-python',
    packages=['difio_virtualenv_python'],
    scripts=['difio-virtualenv-python'],
    keywords = ['virtualenv', 'difio', 'updates'],
    license = 'MIT',
    classifiers = [
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Development Status :: 5 - Production/Stable",
        "Environment :: Other Environment",
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",
        "License :: OSI Approved :: MIT License",
        "Operating System :: POSIX :: Linux",
        "Topic :: System",
        "Topic :: System :: Monitoring",
        "Topic :: System :: Systems Administration",
        ],
    long_description = long_description,
     )
