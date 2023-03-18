from setuptools import find_packages, setup

long_desc = """
This package contains a Sphinx extension to embed Geogebra applets. It defines a directive "ggb".
"""

requires = ["Sphinx>=0.6", "setuptools"]


setup(
    name="sphinxcontrib-geogebra",
    version="2.0",
    description="Sphinx geogebra applet extension",
    author="Solrun Einarsdottir",
    author_email="solrun.einarsdottir@gmail.com",
    maintainer="Benedikt Magnusson",
    maintainer_email="bsm@hi.is",
    packages=find_packages(),
    include_package_data=True,
    install_requires=requires,
    namespace_packages=["sphinxcontrib"],
)
