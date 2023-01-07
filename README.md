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
![initial dataset screenshot](https://user-images.githubusercontent.com/121974615/211162577-c6fba2db-f408-45e1-b7f5-4bbb8d24fd8a.PNG)

There were several redundant or useless fields in the dataframe that I removed to help clean up the data.
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

There were many questions I wanted to answer, but first I decided to omit the data from years prior to 2014, because performing an analysis of a 4 year time span didn't interest me, and because 2014 was tied for the most records.
![year data counts](https://user-images.githubusercontent.com/121974615/211163538-ba615790-892b-4557-a902-644a6ab6d3e2.PNG)

```python
dataframe1_3 = dataframe1_2[dataframe1_2["YearEnd"]==2014]
```
At this point I had decided that for this first analysis, I was interested in determining whether variables predictive of other variables were as predictive at every age group. I decided that in the absence of individuals, my 'n' would be the 57 individual USA states and territories, so I omitted all data that pertained to the USA as a whole.
```python
experiment1 = dataframe1_3[dataframe1_3["LocationDesc"].str.contains("United States")==False]
```
I wanted to use a linear regression model training predictive variables at certain age groups and then testing against other age groups, so I divided the dataset further.
```python
experiment1_train = experiment1[experiment1["Stratification1"].str.contains("4 years")==True]
experiment1_test = experiment1[experiment1["Stratification1"].str.contains("4 years")==False]

experiment1_train_data = experiment1_train[experiment1_train["Stratification1"].str.contains("54 years")==True]
experiment1_train_targets = experiment1_train[experiment1_train["Stratification1"].str.contains("54 years")==False]
```
In the final step of the data table transformation, the numerical 'average' values were reshaped such that they were paired with their corresponding state or region of the USA on the index, and each variable in the columns. This setup makes the impending linear regression analysis much easier.
```python
ex_train_var = pd.DataFrame(experiment1_train_data["Data_Value"].to_numpy().reshape(len(experiment1_train_data.Topic.unique()),len(experiment1_train_data.LocationDesc.unique())).T,index = experiment1_train_data.LocationDesc.unique(),columns = experiment1_train_data.Topic.unique())
ex_train_var
```
![reshaped](https://user-images.githubusercontent.com/121974615/211166055-2676b90e-77e3-4991-b09f-b2b2afff0179.PNG)

