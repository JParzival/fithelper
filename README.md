# fithelper
This repository aims to help Python developers with fit files, transforming them and converting into dataframes.

Provides .FIT file examples gathered from Zwift trainings for a fast introduction to the repository.

## 🛠️ Installation

To install the required packages, just run:

```
pip install -r requirements.txt
```

Probably in the future an option for Docker image is added.

## 💡 How to work with this repo

1. Place your fit files into the data>fit folder.
2. Ensure that the data>json folder is empty, if this is your first execution.
3. Run the conversion from .FIT to .JSON, which is incremental: It will only convert and add the new files.


```
cd src
python fit2json.py
```

4. If needed, convert the .JSON files into a pandas Dataframe to work with it
```
cd src
python json2df.py
```
If the constant SAVE_DATAFRAME is True, the dataframe will be saved on the root folder of the project.


## 🧪 How to run the tests

1. Place yourself in the root folder of the repo
2. Run the following command:

```
pytest
```
3. If you want to gather the coverage, just run the following command after installing coverage:

```
coverage report
```

### Current testing coverage of utils

![Alt text](imgs/coverage_report.png?raw=true "Coverage report")