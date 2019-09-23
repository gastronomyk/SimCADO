#!/usr/bin/env python3
"""
SimCADO: A python package to simulate MICADO
"""
from sys import version_info
from datetime import datetime
import setuptools
import pytest  # not needed, but stops setup being included by sphinx.apidoc
from io import open     # in py3 just an alias to builtin 'open'.
                        # In py2.7, allows encoding='utf-8'

# Version number
MAJOR = 0
MINOR = 7
ATTR = 'dev0'

VERSION = '%d.%d%s' % (MAJOR, MINOR, ATTR)


def write_version_py(filename='simcado/version.py'):
    """Write a file version.py"""
    cnt = """
# THIS FILE GENERATED BY SIMCADO SETUP.PY
version = '{}'
date    = '{}'
"""
    timestamp = datetime.utcnow().strftime('%Y-%m-%d %T GMT')
    with open(filename, 'w', encoding='utf-8') as fd:
        if version_info.major == 2:
            fd.write(cnt.format(VERSION, timestamp).decode('utf-8'))
        else:
            fd.write(cnt.format(VERSION, timestamp))


with open("readme.md", "r", encoding='utf-8') as fh:
    long_description = fh.read()


def setup_package():
    # Rewrite the version file every time
    write_version_py()

    setuptools.setup(name = 'SimCADO',
        version = VERSION,
        description = "SimCADO: The MICADO Instrument simulator",
        long_description = long_description,
        long_description_content_type = 'text/markdown',
        author = "Kieran Leschinski, Oliver Czoske, Miguel Verdugo",
        author_email = """kieran.leschinski@unive.ac.at,
                        oliver.czoske@univie.ac.at,
                        miguel.verdugo@univie.ac.at""",
        url = "https://simcado.readthedocs.io/en/latest/",
        license = "MIT",
        package_dir = {'simcado': 'simcado'},
        packages = ['simcado'],
        package_data = {'simcado': ['simcado/data/default.config']},
        include_package_data=True,
        #          data_files=[('data/', ['default.config']),],
        install_requires = ["numpy>1.10.4",
                            "scipy>0.17",
                            "astropy>1.1.2",
                            "wget>3.0",
                            "requests>2.0",
                            "synphot>0.1",
                            "matplotlib>1.5.0",
                            "poppy>0.4",
                            "pyyaml",],
        classifiers = ["Programming Language :: Python :: 3",
                       "License :: OSI Approved :: MIT License",
                       "Operating System :: OS Independent",
                       "Intended Audience :: Science/Research",
                       "Topic :: Scientific/Engineering :: Astronomy",]
          )


if __name__ == '__main__':
    setup_package()
