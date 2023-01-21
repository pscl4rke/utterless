
pre-release-checks:
	pyroma .

export PYTHON_KEYRING_BACKEND := keyring.backends.null.Keyring

release:
	test ! -d dist
	python3 setup.py sdist bdist_wheel
	check-wheel-contents dist
	twine check dist/*
	twine upload dist/*
	mv build* *egg-info -i dist
	mv dist dist.$$(date +%Y-%m-%d.%H%M%S)
