from setuptools import setup

setup(
    name="Library",
    version="1.0",
    packages=[''],
    install_requires=[],
    author="Antonio Romero Luque",
    author_email="a_pegaso@hotmail.com",
    description="A simple library management system built with Python.",
    long_description=open("README.md", encoding="utf-8").read(),
    url="https://github.com/Anton55100/Library",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    entry_points={
        "console_scripts": [
            "library_management=Library.__main__:main",
        ],
    },
)
