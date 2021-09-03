import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="marko-labeled-footnotes",
    version="0.0.1",
    author="Jake Kara",
    author_email="jake@jakekara.com",
    description="Labeled footnotes support for the Marko Markdown parser",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jakekara/marko-labeled-footnotes",
    project_urls={
        "Bug Tracker": "https://github.com/jakekara/marko-labeled-footnotes/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)