from setuptools import setup, find_packages

setup(
    name="hubspot-python-client",
    version="1.0.0",
    author="Rollout",
    author_email="dev@rollout.com",
    description=hubspot Python client,
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/mike-rollout/hubspot-python-client",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
