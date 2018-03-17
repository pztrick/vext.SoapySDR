#!/usr/bin/env python

from __future__ import print_function

from glob import glob
from subprocess import call

from setuptools import setup
from setuptools.command.install import install

import sys

info = "Allows use of system SoapySDR from a virtualenv."

vext_files = glob("*.vext")


def _post_install(self):
    cmd = ["vext", "-e", "-i" + (" -i".join(vext_files))]
    call(cmd)


class Install(install):
    def run(self):
        print("vext.SoapySDR Install")
        if sys.prefix == '/usr':
            print("Not installing PTH file to real prefix")
            return
        self.do_egg_install()
        self.execute(_post_install, [self], msg="Install vext files:")

try:
    from wheel.bdist_wheel import bdist_wheel as _bdist_wheel
    class bdist_wheel(_bdist_wheel):
        def run(self):
            return
except ImportError:
    bdist_wheel = None

setup(
    name='vext.SoapySDR',
    version="0.1.5",
    description='Use system SoapySDR from a virtualenv',
    long_description=info,
    cmdclass={
        'install': Install,
        'bdist_wheel': bdist_wheel,
    },
    url='https://github.com/pztrick/vext.SoapySDR',
    author='Patrick Paul',
    author_email='patrick@astrohaus.com',
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.5',
    ],
    keywords='virtualenv SoapySDR vext',
    setup_requires=["setuptools>=0.18.8"],
    install_requires=["vext>=0.7.0"],
)
