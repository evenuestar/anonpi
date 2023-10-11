from setuptools import setup, find_packages
from anonpi import (app_info)


setup(
    **app_info(),
    description='The "anonpi" module is a Python package designed to streamline interactions with calling systems. It simplifies the development of applications that require features like machine detection, IVR, DTMF handling, call recording, playback, and more. This module provides a clean and intuitive API for seamless integration into Python applications.',
    long_description=open("README.md").read(),
    packages=find_packages(),
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Topic :: Communications :: Telephony",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.9",
    ],
    keywords="anonpi, python, calling, systems, api, wrapper, module",
    python_requires=">=3.9",
    install_requires=[],
    long_description_content_type="text/markdown"
)
