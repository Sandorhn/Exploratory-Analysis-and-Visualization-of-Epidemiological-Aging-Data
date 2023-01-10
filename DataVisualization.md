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
