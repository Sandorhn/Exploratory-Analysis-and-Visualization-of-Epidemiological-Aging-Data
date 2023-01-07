#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Machine Learning Techniques to know
#Linear Regression, logistic regression, decision trees, random forest, 
#a couple different neural nets, some sott of pca or umap, clustering

#Do some visualization in tableau or powerBi

#projects to do for github:
#1 this one, a complete exploratory analysis of multivariate aging data presented as a story
#2 redo your miRNA analysis in python and post those original datasets on github DONE
#3 do a machine learning drug discovery thing using that tutorial
#4 Do a discovery analysis of blood biomarkers for aging and submit it to the longevity prize

# import pandas lib as pd
import pandas as pd

# read by default 1st sheet of an excel file
dataframe1 = pd.read_csv('rows.csv')
display(dataframe1)
#i think my hypothesis is that in northern states there will be more different rates of distress between the 
#races while in southern states the rates of destress will be more equal in the elderly due to vit D
#deficiency YOU CANT ACTUALLY DO THIS BECUASE THE DATA IS EITHER FOR STATES OR FOR US IN GENERAL FEMALE
#MALE, AND RACE, THERE IS NO DATA ON THE RACE OF EACH STATES


# In[2]:


#lets clean this up a bit first by deleting duplicate rows
dataframe1_1 = dataframe1.drop(
    labels=["Datasource", "Response", "DataValueTypeID", "Data_Value_Type", "Data_Value_Alt", 
            "Sample_Size"],
    axis=1
)

display(dataframe1_1)


# In[3]:


#i want to find out how many unique topics there are and seperate them into seperate dataframes for
#analysis
#dataframe1_1.Topic.unique() #32, wow, what about class?
#dataframe1_1.Class.unique() #6, ok so if you dont do "().size" it tells you what they are instead of 
#just count them

#this dataset contains information for each state plus several US territories for certain age groups 
#over 50 in age gaps of 5 years. There are 4 groups in total, 50-55, 55-60, 60-65, 65+
#so you can try to develop a model that predicts mental health and life satisfaction at 65+ based on
#behaviour in their 50s

#these are the 32 variables
#'Frequent mental distress', 'Disability status',
#        'Fall with injury within last year',
#        'Oral health:  tooth retention',
#        'Lifetime diagnosis of depression', 'Physically unhealthy days',
#        'Ever had pneumococcal vaccine',
#        'Binge drinking within past 30 days',
#        'Social and emotional support',
#        'Prevalence of sufficient sleep (>6 hours)', 'Obesity',
#        'Up-to-date with recommended vaccines and screenings - Men',
#        'Mammogram within past 2 years', 'Colorectal cancer screening',
#        'Current smoking',
#        'No leisure time physical activity within past month',
#        'Life satisfaction', 'Influenza vaccine within past year',
#        'Diabetes screening within past 3 years',
#        'Pap test within past 3 years',
#        'Self-rated health (fair to poor health)',
#        'Self-rated health (good to excellent health)',
#        'Recent activity limitation in past month',
#        'Eating 2 or more fruits daily',
#        'Eating 3 or more vegetables daily',
#        'Taking medication for high blood pressure',
#        'Cholesterol checked in past 5 years', 'High blood pressure ever',
#        'Lifetime diagnosis of anxiety disorder',
#        'Increased confusion or memory loss (ICML) among older adults',
#        'Functional difficulties associated with increased confusion or memory loss (ICML) among older adults',
#        'UTD preventive services (women)' 

#you need to pick only 1 years worth of data because its fucking ur shit up
dataframe1_1.groupby("YearEnd").count()
#ok so lets just do 2014


# In[4]:


#We should keep cleaning up the data - there is never any data available for the virgin islands, so i
#will delete any rows that contain that
dataframe1_2 = dataframe1_1[dataframe1_1["LocationDesc"].str.contains("Virgin Islands")==False]
display(dataframe1_2)


# In[5]:


#K now get rid of anything that isnt 2014
dataframe1_3 = dataframe1_2[dataframe1_2["YearEnd"]==2014]
dataframe1_3


# In[6]:


#QUESTION 1: WHAT CAN WE PREDICT ABOUT QUALITY OF LIFE IN OUR 60S BASED ON OUR BEHAVIOUR IN OUR 50S
#USING EACH STATE AS AN INDEPENDANT DATAPOINT

#You should identify which variables you want to be predictive, and which you want to predict
#then divide the dataset into 50-55 and 60-65 training, and 55-60, 65+ test datasets. So split them in
#2, and you can use each state as an independant datapoint 
#You cna maybe do something with race and gender in USA in general later.

#The Variables that you want to predict in the 60s are Frequent mental distress, life satisfaction
#functional difficulties associated with memory loss, self-rated health, 

#I want to avoid variables related to recently receiving healthcare because they would either be 
#indicative that the person recently acquired symptoms, or they could indicate that they take care of
#themselves more in general, so I could not say whether or not they should be predictors or what is
#being predicted. also 'recent activity limitation' and lack of sleep, it is hard to know if lack of
#sleep should be classified as a negative outcome or a predictor, and the recent activity limitation
# at 65+ could mean that they did well to not have that happen until now, while the unhealthy people
#has it happen a long time ago. I think I will stick to trying to predict those 4, and let all the 
#other variables be predictors.

#for this analysis, first we will drop any records that are for US in general
experiment1 = dataframe1_3[dataframe1_3["LocationDesc"].str.contains("United States")==False]
experiment1


# In[7]:


#ok good, now lets get rid of all the columns with nan readings only
# experiment1 = experiment1.dropna(axis=1)
# experiment1


# In[8]:


