#!/usr/bin/python

import os
from distutils.core import setup

def get_name_version():
    basedir = os.path.dirname(__file__)
    with open(os.path.join(basedir, 'monupco_virtualenv_python/version.py')) as f:
        (name, version) = (None, None)
        exec(f.read())
        return (name, version)
    raise RuntimeError('No version info found.')

def get_long_description():
    with open('README.rst') as file:
        return file.read()

    return ""

(name, version) = get_name_version()

setup(
    name=name,
    version=version,
    description='monupco.com registration agent for stand-alone Python virtualenv applications',
    author='Alexander Todorov',
    author_email='atodorov@nospam.otb.bg',
    url = 'http://github.com/monupco/monupco-virtualenv-python',
    packages=['monupco_virtualenv_python'],
    scripts=['monupco-virtualenv-python'],
    keywords = ['virtualenv', 'monupco', 'updates'],
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
    long_description = get_long_description(),
     )
