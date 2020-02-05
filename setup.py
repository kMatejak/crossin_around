from setuptools import setup

setup(
	name="crossin_around",
	version="1.0.0",
	entry_points={
		"console_scripts": [
			"crossin=app:game"
			]
		}
	)
