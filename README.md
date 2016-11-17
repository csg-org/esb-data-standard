# EAVS Section B Data Standard
## About the project
Developed through a collaborative agreement between the Council of State Governments and the Federal Voting Assistance Program, or FVAP, the Election Administration and Voting Survey (EAVS) Section B Data Standard aims to reduce the amount of work required for election officials to complete the EAVS, a bi-annual survey administered by the US Election Assistance Commission, or EAC. A data export, based on voter-level transactional data, can be compiled to answer the questions in Section B as well as provide more comprehensive information for analysis.

## Documentation
### Prerequisites
The documentation is built with (Sphinx)[http://www.sphinx-doc.org/en/1.4.8/] and requires execution of a simple (python)[https://www.python.org/] script.

### Build
While this first step is optional, it's arguably easiest to create a virtual environment to keep the required libraries contained.

```sh
$ pip install virtualenv
$ virtualenv ./venv
$ source ./venv/bin/activate
```

Once the virtual environment is set up and active, navigate to the project directory (assuming you're not already there) and install the required libraries.

```sh
$ cd /path/to/esb-data-standard
$ pip install -r requirements.txt
```

If you've made changes to the specification, do the following:

```sh
$ cd docs/source
$ python datapackage_docs_parser.py
```

After executing the above (or assuming you haven't made changes), navigate to the `docs` folder and run the following commands:

```sh
$ make html
$ cd build/html
$ python -m http.server()
```

Depending on your version of python (i.e. 2.7 vs 3.x), the last line could be `python -m SimpleHttpServer 8000`. Open a browser and connect to `http://localhost:8000` and you should see the documentation.