# Data cleaning
Code that supports data cleaning workflows

## Split Adlib dat file into CSV files
Script that splits data exported from Adlib into multiple csv files.

To run the script:
```
python clean/split.py
```

To run tests:
```
python -m unittest -v tests.test_split
```

## Merge CSV files into Adlib dat file
Script that merges multiple csv files into dat file that can easily be imported in Adlib.


To run the script, add files to 'merge' folder and run the following command:
```
python clean/merge.py
```

To run tests:
```
python -m unittest -v tests.test_merge
```
