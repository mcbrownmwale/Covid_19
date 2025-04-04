#### Investgating Covid-19 Trends ####

# Import Libraries
## Import Pandas and Numpy for data manipulation and wrangling
import pandas as pd
import numpy as np
import ancillary_func as an

# Import matplotlib and seaborn for data visualisation
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_theme(style = 'white', palette = 'muted')

# Read in Data
covid = pd.read_csv('covid_19.csv')

# Display the first five records of the first five columns
an.get_table(covid.iloc[:, :5].head())

# Inspect Data
## Display DataFrame's dimensions
shape = covid.shape
print(f"Our dataset has {shape[0]} rows and {shape[1]} columns.")

# Understanding Variables
## View general information
df_info = an.df_info_table(covid)
an.get_table(df_info)

# Check for duplicated rows
covid.duplicated().sum()

# Summary Statistics for numeric columns
an.get_table(covid.describe())

# Summary Statistics for qualitative columns
an.get_table(covid.describe(include = ['object']))

# Cleaning Column names
## making column names all lowercase
covid.columns = covid.columns.str.lower()

## renaming hospitalized column
covid.rename(columns = {'hospitalizedcurr': 'hospitalized_curr'}, inplace = True)

## Display the cleaned column names
for i in covid.columns:
    print(i)

# Change columns data type
## Convert data column to datetime datatype
covid['date'] = pd.to_datetime(covid['date'])

## Display the datatype for date column
print(covid['date'].dtype)    

# Isolate the data we need
## All states data
covid_all_states = covid[covid['province_state'] == 'All States'].reset_index(drop = True)
shape = covid_all_states.shape

## Display the dimensions
print(f"New number of rows is {shape[0]}.",
       f"The number of columns is maintained, we still have {shape[1]} columns.", sep='\n')

## Columns related to cummulative measures
covid_all_states_cummulative = covid_all_states[['date', 'continent_name', \
                                                 'two_letter_country_code', 'positive',\
                                                 'hospitalized', 'recovered', 'death', 'total_tested']]

## Columns related to daily measures
covid_all_states_daily = covid_all_states[['date', 'country_region', 'active', 'hospitalized_curr', 'daily_tested', 'daily_positive']]

## View the dimensions of the the datasets to confirm if filtering has been successful
print(covid_all_states_cummulative.shape, covid_all_states_daily.shape, sep='\n')

# Find Countries with highest number of covid deaths
## A pivot table for cummulative deaths by country
covid_deaths_cum = covid_all_states_cummulative.\
pivot_table(values = 'death', index = 'two_letter_country_code', 
            aggfunc = 'max').sort_values(by = 'death', ascending = False).head(10)
covid_deaths_cum.index = ['United States', 'Italy', 
                          'United Kingdom', 'Belgium', 'Russua', 'Turkey', 'Sweden', 'Canada', 'New Zealand', 'Poland']
covid_deaths_cum.columns = ['Cummulative Deaths']
covid_deaths_cum.reset_index(inplace = True)
covid_deaths_cum.rename(columns = {'index': 'Country Name'}, inplace = True)
an.get_table(covid_deaths_cum)

## Visualize countries with the highest numbers of covid deaths
sns.barplot(data = covid_deaths_cum, orient = 'h', x = 'Cummulative Deaths',
             y = covid_deaths_cum.index, hue = 'Cummulative Deaths')
sns.despine(left = True, bottom = True)
plt.ylabel('')
plt.xlabel('')
plt.xticks([0, 40000, 80000 ], ['0', '40,000', '80,000'])
plt.tick_params(labelcolor = 'gray')
plt.tick_params(labeltop = True, labelbottom = False)
plt.text(x = -25000, y = -2.6, s = 'Top Ten Countries with Higher Cummulative Covid-19 Deaths',
          fontdict = {'weight':'bold', 'family':'serif'})
plt.text(x = -25000, y = -2, s = 'United States is the Country that recorded highest Cummulative Deaths',\
         fontdict = {'weight':'bold', 'family':'serif', 'color':'gray'})
plt.show()

# Finding the Top Ten Tested Countries
## Determine the top ten tested cases
covid_all_states_daily_sum = covid_all_states_daily.groupby('country_region')[['active', 'hospitalized_curr', 'daily_tested', 'daily_positive']].sum()
covid_all_states_daily_sum.rename(columns={'daily_tested':'tested', 'daily_positive':'positive', 'hospitalized_curr':'hospitalized'}, inplace = True)
covid_all_states_daily_sum_sorted = covid_all_states_daily_sum.sort_values(by = 'tested', ascending = False)
covid_top_ten = covid_all_states_daily_sum_sorted.head(10)
covid_top_ten.index.name = None
an.get_table(covid_top_ten)

