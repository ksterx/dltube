"""
This is a setup.py script generated by py2applet

Usage:
    python setup.py py2app
"""

from setuptools import setup

APP = ["app.py"]
APP_NAME = "dltube"
DATA_FILES = []
OPTIONS = {
    "iconfile": "images/app.icns",
    "plist": {
        "CFBundleName": APP_NAME,
        "CFBundleDisplayName": APP_NAME,
        "CFBundleVersion": "1.0",
        "CFBundleShortVersionString": "1.0",
    },
}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={"py2app": OPTIONS},
    setup_requires=["py2app"],
)
