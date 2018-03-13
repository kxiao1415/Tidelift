# Tidelift

in command line
1. cd path/to/this/directory
2. source tidelift/bin/activate
3. export PYTHONPATH="$PYTHONPATH:path/to/this/directory"
4. pip install -r requirements.txt
5. python run.py

Now you can make requests to the two end points like this:

1. curl -X GET 'http://localhost:5000/package/health/dummy/0.9'

2. curl -X GET 'http://localhost:5000/package/releases/tiny-tarball'