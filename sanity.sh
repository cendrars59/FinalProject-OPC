isort -rc .
docformatter --recursive --in-place .
autopep8 --recursive --in-place .
flake8