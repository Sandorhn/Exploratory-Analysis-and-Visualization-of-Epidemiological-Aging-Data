## Exploratory Investigation of Epidemiological Aging Data USA 2014

I found a dataset online (rows.csv) that is a very disorganized spreadsheet depicting different territories in the USA, and several variables measured from their older populations.
This was a great excesize for translating and rearranging the dataframe in pandas.
```python
# import pandas lib as pd
import pandas as pd

# read by default 1st sheet of an excel file
dataframe1 = pd.read_csv('rows.csv')
display(dataframe1)
```
