from setuptools import setup

setup(
    name="PySizer",
    author="Kumar Aditya",
    author_email="@kumaraditya303 Github",
    description="PySizer is a simple python command line program to resize images efficiently using Threads. This program uses click as a command line argument parser. It can also be used to pyinstaller to create a executable.",
    license="MIT",
    keywords="Pillow ThreadPoolExecutor",
    url="https://github.com/kumaraditya303/PySizer",
    version="1.0.0",
    py_modules=["pysizer"],
    install_requires=[
        "Click",
        "Pillow",
    ],
    entry_points="""
	[console_scripts]
	pysizer=pysizer:main
	""",
    classifiers=["Topic :: Utilities"],
)