## Visualize the top ten tested countries
sns.barplot(data=covid_top_ten, orient = 'h', x='tested', y=covid_top_ten.index, hue = 'tested')
sns.despine(left = True, bottom = True)
plt.ticklabel_format(axis = 'x', style = 'plain')
plt.xticks([2500000, 7500000, 12500000, 17500000], ['2,500,000', '7,500,000', '12,500,000', '17,500,000'])
plt.text(x = -4000000, y = -2.6, s = 'Top Ten Countries with Higher Volumes of Covid-19 Tests', fontdict = {'weight':'bold', 'family':'serif'})
plt.text(x = -4000000, y = -2, s = 'The United States conducted more Covid-19 tests than any other country',\
         fontdict = {'weight':'bold', 'family':'serif', 'color':'gray'})
plt.tick_params(labeltop = True, labelbottom = False)
plt.tick_params(labelcolor = 'gray')
plt.ylabel('')
plt.xlabel('')
plt.show()

# Identifying the highest testes against the positives
positivity_rated = covid_top_ten.copy()
positivity_rated['positivity_rate'] = (positivity_rated['positive']/positivity_rated['tested'])*100
top_ten_positivity_rated = positivity_rated.sort_values(by='positivity_rate', ascending = False).head(10)['positivity_rate'].reset_index()
top_ten_positivity_rated.rename(columns = {'index': 'Country Name'}, inplace = True) 
an.get_table(top_ten_positivity_rated)

# Visualization
sns.barplot(data = top_ten_positivity_rated, x = 'positivity_rate',\
             y = 'Country Name', orient = 'h', hue = 'positivity_rate')
sns.despine(left = True, bottom = True)
plt.text(x = -3, y = -2.6, s = 'Positivity Rate among Countries with Higher Volumes of Covid-19 Tests', fontdict = {'weight':'bold', 'family':'serif'})
plt.text(x = -3, y = -2, s = 'The United Kingdom recorded the highest positivity rate',\
         fontdict = {'weight':'bold', 'family':'serif', 'color':'gray'})
plt.xticks([0, 2, 4, 6, 8, 10], ['0%', '2%', '4%', '6%', '8%', '10%'])
plt.tick_params(labelcolor = 'gray')
plt.ylabel('')
plt.xlabel('')
plt.tick_params(labeltop = True, labelbottom = False)
plt.grid(False)
plt.show()

# Scale data to population level
## Number of tested cases agaisnt total population
### population list
pop_dict = {'population':[331002651, 145934462, 60461826, 1380004385, 84339067, 37742154, 67886011, 25499884, 32971854, 37846611]}
pop = pd.DataFrame(pop_dict)
pop.index = ['United States', 'Russia', 'Italy', 'India', 'Turkey', 'Canada', 'United Kingdom', 'Australia', 'Peru', 'Poland']
covid_top_ten_pop = covid_top_ten
covid_top_ten_pop = pd.merge(left = covid_top_ten_pop, right = pop, left_index= True, right_index= True)
an.get_table(covid_top_ten_pop)

### Tested cases against total population
covid_top_ten_pop['percentage_tested'] = (covid_top_ten_pop['tested']/covid_top_ten_pop['population'])*100
an.get_table(covid_top_ten_pop[['tested', 'population', 'percentage_tested']])

# Variables as Fractions of their Population Levels
##
covid_top_ten_percentage = covid_top_ten_pop.iloc[:, :-1]
covid_top_ten_percentage['active'] = (covid_top_ten_percentage['active']/covid_top_ten_percentage['population'])*100
covid_top_ten_percentage['hospitalized'] = (covid_top_ten_percentage['hospitalized']/covid_top_ten_percentage['population'])*100
covid_top_ten_percentage['tested'] = (covid_top_ten_percentage['tested']/covid_top_ten_percentage['population'])*100
covid_top_ten_percentage['positive'] = (covid_top_ten_percentage['positive']/covid_top_ten_percentage['population'])*100
covid_top_ten_percentage.rename(columns = {'active':'active_cases', 'hospitalized':'hospitalized_cases',\
                                           'tested':'tested_cases', 'positive':'positive_cases'}, inplace = True)
covid_top_ten_percentage.drop('population', axis = 1, inplace = True)
an.get_table(covid_top_ten_percentage)

## 
covid_top_ten_percentage_ranked = covid_top_ten_percentage.rank()
covid_top_ten_percentage_ranked['total_ranked'] = covid_top_ten_percentage_ranked.sum(axis=1)
covid_top_ten_percentage_ranked.rename(\
    columns={'active_cases':'active_rank',\
             'hospitalized_cases':'hosp_rank',\
             'tested_case':'tested_rank', 'positive_cases':'pos_rank'}, inplace = True)
covid_top_ten_percentage_ranked.sort_values(by='total_ranked', ascending = False, inplace = True)
an.get_table(covid_top_ten_percentage_ranked)

######################################################### THE END #####################################################################################
