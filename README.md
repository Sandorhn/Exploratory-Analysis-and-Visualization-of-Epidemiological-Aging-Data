## Data Cleaning and Visualization of Epidemiological Aging Data USA 2014

![Obesity](https://user-images.githubusercontent.com/121974615/211625772-1f1c0b8b-52ac-4116-a83f-7f0da6ffe4ee.gif)

I found a dataset online (rows.csv) that is a very disorganized spreadsheet depicting different territories in the USA, and several variables measured from their older populations.
This was a great excesize for translating and rearranging the dataframe in pandas in python, and visualizing using more advanced method in ggplot2 in R.

## Data Cleaning
First, I loaded the dataset into python.
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


## Visualization of Epidemiological Aging Data

I wanted to show the data in the form of a map specific to each state and show how each topic changed over time. 
In order to do this, I used ggplot2 with map_data in R.

First things first, I loaded the csvs in.
```r
df2011_50<-read.csv("C:/Users/Sandor/Desktop/EMPLOYMENT/Aging Projects/Data Analysis Aging Study/Data4visualization/df2011_50i.csv")
df2011_55<-read.csv("C:/Users/Sandor/Desktop/EMPLOYMENT/Aging Projects/Data Analysis Aging Study/Data4visualization/df2011_55i.csv")
df2011_60<-read.csv("C:/Users/Sandor/Desktop/EMPLOYMENT/Aging Projects/Data Analysis Aging Study/Data4visualization/df2011_60i.csv")
df2011_65<-read.csv("C:/Users/Sandor/Desktop/EMPLOYMENT/Aging Projects/Data Analysis Aging Study/Data4visualization/df2011_65i.csv")
df2012_50<-read.csv("C:/Users/Sandor/Desktop/EMPLOYMENT/Aging Projects/Data Analysis Aging Study/Data4visualization/df2012_50i.csv")
df2012_55<-read.csv("C:/Users/Sandor/Desktop/EMPLOYMENT/Aging Projects/Data Analysis Aging Study/Data4visualization/df2012_55i.csv")
df2012_60<-read.csv("C:/Users/Sandor/Desktop/EMPLOYMENT/Aging Projects/Data Analysis Aging Study/Data4visualization/df2012_60i.csv")
df2012_65<-read.csv("C:/Users/Sandor/Desktop/EMPLOYMENT/Aging Projects/Data Analysis Aging Study/Data4visualization/df2012_65i.csv")
df2013_50<-read.csv("C:/Users/Sandor/Desktop/EMPLOYMENT/Aging Projects/Data Analysis Aging Study/Data4visualization/df2013_50i.csv")
df2013_55<-read.csv("C:/Users/Sandor/Desktop/EMPLOYMENT/Aging Projects/Data Analysis Aging Study/Data4visualization/df2013_55i.csv")
df2013_60<-read.csv("C:/Users/Sandor/Desktop/EMPLOYMENT/Aging Projects/Data Analysis Aging Study/Data4visualization/df2013_60i.csv")
df2013_65<-read.csv("C:/Users/Sandor/Desktop/EMPLOYMENT/Aging Projects/Data Analysis Aging Study/Data4visualization/df2013_65i.csv")
df2014_50<-read.csv("C:/Users/Sandor/Desktop/EMPLOYMENT/Aging Projects/Data Analysis Aging Study/Data4visualization/df2014_50i.csv")
df2014_55<-read.csv("C:/Users/Sandor/Desktop/EMPLOYMENT/Aging Projects/Data Analysis Aging Study/Data4visualization/df2014_55i.csv")
df2014_60<-read.csv("C:/Users/Sandor/Desktop/EMPLOYMENT/Aging Projects/Data Analysis Aging Study/Data4visualization/df2014_60i.csv")
df2014_65<-read.csv("C:/Users/Sandor/Desktop/EMPLOYMENT/Aging Projects/Data Analysis Aging Study/Data4visualization/df2014_65i.csv")
```
There were a few remaining things to do to prepare the data for visualization, because I wanted to look at a map of each state, it didn't make sense to keep the race and gender data on the USA as a whole.
```r
df2011_50s<-df2011_50[!grepl("united", df2011_50$X),]
df2011_55s<-df2011_55[!grepl("united", df2011_55$X),]
df2011_60s<-df2011_60[!grepl("united", df2011_60$X),]
df2011_65s<-df2011_65[!grepl("united", df2011_65$X),]
df2012_50s<-df2012_50[!grepl("united", df2012_50$X),]
df2012_55s<-df2012_55[!grepl("united", df2012_55$X),]
df2012_60s<-df2012_60[!grepl("united", df2012_60$X),]
df2012_65s<-df2012_65[!grepl("united", df2012_65$X),]
df2013_50s<-df2013_50[!grepl("united", df2013_50$X),]
df2013_55s<-df2013_55[!grepl("united", df2013_55$X),]
df2013_60s<-df2013_60[!grepl("united", df2013_60$X),]
df2013_65s<-df2013_65[!grepl("united", df2013_65$X),]
df2014_50s<-df2014_50[!grepl("united", df2014_50$X),]
df2014_55s<-df2014_55[!grepl("united", df2014_55$X),]
df2014_60s<-df2014_60[!grepl("united", df2014_60$X),]
df2014_65s<-df2014_65[!grepl("united", df2014_65$X),]
```
I also needed to remove the "no_data" artefact that appeared at the end of the NewColumn for each of the states after creating that column in python.
```r
no_data<-" no_data"

df2011_50sn<-as.data.frame(gsub(no_data, "", df2011_50s$X))
df2011_50s<-subset(df2011_50s, select = -c(X))
df2011_50s$region<-df2011_50sn$`gsub(no_data, "", df2011_50s$X)`

df2011_55sn<-as.data.frame(gsub(no_data, "", df2011_55s$X))
df2011_55s<-subset(df2011_55s, select = -c(X))
df2011_55s$region<-df2011_55sn$`gsub(no_data, "", df2011_55s$X)`

df2011_60sn<-as.data.frame(gsub(no_data, "", df2011_60s$X))
df2011_60s<-subset(df2011_60s, select = -c(X))
df2011_60s$region<-df2011_60sn$`gsub(no_data, "", df2011_60s$X)`

df2011_65sn<-as.data.frame(gsub(no_data, "", df2011_65s$X))
df2011_65s<-subset(df2011_65s, select = -c(X))
df2011_65s$region<-df2011_65sn$`gsub(no_data, "", df2011_65s$X)`

df2012_50sn<-as.data.frame(gsub(no_data, "", df2012_50s$X))
df2012_50s<-subset(df2012_50s, select = -c(X))
df2012_50s$region<-df2012_50sn$`gsub(no_data, "", df2012_50s$X)`

df2012_55sn<-as.data.frame(gsub(no_data, "", df2012_55s$X))
df2012_55s<-subset(df2012_55s, select = -c(X))
df2012_55s$region<-df2012_55sn$`gsub(no_data, "", df2012_55s$X)`

df2012_60sn<-as.data.frame(gsub(no_data, "", df2012_60s$X))
df2012_60s<-subset(df2012_60s, select = -c(X))
df2012_60s$region<-df2012_60sn$`gsub(no_data, "", df2012_60s$X)`

df2012_65sn<-as.data.frame(gsub(no_data, "", df2012_65s$X))
df2012_65s<-subset(df2012_65s, select = -c(X))
df2012_65s$region<-df2012_65sn$`gsub(no_data, "", df2012_65s$X)`

df2013_50sn<-as.data.frame(gsub(no_data, "", df2013_50s$X))
df2013_50s<-subset(df2013_50s, select = -c(X))
df2013_50s$region<-df2013_50sn$`gsub(no_data, "", df2013_50s$X)`

df2013_55sn<-as.data.frame(gsub(no_data, "", df2013_55s$X))
df2013_55s<-subset(df2013_55s, select = -c(X))
df2013_55s$region<-df2013_55sn$`gsub(no_data, "", df2013_55s$X)`

df2013_60sn<-as.data.frame(gsub(no_data, "", df2013_60s$X))
df2013_60s<-subset(df2013_60s, select = -c(X))
df2013_60s$region<-df2013_60sn$`gsub(no_data, "", df2013_60s$X)`

df2013_65sn<-as.data.frame(gsub(no_data, "", df2013_65s$X))
df2013_65s<-subset(df2013_65s, select = -c(X))
df2013_65s$region<-df2013_65sn$`gsub(no_data, "", df2013_65s$X)`

df2014_50sn<-as.data.frame(gsub(no_data, "", df2014_50s$X))
df2014_50s<-subset(df2014_50s, select = -c(X))
df2014_50s$region<-df2014_50sn$`gsub(no_data, "", df2014_50s$X)`

df2014_55sn<-as.data.frame(gsub(no_data, "", df2014_55s$X))
df2014_55s<-subset(df2014_55s, select = -c(X))
df2014_55s$region<-df2014_55sn$`gsub(no_data, "", df2014_55s$X)`

df2014_60sn<-as.data.frame(gsub(no_data, "", df2014_60s$X))
df2014_60s<-subset(df2014_60s, select = -c(X))
df2014_60s$region<-df2014_60sn$`gsub(no_data, "", df2014_60s$X)`

df2014_65sn<-as.data.frame(gsub(no_data, "", df2014_65s$X))
df2014_65s<-subset(df2014_65s, select = -c(X))
df2014_65s$region<-df2014_65sn$`gsub(no_data, "", df2014_65s$X)`
```
Next, I downloaded the geom_polygon data for each state, and merged the latitude and longitude coordinates with my own epidemiology data.
```r
mapstates<-map_data("state")

#merge your data to the states data
library(dplyr)
merged2011_50<-inner_join(mapstates, df2011_50s, by="region")
merged2011_55<-inner_join(mapstates, df2011_55s, by="region")
merged2011_60<-inner_join(mapstates, df2011_60s, by="region")
merged2011_65<-inner_join(mapstates, df2011_65s, by="region")
merged2012_50<-inner_join(mapstates, df2012_50s, by="region")
merged2012_55<-inner_join(mapstates, df2012_55s, by="region")
merged2012_60<-inner_join(mapstates, df2012_60s, by="region")
merged2012_65<-inner_join(mapstates, df2012_65s, by="region")
merged2013_50<-inner_join(mapstates, df2013_50s, by="region")
merged2013_55<-inner_join(mapstates, df2013_55s, by="region")
merged2013_60<-inner_join(mapstates, df2013_60s, by="region")
merged2013_65<-inner_join(mapstates, df2013_65s, by="region")
merged2014_50<-inner_join(mapstates, df2014_50s, by="region")
merged2014_55<-inner_join(mapstates, df2014_55s, by="region")
merged2014_60<-inner_join(mapstates, df2014_60s, by="region")
merged2014_65<-inner_join(mapstates, df2014_65s, by="region")
```
I had considered using gganimate to generate the slideshow effect I was looking for, but stacking the topic data from each of these dataframes on one another in order to animate by date and age group would leave me with a dataframe of ~200,000 rows and having come this far it was faster to do this another way. If I were starting from scratch however, I would have set up the dataframes in python with gganimate in mind.
Instead, I plotted the topic variables one at a time, making sure to keep the scale of the data consistent with scale_fill_gradient2 so that in the gif animation would be easier to understand.
```r
m11_50<-ggplot() + geom_polygon(data=merged2011_50, aes(x=long, y=lat, group=group, fill=Taking.medication.for.high.blood.pressure),
               color="white", size=0.2) + theme_bw() + theme(panel.border = element_blank(), panel.grid.major = element_blank(),
               panel.grid.minor = element_blank()) + scale_fill_gradient2(limits = c(0, 100), oob = scales::squish)
m11_50<-m11_50 + guides(fill=guide_legend(title = "% Taking Medication for High Blood Pressure")) + ggtitle("2011, Individuals Aged 50-54")
ggsave("m11_50.png")

m11_55<-ggplot() + geom_polygon(data=merged2011_55, aes(x=long, y=lat, group=group, fill=Taking.medication.for.high.blood.pressure),
               color="white", size=0.2) + theme_bw() + theme(panel.border = element_blank(), panel.grid.major = element_blank(),
               panel.grid.minor = element_blank()) + scale_fill_gradient2(limits = c(0, 100), oob = scales::squish)
m11_55<-m11_55 + guides(fill=guide_legend(title = "% Taking Medication for High Blood Pressure")) + ggtitle("2011, Individuals Aged 55-59")
ggsave("m11_55.png")

m11_60<-ggplot() + geom_polygon(data=merged2011_60, aes(x=long, y=lat, group=group, fill=Taking.medication.for.high.blood.pressure),
               color="white", size=0.2) + theme_bw() + theme(panel.border = element_blank(), panel.grid.major = element_blank(),
               panel.grid.minor = element_blank()) + scale_fill_gradient2(limits = c(0, 100), oob = scales::squish)
m11_60<-m11_60 + guides(fill=guide_legend(title = "% Taking Medication for High Blood Pressure")) + ggtitle("2011, Individuals Aged 60-64")
ggsave("m11_60.png")

m11_65<-ggplot() + geom_polygon(data=merged2011_65, aes(x=long, y=lat, group=group, fill=Taking.medication.for.high.blood.pressure),
               color="white", size=0.2) + theme_bw() + theme(panel.border = element_blank(), panel.grid.major = element_blank(),
               panel.grid.minor = element_blank()) + scale_fill_gradient2(limits = c(0, 100), oob = scales::squish)
m11_65<-m11_65 + guides(fill=guide_legend(title = "% Taking Medication for High Blood Pressure")) + ggtitle("2011, Individuals Aged 65+")
ggsave("m11_65.png")



m12_50<-ggplot() + geom_polygon(data=merged2012_50, aes(x=long, y=lat, group=group, fill=Taking.medication.for.high.blood.pressure),
               color="white", size=0.2) + theme_bw() + theme(panel.border = element_blank(), panel.grid.major = element_blank(),
               panel.grid.minor = element_blank()) + scale_fill_gradient2(limits = c(0, 100), oob = scales::squish)
m12_50<-m12_50 + guides(fill=guide_legend(title = "% Taking Medication for High Blood Pressure")) + ggtitle("2012, Individuals Aged 50-54")
ggsave("m12_50.png")

m12_55<-ggplot() + geom_polygon(data=merged2012_55, aes(x=long, y=lat, group=group, fill=Taking.medication.for.high.blood.pressure),
               color="white", size=0.2) + theme_bw() + theme(panel.border = element_blank(), panel.grid.major = element_blank(),
               panel.grid.minor = element_blank()) + scale_fill_gradient2(limits = c(0, 100), oob = scales::squish)
m12_55<-m12_55 + guides(fill=guide_legend(title = "% Taking Medication for High Blood Pressure")) + ggtitle("2012, Individuals Aged 55-59")
ggsave("m12_55.png")

m12_60<-ggplot() + geom_polygon(data=merged2012_60, aes(x=long, y=lat, group=group, fill=Taking.medication.for.high.blood.pressure),
               color="white", size=0.2) + theme_bw() + theme(panel.border = element_blank(), panel.grid.major = element_blank(),
               panel.grid.minor = element_blank()) + scale_fill_gradient2(limits = c(0, 100), oob = scales::squish)
m12_60<-m12_60 + guides(fill=guide_legend(title = "% Taking Medication for High Blood Pressure")) + ggtitle("2012, Individuals Aged 60-64")
ggsave("m12_60.png")

m12_65<-ggplot() + geom_polygon(data=merged2012_65, aes(x=long, y=lat, group=group, fill=Taking.medication.for.high.blood.pressure),
               color="white", size=0.2) + theme_bw() + theme(panel.border = element_blank(), panel.grid.major = element_blank(),
               panel.grid.minor = element_blank()) + scale_fill_gradient2(limits = c(0, 100), oob = scales::squish)
m12_65<-m12_65 + guides(fill=guide_legend(title = "% Taking Medication for High Blood Pressure")) + ggtitle("2012, Individuals Aged 65+")
ggsave("m12_65.png")


m13_50<-ggplot() + geom_polygon(data=merged2013_50, aes(x=long, y=lat, group=group, fill=Taking.medication.for.high.blood.pressure),
               color="white", size=0.2) + theme_bw() + theme(panel.border = element_blank(), panel.grid.major = element_blank(),
               panel.grid.minor = element_blank()) + scale_fill_gradient2(limits = c(0, 100), oob = scales::squish)
m13_50<-m13_50 + guides(fill=guide_legend(title = "% Taking Medication for High Blood Pressure")) + ggtitle("2013, Individuals Aged 50-54")
ggsave("m13_50.png")

m13_55<-ggplot() + geom_polygon(data=merged2013_55, aes(x=long, y=lat, group=group, fill=Taking.medication.for.high.blood.pressure),
               color="white", size=0.2) + theme_bw() + theme(panel.border = element_blank(), panel.grid.major = element_blank(),
               panel.grid.minor = element_blank()) + scale_fill_gradient2(limits = c(0, 100), oob = scales::squish)
m13_55<-m13_55 + guides(fill=guide_legend(title = "% Taking Medication for High Blood Pressure")) + ggtitle("2013, Individuals Aged 55-59")
ggsave("m13_55.png")

m13_60<-ggplot() + geom_polygon(data=merged2013_60, aes(x=long, y=lat, group=group, fill=Taking.medication.for.high.blood.pressure),
               color="white", size=0.2) + theme_bw() + theme(panel.border = element_blank(), panel.grid.major = element_blank(),
               panel.grid.minor = element_blank()) + scale_fill_gradient2(limits = c(0, 100), oob = scales::squish)
m13_60<-m13_60 + guides(fill=guide_legend(title = "% Taking Medication for High Blood Pressure")) + ggtitle("2013, Individuals Aged 60-64")
ggsave("m13_60.png")

m13_65<-ggplot() + geom_polygon(data=merged2013_65, aes(x=long, y=lat, group=group, fill=Taking.medication.for.high.blood.pressure),
               color="white", size=0.2) + theme_bw() + theme(panel.border = element_blank(), panel.grid.major = element_blank(),
               panel.grid.minor = element_blank()) + scale_fill_gradient2(limits = c(0, 100), oob = scales::squish)
m13_65<-m13_65 + guides(fill=guide_legend(title = "% Taking Medication for High Blood Pressure")) + ggtitle("2013, Individuals Aged 65+")
ggsave("m13_65.png")


m14_50<-ggplot() + geom_polygon(data=merged2014_50, aes(x=long, y=lat, group=group, fill=Taking.medication.for.high.blood.pressure),
               color="white", size=0.2) + theme_bw() + theme(panel.border = element_blank(), panel.grid.major = element_blank(),
               panel.grid.minor = element_blank()) + scale_fill_gradient2(limits = c(0, 100), oob = scales::squish)
m14_50<-m14_50 + guides(fill=guide_legend(title = "% Taking Medication for High Blood Pressure")) + ggtitle("2014, Individuals Aged 50-54")
ggsave("m14_50.png")

m14_55<-ggplot() + geom_polygon(data=merged2014_55, aes(x=long, y=lat, group=group, fill=Taking.medication.for.high.blood.pressure),
               color="white", size=0.2) + theme_bw() + theme(panel.border = element_blank(), panel.grid.major = element_blank(),
               panel.grid.minor = element_blank()) + scale_fill_gradient2(limits = c(0, 100), oob = scales::squish)
m14_55<-m14_55 + guides(fill=guide_legend(title = "% Taking Medication for High Blood Pressure")) + ggtitle("2014, Individuals Aged 55-59")
ggsave("m14_55.png")

m14_60<-ggplot() + geom_polygon(data=merged2014_60, aes(x=long, y=lat, group=group, fill=Taking.medication.for.high.blood.pressure),
               color="white", size=0.2) + theme_bw() + theme(panel.border = element_blank(), panel.grid.major = element_blank(),
               panel.grid.minor = element_blank()) + scale_fill_gradient2(limits = c(0, 100), oob = scales::squish)
m14_60<-m14_60 + guides(fill=guide_legend(title = "% Taking Medication for High Blood Pressure")) + ggtitle("2014, Individuals Aged 60-64")
ggsave("m14_60.png")

m14_65<-ggplot() + geom_polygon(data=merged2014_65, aes(x=long, y=lat, group=group, fill=Taking.medication.for.high.blood.pressure),
               color="white", size=0.2) + theme_bw() + theme(panel.border = element_blank(), panel.grid.major = element_blank(),
               panel.grid.minor = element_blank()) + scale_fill_gradient2(limits = c(0, 100), oob = scales::squish)
m14_65<-m14_65 + guides(fill=guide_legend(title = "% Taking Medication for High Blood Pressure")) + ggtitle("2014, Individuals Aged 65+")
ggsave("m14_65.png")
```
Once all the images were generated, I simply looped them into gifs with free online editing software. Here is an example of the gif for the percent of individuals currently smoking in each state, for each older age group, and for each year 2011-2014. The others are posted as files.
![CurrentSmoking](https://user-images.githubusercontent.com/121974615/211622429-ac56187e-a020-47d3-bbf1-33d43f21a22b.gif)


