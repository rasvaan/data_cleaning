## Merge CSV files into Adlib dat file
Script that merges multiple csv files into dat file that can easily be imported in Adlib.

```
merge
│   merge.exe
│   merge.log
│   merge.md
│
└───data
│   │
│   merge
│       │   1_tag1.csv
│       │   2_tag2.csv
│       │   ...
│   └───out
│       │   merge-date.dat
```

To merge .csv files in a single Adlib .dat file follow these steps:

1. add .csv files to folder `merge/data/merge`
2. run `merge/merge.exe`
3. check log `merge/merge.log`
4. retrieve .dat file from `merge/data/out`
