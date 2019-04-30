import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pypse",
    version="0.0.2",
    author="Hankel Bao",
    author_email="hankel.bao@gmail.com",
    description="A compiler for Pseudocode written in python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/HankelBao/PyPse",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=['lark-parser'],
)
