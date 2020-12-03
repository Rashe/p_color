python3 setup.py bdist_wheel
python3 setup.py bdist

python3 -m twine upload --repository pypi dist/*