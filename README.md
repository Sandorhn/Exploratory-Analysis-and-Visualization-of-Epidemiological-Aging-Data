## Data Cleaning and Visualization of Epidemiological Aging Data USA 2014

I found a dataset online (rows.csv) that is a very disorganized spreadsheet depicting different territories in the USA, and several variables measured from their older populations.
This was a great excesize for translating and rearranging the dataframe in pandas.
```python
# import pandas lib as pd
import pandas as pd

# read by default 1st sheet of an excel file
dataframe1 = pd.read_csv('rows.csv')
display(dataframe1)
```
![initial dataset screenshot](https://user-images.githubusercontent.com/121974615/211162577-c6fba2db-f408-45e1-b7f5-4bbb8d24fd8a.PNG)

There were several redundant or blank fields in the dataframe that I removed to help clean up the data.
```python
dataframe1_1 = dataframe1.drop(
    labels=["Datasource", "Response", "DataValueTypeID", "Data_Value_Type", "Data_Value_Alt", 
            "Sample_Size"],
    axis=1
)
```
There was also no data for the Virgin Islands, so it was removed from the dataset.
``` python
dataframe1_2 = dataframe1_1[dataframe1_1["LocationDesc"].str.contains("Virgin Islands")==False]
```
The dataset spans 4 years (2011-2014) and four age groups (50-54, 55-59, 60-64, and 65+). The only numerical data are percentages of those age groups in different states or territories of the USA for which one of the following 32 variables apply:
Frequent mental distress, Disability status, Fall with injury within last year, Oral health: tooth retention, Lifetime diagnosis of depression, Physically unhealthy days, Ever had pneumococcal vaccine, Binge drinking within past 30 days, Social and emotional support, Prevalence of sufficient sleep (>6 hours), Obesity, Up-to-date with recommended vaccines and screenings - Men, Mammogram within past 2 years, Colorectal cancer screening, Current smoking, No leisure time physical activity within past month, Life satisfaction, Influenza vaccine within past year, Diabetes screening within past 3 years, Pap test within past 3 years, Self-rated health (fair to poor health), Self-rated health (good to excellent health), Recent activity limitation in past month, Eating 2 or more fruits daily, Eating 3 or more vegetables daily, Taking medication for high blood pressure, Cholesterol checked in past 5 years, High blood pressure ever, Lifetime diagnosis of anxiety disorder, Increased confusion or memory loss (ICML) among older adults, Functional difficulties associated with increased confusion or memory loss (ICML) among older adults, UTD preventive services (women). 

There were many questions I wanted to answer, but first I decided to remold the data into more graphable spreadsheets with region as the index, and topic as the column names. In order to do this, I had to split the dataset into 16 datasets, for each year and age group. But even before that I needed to make sure each region name was unique. There were 7 fields that were described as United States: DC and Territories, but that were subdivided into the fields: female, male, asian, black, white, hispanic, and native american. These descriptors had to be added to the location column in order to be able to parse the data correctly. To solve this problem, I created a new column that appended the demographic data to the specific regions, as there was no demographic data listed for specific states, this was not an issue.
```python
dataframe1_2["NewColumn"] = dataframe1_2["LocationDesc"].str.lower() + " " + dataframe1_2["Stratification2"].str.lower()
```
While most of the data units were averages, there were also a handful of means collected, but being in the minority of values, these were removed from the dataset.
```python
dataframe1_2 = dataframe1_2[dataframe1_2['Data_Value_Unit'].str.contains('Number')==False]
```





