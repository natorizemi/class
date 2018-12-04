# rough spec

## Procedure
1. Read conversations from file
1. Calculate TF-IDF
1. Export result for each files (descending order, CSV format)

## Export format
* CSV
* CSV filename: `ORIGIN-FILENAME_LOCAL-GOVERNMENT-CODE.csv`
* columns
    1. word
    1. tfidf

### CSV Example
```csv
word,tfidf
御,0.000713596
実習,0.000607071
```
