import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

with open("requirements.txt", "r") as f:
    required_packages = f.read().splitlines()

setuptools.setup(
    name="xnetwork",
    version="1.0.3",
    author="Filipi N. Silva and Cesar H. Comin",
    author_email="filsilva@iu.edu",
    description="Small python package to read .xnet (compleX NETwork format) files used in my other scripts.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/filipinascimento/xnet",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.0',
    install_requires=required_packages
)