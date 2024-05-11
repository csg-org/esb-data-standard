# EAVS Section B Data Standard
## About the project
Developed through a collaborative agreement between the Council of State Governments and the Federal Voting Assistance Program, or FVAP, the Election Administration and Voting Survey (EAVS) Section B Data Standard aims to reduce the amount of work required for election officials to complete the EAVS, a bi-annual survey administered by the US Election Assistance Commission, or EAC. A data export, based on voter-level transactional data, can be compiled to answer the questions in Section B as well as provide more comprehensive information for analysis.

## Documentation
### Prerequisites
The documentation is built with [Sphinx](https://www.sphinx-doc.org/en/master/) and requires execution of a simple [python](https://www.python.org/) script. Packages are maintained with [pipenv](https://pypi.org/project/pipenv/), which can be installed with [pip](https://pypi.org/project/pip/).

#### Changing branch name
If you have an existing clone of the respository, you'll need to update the branch name to `main` from `master`. To do this, run the following commands:

```sh
git branch -m master main
git fetch origin
git branch -u origin/main main
git remote set-head origin -a
```

### Build
Navigate to the project directory (assuming you're not already there) and install the required libraries.

```sh
cd /path/to/esb-data-standard
pipenv install
```

If you've made changes to the specification, do the following:

```sh
cd docs
pipenv run python tableschema_docs_parser.py
```

After executing the above (or assuming you haven't made changes), navigate to the `docs` folder and run the following commands:

```sh
sphinx-build -b html source build
python -m http.server --directory build
```

Open a browser and connect to [http://localhost:8000](http://localhost:8000) and you should see the documentation.

## Publishing a new release

When publishing a new release, double-check that there are no errors in the tableschema, the version numbers are correct in `tableschema.json` and `conf.py`, the documentation contains no build errors, and the documentation is viewable locally using the steps defined above.

When creating a GitHub release, make sure to explicitly add the latest `tableschema.json` to the release so implementers of the standard can easily access the file to use to validate their standardized datasets using the [DataCurator](https://github.com/qcif/data-curator).