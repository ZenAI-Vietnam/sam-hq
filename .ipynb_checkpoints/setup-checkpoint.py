from setuptools import setup, find_packages

setup(
    name="sam_hq",
    version="0.1.1",
    packages=find_packages(),
    install_requires=[
        "torch>=1.7.0",
        "torchvision",
        "numpy",
        "opencv-python",
        "timm",
        "segment-anything"
    ],
    author="HQ-SAM team",
    description="High Quality Segment Anything Model",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/ZenAI-Vietnam/sam-hq",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
)