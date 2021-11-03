from setuptools import setup, find_packages

VERSION = '0.1.0'
DESCRIPTION = 'BoldLines Python Package'

with open("README.md", "r", encoding="utf-8") as fh:
    long = fh.read()


setup(

    name="BoldLines",
    version=VERSION,
    author="krishna sonune",
    author_email="krishnasonune87@gmail.com",
    description=DESCRIPTION,
    long_description=long,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    install_requires=[],  
    

    keywords=['python', 'first package'],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Education",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)
