from setuptools import setup

setup(
	name='PySizer',
	version='1.0.0',
	py_modules=['pysizer'],
	install_requires=[
		"Click",
		"Pillow",
	],
	entry_points='''
	[console_scripts]
	pysizer=pysizer:main
	''',
)
