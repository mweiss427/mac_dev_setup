import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()


setuptools.setup(
    name='mac_developer_setup',
    version='0.1',
    scripts=['mac_developer_setup'],
    author="Matt Weiss",
    author_email="mweiss427@gmail.com",
    description="A Mac uitlity package for developers",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/mweiss427/mac_dev_setup.git",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: macOS",
    ],
)
