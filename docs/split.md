# Split Adlib dat file into CSV files
Script that splits data exported from Adlib into multiple csv files.

```
split
│   split.exe
│   split.log
│   split.md
│
└───data
│   │
│   └───split
│   │   │   records.dat
│   └───out
│       │   1_tag1.csv
│       │   2_tag2.csv
│       │   ...
```

To split an Adlib .dat file follow these steps:

1. add a file called `records.dat` in the folder `split/data/split`
2. run `split/split.exe`
3. check log `split/split.log`
4. retrieve csv files from `split/data/out`
