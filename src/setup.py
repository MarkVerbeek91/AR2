from distutils.core import setup
import py2exe, sys, os

setup(
    name    = 'AR2 control program',
    version = '1.0',
    options = {'py2exe': {'optimize': 2}},
    windows = [{'script': "AR2.py","icon_resources": [(1, "icons/AR2.ico")]}],
    zipfile = "shared.lib",
)
