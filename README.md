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
Finally, with all the data cleaning done, it was time to seperate the dataframe into 16 different dataframes along the lines of age groups and years.
```python
df2014 = dataframe1_2[dataframe1_2["YearEnd"]==2014]
df2013 = dataframe1_2[dataframe1_2["YearEnd"]==2013]
df2012 = dataframe1_2[dataframe1_2["YearEnd"]==2012]
df2011 = dataframe1_2[dataframe1_2["YearEnd"]==2011]

#ok now 4 of each of these to make the 16
df2011_50 = df2011[df2011["Stratification1"].str.contains("50")==True]
df2011_55 = df2011[df2011["Stratification1"].str.contains("55")==True]
df2011_60 = df2011[df2011["Stratification1"].str.contains("60")==True]
df2011_65 = df2011[df2011["Stratification1"].str.contains("65")==True]

df2012_50 = df2012[df2012["Stratification1"].str.contains("50")==True]
df2012_55 = df2012[df2012["Stratification1"].str.contains("55")==True]
df2012_60 = df2012[df2012["Stratification1"].str.contains("60")==True]
df2012_65 = df2012[df2012["Stratification1"].str.contains("65")==True]

df2013_50 = df2013[df2013["Stratification1"].str.contains("50")==True]
df2013_55 = df2013[df2013["Stratification1"].str.contains("55")==True]
df2013_60 = df2013[df2013["Stratification1"].str.contains("60")==True]
df2013_65 = df2013[df2013["Stratification1"].str.contains("65")==True]

df2014_50 = df2014[df2014["Stratification1"].str.contains("50")==True]
df2014_55 = df2014[df2014["Stratification1"].str.contains("55")==True]
df2014_60 = df2014[df2014["Stratification1"].str.contains("60")==True]
df2014_65 = df2014[df2014["Stratification1"].str.contains("65")==True]
```
In 16 dataframes, there were no longer multiple variables for each state other than 'topic' variables.
The reshaping of the dataframes could be performed.
To explain what is happening here: State averages were converted to an array and reshaped to a structure where the number of unique states made up the indexes, and the number of unique topics made up the columns. The state and column names were then set as the row and column names. This format made the data much more tidy and graphable.
```python
df2011_50i = pd.DataFrame(df2011_50["Data_Value"].to_numpy().reshape(len(df2011_50.Topic.unique()),len(df2011_50.NewColumn.unique())).T,index = df2011_50.NewColumn.unique(),columns = df2011_50.Topic.unique())
df2011_55i = pd.DataFrame(df2011_55["Data_Value"].to_numpy().reshape(len(df2011_55.Topic.unique()),len(df2011_55.NewColumn.unique())).T,index = df2011_55.NewColumn.unique(),columns = df2011_55.Topic.unique())
df2011_60i = pd.DataFrame(df2011_60["Data_Value"].to_numpy().reshape(len(df2011_60.Topic.unique()),len(df2011_60.NewColumn.unique())).T,index = df2011_60.NewColumn.unique(),columns = df2011_60.Topic.unique())
df2011_65i = pd.DataFrame(df2011_65["Data_Value"].to_numpy().reshape(len(df2011_65.Topic.unique()),len(df2011_65.NewColumn.unique())).T,index = df2011_65.NewColumn.unique(),columns = df2011_65.Topic.unique())

df2012_50i = pd.DataFrame(df2012_50["Data_Value"].to_numpy().reshape(len(df2012_50.Topic.unique()),len(df2012_50.NewColumn.unique())).T,index = df2012_50.NewColumn.unique(),columns = df2012_50.Topic.unique())
df2012_55i = pd.DataFrame(df2012_55["Data_Value"].to_numpy().reshape(len(df2012_55.Topic.unique()),len(df2012_55.NewColumn.unique())).T,index = df2012_55.NewColumn.unique(),columns = df2012_55.Topic.unique())
df2012_60i = pd.DataFrame(df2012_60["Data_Value"].to_numpy().reshape(len(df2012_60.Topic.unique()),len(df2012_60.NewColumn.unique())).T,index = df2012_60.NewColumn.unique(),columns = df2012_60.Topic.unique())
df2012_65i = pd.DataFrame(df2012_65["Data_Value"].to_numpy().reshape(len(df2012_65.Topic.unique()),len(df2012_65.NewColumn.unique())).T,index = df2012_65.NewColumn.unique(),columns = df2012_65.Topic.unique())

df2013_50i = pd.DataFrame(df2013_50["Data_Value"].to_numpy().reshape(len(df2013_50.Topic.unique()),len(df2013_50.NewColumn.unique())).T,index = df2013_50.NewColumn.unique(),columns = df2013_50.Topic.unique())
df2013_55i = pd.DataFrame(df2013_55["Data_Value"].to_numpy().reshape(len(df2013_55.Topic.unique()),len(df2013_55.NewColumn.unique())).T,index = df2013_55.NewColumn.unique(),columns = df2013_55.Topic.unique())
df2013_60i = pd.DataFrame(df2013_60["Data_Value"].to_numpy().reshape(len(df2013_60.Topic.unique()),len(df2013_60.NewColumn.unique())).T,index = df2013_60.NewColumn.unique(),columns = df2013_60.Topic.unique())
df2013_65i = pd.DataFrame(df2013_65["Data_Value"].to_numpy().reshape(len(df2013_65.Topic.unique()),len(df2013_65.NewColumn.unique())).T,index = df2013_65.NewColumn.unique(),columns = df2013_65.Topic.unique())

df2014_50i = pd.DataFrame(df2014_50["Data_Value"].to_numpy().reshape(len(df2014_50.Topic.unique()),len(df2014_50.NewColumn.unique())).T,index = df2014_50.NewColumn.unique(),columns = df2014_50.Topic.unique())
df2014_55i = pd.DataFrame(df2014_55["Data_Value"].to_numpy().reshape(len(df2014_55.Topic.unique()),len(df2014_55.NewColumn.unique())).T,index = df2014_55.NewColumn.unique(),columns = df2014_55.Topic.unique())
df2014_60i = pd.DataFrame(df2014_60["Data_Value"].to_numpy().reshape(len(df2014_60.Topic.unique()),len(df2014_60.NewColumn.unique())).T,index = df2014_60.NewColumn.unique(),columns = df2014_60.Topic.unique())
df2014_65i = pd.DataFrame(df2014_65["Data_Value"].to_numpy().reshape(len(df2014_65.Topic.unique()),len(df2014_65.NewColumn.unique())).T,index = df2014_65.NewColumn.unique(),columns = df2014_65.Topic.unique())
```
![tidy and graphable](https://user-images.githubusercontent.com/121974615/211614892-21953422-65af-403e-a9b9-273bd37218d2.PNG)
Finally, the reshaped dataframes were exported for visualization.
```python
df2011_50i.to_csv(r'C:/Users/Sandor/Desktop/EMPLOYMENT/Aging Projects/Data Analysis Aging Study/Data4visualization/df2011_50i.csv')
df2011_55i.to_csv(r'C:/Users/Sandor/Desktop/EMPLOYMENT/Aging Projects/Data Analysis Aging Study/Data4visualization/df2011_55i.csv')
df2011_60i.to_csv(r'C:/Users/Sandor/Desktop/EMPLOYMENT/Aging Projects/Data Analysis Aging Study/Data4visualization/df2011_60i.csv')
df2011_65i.to_csv(r'C:/Users/Sandor/Desktop/EMPLOYMENT/Aging Projects/Data Analysis Aging Study/Data4visualization/df2011_65i.csv')

df2012_50i.to_csv(r'C:/Users/Sandor/Desktop/EMPLOYMENT/Aging Projects/Data Analysis Aging Study/Data4visualization/df2012_50i.csv')
df2012_55i.to_csv(r'C:/Users/Sandor/Desktop/EMPLOYMENT/Aging Projects/Data Analysis Aging Study/Data4visualization/df2012_55i.csv')
df2012_60i.to_csv(r'C:/Users/Sandor/Desktop/EMPLOYMENT/Aging Projects/Data Analysis Aging Study/Data4visualization/df2012_60i.csv')
df2012_65i.to_csv(r'C:/Users/Sandor/Desktop/EMPLOYMENT/Aging Projects/Data Analysis Aging Study/Data4visualization/df2012_65i.csv')

df2013_50i.to_csv(r'C:/Users/Sandor/Desktop/EMPLOYMENT/Aging Projects/Data Analysis Aging Study/Data4visualization/df2013_50i.csv')
df2013_55i.to_csv(r'C:/Users/Sandor/Desktop/EMPLOYMENT/Aging Projects/Data Analysis Aging Study/Data4visualization/df2013_55i.csv')
df2013_60i.to_csv(r'C:/Users/Sandor/Desktop/EMPLOYMENT/Aging Projects/Data Analysis Aging Study/Data4visualization/df2013_60i.csv')
df2013_65i.to_csv(r'C:/Users/Sandor/Desktop/EMPLOYMENT/Aging Projects/Data Analysis Aging Study/Data4visualization/df2013_65i.csv')

df2014_50i.to_csv(r'C:/Users/Sandor/Desktop/EMPLOYMENT/Aging Projects/Data Analysis Aging Study/Data4visualization/df2014_50i.csv')
df2014_55i.to_csv(r'C:/Users/Sandor/Desktop/EMPLOYMENT/Aging Projects/Data Analysis Aging Study/Data4visualization/df2014_55i.csv')
df2014_60i.to_csv(r'C:/Users/Sandor/Desktop/EMPLOYMENT/Aging Projects/Data Analysis Aging Study/Data4visualization/df2014_60i.csv')
df2014_65i.to_csv(r'C:/Users/Sandor/Desktop/EMPLOYMENT/Aging Projects/Data Analysis Aging Study/Data4visualization/df2014_65i.csv')
```


