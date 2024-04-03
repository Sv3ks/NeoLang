@echo off
py setup.py sdist bdist_wheel
pip install dist\neolang-%1-py3-none-any.whl --force-reinstall