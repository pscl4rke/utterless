
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

####

image-to-run += test-in-container-3.8-slim-bullseye
image-to-run += test-in-container-3.9-slim-bullseye
image-to-run += test-in-container-3.10-slim-bullseye
image-to-run += test-in-container-3.11-slim-bullseye
image-to-run += test-in-container-3.12-slim-bookworm
image-to-run += test-in-container-3.13-slim-bookworm

test-in-container: $(image-to-run)
	@echo
	@echo "=============================================================="
	@echo "Successfully tested all versions with ephemerun:"
	@echo "$^" | tr ' ' '\n'
	@echo "=============================================================="
	@echo

test-in-container-%:
	@echo
	@echo "=============================================================="
	@echo "Testing with docker.io/library/python:$*"
	@echo "=============================================================="
	@echo
	ephemerun \
		-i "docker.io/library/python:$*" \
		-v ".:/root/src:ro" \
		-W "/root" \
		-S "cp -air ./src/* ." \
		-S "pip --no-cache-dir install ." \
		-W "/root/tests" \
		-S "python -m unittest discover ." \