#ok good, now lets split this into training and test datasets
experiment1_train = experiment1[experiment1["Stratification1"].str.contains("4 years")==True]
experiment1_train

experiment1_test = experiment1[experiment1["Stratification1"].str.contains("4 years")==False]
experiment1_test
#ok awesome. now you need to set up your data so that u can actually do tests on it


# In[9]:


#Divide these test and train datasets into targets with age groups
experiment1_train_data = experiment1_train[experiment1_train["Stratification1"].str.contains("54 years")==True]
display(experiment1_train_data)

experiment1_train_targets = experiment1_train[experiment1_train["Stratification1"].str.contains("54 years")==False]
experiment1_train_targets


# In[10]:


#You want to build a new dataframe for the experiment1_train, that makes each of the categories within
#'topic' a column in a new dataframe, and the corresponding data values for the states within each
#variable are the n readings

#so all of whats before is within creating the new dataframe, since there is only 1 column with 
#numbers we are interested in, but we need to reshape them in the format of the number of new rows
#we want which is equal to the number of unique values for states for rows and the number of unique
#topics for columns. But then we need to transpose the column data so that it moves laterally. THen,
#finally now that the data is in place we need to simply give the index(or row names) and column
#names those unique values.
ex_train_var = pd.DataFrame(experiment1_train_data["Data_Value"].to_numpy().reshape(len(experiment1_train_data.Topic.unique()),len(experiment1_train_data.LocationDesc.unique())).T,index = experiment1_train_data.LocationDesc.unique(),columns = experiment1_train_data.Topic.unique())
ex_train_var
#this data table transformation makes the data much easier to work with.


# In[11]:


#Ok now lets do this for our targets
ex_train_targs = pd.DataFrame(experiment1_train_targets["Data_Value"].to_numpy().reshape(len(experiment1_train_targets.Topic.unique()),len(experiment1_train_targets.LocationDesc.unique())).T,index = experiment1_train_targets.LocationDesc.unique(),columns = experiment1_train_targets.Topic.unique())
ex_train_targs


# In[12]:


#Ok for the target dataset lets just keep the 2 variables of interest
targs_train = ex_train_targs[["Life satisfaction", "Frequent mental distress"]]
targs_train


# In[13]:


#We now have to deal with the NaNs before we can proceed
import numpy as np

X_train = ex_train_var.replace(np. nan, 0)
Y_train = targs_train.replace(np. nan, 0)


# In[14]:


X_train.shape, Y_train.shape


# In[15]:


from sklearn import linear_model
from sklearn.metrics import mean_squared_error, r2_score

#build the linear regression model
model = linear_model.LinearRegression()


# In[16]:


#ok now lets actually add our stuff to the model
model.fit(X_train, Y_train)


# In[24]:


#Ok this doesnt actually show anything, it just silently trained the model, so now to see how good a 
#predictor it is we need our test datasets to be in the same format
experiment1_test
#So first we take this and split it into data and targets
experiment1_test_data = experiment1_test[experiment1_test["Stratification1"].str.contains("59 years")==True]
display(experiment1_test_data)
experiment1_test_targets = experiment1_test[experiment1_test["Stratification1"].str.contains("59 years")==False]
experiment1_test_targets
#ok perfect, now reorganize the dataframes as you did with the training sets
ex_test_var = pd.DataFrame(experiment1_test_data["Data_Value"].to_numpy().reshape(len(experiment1_test_data.Topic.unique()),len(experiment1_test_data.LocationDesc.unique())).T,index = experiment1_test_data.LocationDesc.unique(),columns = experiment1_test_data.Topic.unique())
ex_test_var
ex_test_targs = pd.DataFrame(experiment1_test_targets["Data_Value"].to_numpy().reshape(len(experiment1_test_targets.Topic.unique()),len(experiment1_test_targets.LocationDesc.unique())).T,index = experiment1_test_targets.LocationDesc.unique(),columns = experiment1_test_targets.Topic.unique())
ex_test_targs
#ok good. now just do that thing for the targets only
targs_test = ex_test_targs[["Life satisfaction", "Frequent mental distress"]]
targs_test
#unfortunetely, life satisfaction for over 65 is seldom measured, and it is mostly nan, but we can
#still get a prediction for frequent mental distress.
X_test = ex_test_var.replace(np. nan, 0)
Y_test = targs_test.replace(np. nan, 0)
X_train.shape, Y_train.shape


# In[26]:


#Ok, now the prediction of y, we dont actually need data for life satisfaction other than to check
#if the prediction is correct
Y_pred = model.predict(X_test)


# In[27]:


#ok so now the prediction has been made, and we need to check how well it worked.
print('Coefficients:', model.coef_)
print('Intercept:', model.intercept_)
print('Mean squared error (MSE): %.2f'
      % mean_squared_error(Y_test, Y_pred))
print('Coefficient of determination (R^2): %.2f'
      % r2_score(Y_test, Y_pred))

#each coefficiant shows you how well each of the variables are predictive of each target defined in the
#square brackets


# In[41]:


#Ok lets try to plot this
import seaborn as sns
Y_test = np.array(Y_test)
np.array(Y_pred)
sns.scatterplot(Y_test.T[1], Y_pred.T[1])
#these are 2D arrays, while sns expects a 1d array
#so basically this is a bad model for predicting frequent panic attacks which is unsurprising.
#instead what you could do is use things in certain age groups and see if they are predictive of things
#in other age groups.


# In[39]:


#Ok so that didn't work, now lets try some simpler things to get our confidence back.
#Lets see how well smoking predicts teeth falling out in our 50s, and see if that is predictive of 
#Smoking making our teeth fall out in our 60s.


