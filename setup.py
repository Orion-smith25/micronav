from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="waynav",
    version="0.1.1",
    author="Smith (Maritime Autonomy Lab)",
    description="Lightweight autonomous navigation library",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Orion-smith25/micronav",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Scientific/Engineering",
    ],
    python_requires=">=3.7",
)
