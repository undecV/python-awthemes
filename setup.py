"""
A port of [tcl-awthemes] to Python ttk.
"""

from setuptools import setup, find_packages


__version__: str = "0.2.0"


setup(
    name="python-awthemes",
    version=__version__,
    packages=find_packages(),
    description="A port of [tcl-awthemes] to Python ttk.",
    long_description=open("README.md", "r", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    author="undecV",
    author_email="22562116+undecV@users.noreply.github.com",
    license="Zlib",
    install_requires=[
        "tksvg"
    ],
    include_package_data=True,
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: zlib/libpng License",
        "Programming Language :: Tcl",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
)
