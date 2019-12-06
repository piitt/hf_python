make 3 files (setup.py, RAEDME.txt, module.py)
my_module$ python3 setup.py sdist

cd dist
dist$ python3 -m pip install vsearch-1.0.tar.gz

python3 -m pip install pytest-pep8
python3 -m pytest --pep8 vsearch.py

