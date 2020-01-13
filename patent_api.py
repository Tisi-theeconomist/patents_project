# -*- coding: utf-8 -*-
# Retrieving and preparing wind and solar data for 	REDUCTION OF GREENHOUSE GAS [GHG] EMISSIONS, RELATED TO ENERGY GENERATION, TRANSMISSION OR DISTRIBUTION - YO2E and 
#Integration of renewable energy sources in buildings - Y02B

import pandas as pd
import numpy as np
import requests
import json


# Reference
# #cpc_subsection = Y02
# #cpc_group = Y02E
# #subgroup = Y02E10/541

'''#Solar data'''
#Dynamic api to pull solar and wind data from patent view for single group/subgroup 
#Change title, abstract, start date, end date, group_id to get respective data
#to use subgroup_id instead of group_id just change "cpc_group_id" within data variable to "cpc_subgroup_id"

#Request solar data under group_id Y02E
abstract = "solar Photovoltaic PV"
start_date = "1990-01-04"
end_date = "2019-12-31"
group_id = "Y02E"
subgroup_id = ""
url = "https://www.patentsview.org/api/patents/query" 

data = { 
    "q":{ "_and":[ {"cpc_group_id":group_id}, {"_gte":{"patent_date":start_date}},
                  {"_lte":{"patent_date":end_date}}, {"_text_any":{"patent_abstract":abstract}}]},
    
    "f":["patent_title","patent_number", "patent_type","patent_date","patent_abstract",
         "patent_firstnamed_assignee_id", "patent_firstnamed_assignee_country", "patent_firstnamed_assignee_latitude",
         "patent_firstnamed_assignee_longitude","patent_firstnamed_assignee_city", "patent_firstnamed_inventor_latitude",
         "patent_firstnamed_inventor_longitude","patent_firstnamed_inventor_city", "patent_firstnamed_inventor_country",
         "patent_firstnamed_inventor_id", "assignee_organization", "assignee_id", "assignee_type", "assignee_total_num_patents"], 
    
    "o":{"page":1, "per_page":10000} 
}

#retrieve data from patentview
resp = requests.post(url, json=data)
#check status that it is working
resp.status_code
#load data
r= json.loads(resp.content)
r

#convert json data into dataframe
df= pd.DataFrame(list(r['patents']))
df.head(5)
#check items within assignees column
df.assignees.head(2).values.tolist()
#convert assignees lists into a dataframes
df2=df['assignees'].apply(lambda x: pd.DataFrame(x)) 
df2.head()
#merge assignees dataframes into one dataframe
df3= pd.DataFrame(np.concatenate(df2, axis=0),
                         columns= ['assignee_organization', 'assignee_key_id', 'assignee_type',
                                   'assignee_total_num_patents', 'assignee_key_id'])
df3.head()
#remove the assignees column from original dataframe
df = df[df.columns[:-1]]
df.head()
#save first 10,000 datapoint of solar patents and assignee data from group_id  Y02E  to csv
solar_patents_page1 = df.to_csv("solarY02E_patents.csv", header=True, index=False)
solar_assignees_page1 = df3.to_csv("solarY02E_assignee.csv", header=True, index=False)

#get the data above 10,000 - change api variable "o" to  "o":{"page":2, "per_page":10000} keep everything else the same
abstract = "solar Photovoltaic PV"
start_date = "1990-01-04"
end_date = "2019-12-31"
group_id = "Y02E"
subgroup_id = ""
url = "https://www.patentsview.org/api/patents/query" 

data = { 
    "q":{ "_and":[ {"cpc_group_id":group_id}, {"_gte":{"patent_date":start_date}},
                  {"_lte":{"patent_date":end_date}}, {"_text_any":{"patent_abstract":abstract}}]},
    
    "f":["patent_title","patent_number", "patent_type","patent_date","patent_abstract",
         "patent_firstnamed_assignee_id", "patent_firstnamed_assignee_country", "patent_firstnamed_assignee_latitude",
         "patent_firstnamed_assignee_longitude","patent_firstnamed_assignee_city", "patent_firstnamed_inventor_latitude",
         "patent_firstnamed_inventor_longitude","patent_firstnamed_inventor_city", "patent_firstnamed_inventor_country",
         "patent_firstnamed_inventor_id","assignee_organization", "assignee_id", "assignee_type", "assignee_total_num_patents"], 
    
    "o":{"page":2, "per_page":10000} 
}

#retrieve data from patentview
resp = requests.post(url, json=data)
#load retrieved json data
r= json.loads(resp.content)
#convert json data into dataframe
df= pd.DataFrame(list(r['patents']))
#convert assignees lists into a dataframes
df2=df['assignees'].apply(lambda x: pd.DataFrame(x)) 
#merge assignees dataframes into one dataframe
df3= pd.DataFrame(np.concatenate(df2, axis=0),
                         columns= ['assignee_organization', 'assignee_key_id','assignee_type',
                                   'assignee_total_num_patents', 'assignee_key_id'])
#remove the assignees column from original dataframe
df = df[df.columns[:-1]]
#save solar patent and assignee data  from group_id Y02E to csv 
solar_patents_page2 = df.to_csv("solarY02E_patents_page2.csv", header=True, index=False)
solar_assignees_page2 = df3.to_csv("solarY02E_assignee_page2.csv", header=True, index=False)

#Dynamic api to pull solar and wind data from patent view for multiple group/subgroup
#Change title, abstract, start date, end date, group_id to get respective data
#We are pulling data under Y02B for subgroups under "integration of renewable energy sources in buildings"
abstract = "photovoltaic PV roof solar"
start_date = "1990-01-04"
end_date = "2019-12-31"
subgroup_id_0 = "Y02B10/00"
subgroup_id_1 = "Y02B10/10"
subgroup_id_2 = "Y02B10/12"
subgroup_id_3 = "Y02B10/14"
subgroup_id_4 = "Y02B10/20"
subgroup_id_5 = "Y02B10/22"
subgroup_id_6 = "Y02B10/24"
subgroup_id_7 = "Y02B10/70"
subgroup_id_8 = "Y02B10/72"
url = "https://www.patentsview.org/api/patents/query" 

data = { 
    "q":{"_or":[{ "_and":[ {"cpc_subgroup_id":subgroup_id_0}, {"_gte":{"patent_date":start_date}},
                  {"_lte":{"patent_date":end_date}}, {"_text_any":{"patent_abstract":abstract}}]},
                { "_and":[ {"cpc_subgroup_id":subgroup_id_1}, {"_gte":{"patent_date":start_date}},
                  {"_lte":{"patent_date":end_date}}, {"_text_any":{"patent_abstract":abstract}}]},
              { "_and":[ {"cpc_subgroup_id":subgroup_id_2}, {"_gte":{"patent_date":start_date}},
                  {"_lte":{"patent_date":end_date}}, {"_text_any":{"patent_abstract":abstract}}]},
               { "_and":[ {"cpc_subgroup_id":subgroup_id_3}, {"_gte":{"patent_date":start_date}},
                  {"_lte":{"patent_date":end_date}}, {"_text_any":{"patent_abstract":abstract}}]},
               { "_and":[ {"cpc_subgroup_id":subgroup_id_4}, {"_gte":{"patent_date":start_date}},
                  {"_lte":{"patent_date":end_date}}, {"_text_any":{"patent_abstract":abstract}}]},
                { "_and":[ {"cpc_subgroup_id":subgroup_id_5}, {"_gte":{"patent_date":start_date}},
                  {"_lte":{"patent_date":end_date}}, {"_text_any":{"patent_abstract":abstract}}]},
                { "_and":[ {"cpc_subgroup_id":subgroup_id_6}, {"_gte":{"patent_date":start_date}},
                  {"_lte":{"patent_date":end_date}}, {"_text_any":{"patent_abstract":abstract}}]},
               { "_and":[ {"cpc_subgroup_id":subgroup_id_7}, {"_gte":{"patent_date":start_date}},
                  {"_lte":{"patent_date":end_date}}, {"_text_any":{"patent_abstract":abstract}}]},
               { "_and":[ {"cpc_subgroup_id":subgroup_id_8}, {"_gte":{"patent_date":start_date}},
                  {"_lte":{"patent_date":end_date}}, {"_text_any":{"patent_abstract":abstract}}]}]},
    
    "f":["patent_title","patent_number", "patent_type","patent_date","patent_abstract",
         "patent_firstnamed_assignee_id", "patent_firstnamed_assignee_country", "patent_firstnamed_assignee_latitude",
         "patent_firstnamed_assignee_longitude","patent_firstnamed_assignee_city", "patent_firstnamed_inventor_latitude",
         "patent_firstnamed_inventor_longitude","patent_firstnamed_inventor_city", "patent_firstnamed_inventor_country",
         "patent_firstnamed_inventor_id","assignee_organization", "assignee_id", "assignee_type", "assignee_total_num_patents"], 
    
    "o":{"per_page":10000} 
}

#retrieve data from patentview
resp = requests.post(url, json=data)
#check status that it is working
resp.status_code
#load retrieved json data
r= json.loads(resp.content)
r
#convert json data into dataframe
df= pd.DataFrame(list(r['patents']))
df.head()
#check items within assignees column
df.assignees.head(2).values.tolist()
#convert assignees lists into a dataframes
df2=df['assignees'].apply(lambda x: pd.DataFrame(x)) 
df2[0]
#merge assignees dataframes into one dataframe
df3= pd.DataFrame(np.concatenate(df2, axis=0),
                         columns= ['assignee_organization', 'assignee_key_id','assignee_type', 
                                   'assignee_total_num_patents', 'assignee_key_id'])
df3.head()
#remove the assignees column from original dataframe
df = df[df.columns[:-1]]
df.head()
#save solar patent and assignee data to csv from Y02B - filter words  "photovoltaic PV roof solar"
solarY02B_patents = df.to_csv("solarY02B_patents.csv", header=True, index=False)
solarY02B_assignees = df3.to_csv("solarY02B_assignee.csv", header=True, index=False)

'''#Further Solar Data Preparation'''
# ## Solar data preparation
#import retrieved page 1 and page 2 solar data for group YO2E
solar_df1 = pd.read_csv("solarY02E_patents.csv")
solar_df2 = pd.read_csv("solarY02E_patents_page2.csv")
#merge the two dataframes
solar = pd.concat([solar_df1, solar_df2], sort = False)
#inspect the merged data
solar.head()
#check if the rows are unique
solar.nunique()

#import retrieved page 1 and page 2 solar patent assignee data for group Y02E
solar_assignee_df1 = pd.read_csv("solarY02E_assignee.csv")
solar_assignee_df2 = pd.read_csv("solarY02E_assignee_page2.csv")
#merge the two assignee dataframes
solar_assignee = pd.concat([solar_assignee_df1, solar_assignee_df2], sort = False)
#inspect the merged data
solar_assignee.head()
#check how many rows are unique - we don't need duplicate in this dataframe
solar_assignee.nunique()

#get the unique values (rows) by subsetting on the variable we are going to use to merge the dataframe later
solar_assignee_unique = solar_assignee.drop_duplicates(subset=['assignee_key_id'])
solar_assignee_unique
#reset the index
solar_assignee_unique.reset_index(inplace= True, drop=True)
#inspect the data with new index
solar_assignee_unique.head(5)

#Interested in having all information from solar_assignee_unique dataframe except assignee_key_id.1 populated in solar dataframe. Start merging preparation by recalling the solar data 
solar.head(1)
#Using "patent_firstnamed_assignee_id" from solar dataframe and assignee_key_id from solar_assignee_unique dataframe the two dataframes can be merged. 
#Basically we are looking up "patent_firstnamed_assignee_id" information in solar_assignee_unique dataframe 
#Add "assignee_key_id" column to the solar dataframe
solar['assignee_key_id'] = solar['patent_firstnamed_assignee_id']
#check information of the solar dataframe
solar.info()
#check the merging criteria
solar['assignee_key_id'].isin(solar_assignee_unique['assignee_key_id']).value_counts()
#merge the two dataframes using 'assignee_key_id'
df_solar = pd.merge(solar, solar_assignee_unique[['assignee_key_id', 'assignee_organization', 
                                        'assignee_type', 'assignee_total_num_patents' ]],
                  on='assignee_key_id')
#inspect the merged data
df_solar.info()

# ### Prepare Solar Data from group Y02B which related to buildings renewable integration. The same steps used in Y02E above applies here
#import retrieved  solar data 
solar_building = pd.read_csv("solarY02B_patents.csv")
#inspect the data
solar_building.head(2)
#import retrieved solar patent assignee data 
solar_assignee_building = pd.read_csv("solarY02B_assignee.csv")
#inspect the data
solar_assignee_building.head()
#check how many rows are unique - we don't need duplicate in this dataframe
solar_assignee_building.nunique()

#merge data
#get the unique values (rows) by subsetting on the variable we are going to use to merge the dataframe later
solar_assignee_building_unique = solar_assignee_building.drop_duplicates(subset=['assignee_key_id'])
#reset the index
solar_assignee_building_unique.reset_index(inplace= True, drop=True)
#inspect the data with new index
solar_assignee_building_unique.head(5)

#Add "assignee_key_id" column to the solar dataframe
solar_building['assignee_key_id'] = solar_building['patent_firstnamed_assignee_id']
solar_building.head(2)
#check the merging criteria
solar_building['assignee_key_id'].isin(solar_assignee_building_unique['assignee_key_id']).value_counts()
#merge the two dataframes using 'assignee_key_id' 
df_solar_building = pd.merge(solar_building, solar_assignee_building_unique[['assignee_key_id', 'assignee_organization', 
                                        'assignee_type', 'assignee_total_num_patents' ]],
                  on='assignee_key_id')
df_solar_building.head()
#inspect the merged data
df_solar_building.info()
#save solar patent to csv
solargen_data = df_solar.to_csv("solargen.csv", header=True, index=False)
solarbuild_data = df_solar_building.to_csv("solarbuild.csv", header=True, index=False)


''' WIND'''
## Wind Patent Data
#Request wind data under group_id Y02E
#Change api request abstract variable to wind filter words ("wind nacelle nacelles") keep everything else the same

abstract = "wind nacelle nacelles"
start_date = "1990-01-04"
end_date = "2019-12-31"
group_id = "Y02E"
subgroup_id = ""
url = "https://www.patentsview.org/api/patents/query" 

data = { 
    "q":{ "_and":[ {"cpc_group_id":group_id}, {"_gte":{"patent_date":start_date}},
                  {"_lte":{"patent_date":end_date}}, {"_text_any":{"patent_abstract":abstract}}]},
    
    "f":["patent_title","patent_number", "patent_type","patent_date","patent_abstract",
         "patent_firstnamed_assignee_id", "patent_firstnamed_assignee_country", "patent_firstnamed_assignee_latitude",
         "patent_firstnamed_assignee_longitude","patent_firstnamed_assignee_city", "patent_firstnamed_inventor_latitude",
         "patent_firstnamed_inventor_longitude","patent_firstnamed_inventor_city", "patent_firstnamed_inventor_country",
         "patent_firstnamed_inventor_id","assignee_organization", "assignee_id", "assignee_type", "assignee_total_num_patents"], 
    
    "o":{"page":2, "per_page":10000} 
}

#retrieve data from patentview
resp = requests.post(url, json=data)
#load retrieved json data
r= json.loads(resp.content)
#convert json data into dataframe
df= pd.DataFrame(list(r['patents']))
#convert assignees lists into a dataframes
df2=df['assignees'].apply(lambda x: pd.DataFrame(x)) 
#merge assignees dataframes into one dataframe
df3= pd.DataFrame(np.concatenate(df2, axis=0),
                         columns= ['assignee_organization', 'assignee_key_id', 'assignee_type', 
                                   'assignee_total_num_patents', 'assignee_key_id'])
#remove the assignees column from original dataframe
df = df[df.columns[:-1]]
#save wind patent and assignee data from group_id Y02E to csv
windY02E_patents = df.to_csv("windY02E_patents.csv", header=True, index=False)
windY02E_assignees = df3.to_csv("windY02E_assignee.csv", header=True, index=False)

#Dynamic api to pull solar and wind data from patent view for multiple group/subgroup
#Change title, abstract, start date, end date, group_id to get respective data
# We are pulling data under Y02B for subgroups under "integration of renewable energy sources in buildings"

abstract = "wind nacelle nacelles"
start_date = "1990-01-04"
end_date = "2019-12-31"
subgroup_id_0 = "Y02B10/24"
subgroup_id_1 = "Y02B10/30"
subgroup_id_2 = "Y02B10/70"
subgroup_id_3 = "Y02B10/72"

url = "https://www.patentsview.org/api/patents/query" 

data = { 
    "q":{"_or":[{ "_and":[ {"cpc_subgroup_id":subgroup_id_0}, {"_gte":{"patent_date":start_date}},
                  {"_lte":{"patent_date":end_date}}, {"_text_any":{"patent_abstract":abstract}}]},
               { "_and":[ {"cpc_subgroup_id":subgroup_id_1}, {"_gte":{"patent_date":start_date}},
                  {"_lte":{"patent_date":end_date}}, {"_text_any":{"patent_abstract":abstract}}]},
                 { "_and":[ {"cpc_subgroup_id":subgroup_id_2}, {"_gte":{"patent_date":start_date}},
                  {"_lte":{"patent_date":end_date}}, {"_text_any":{"patent_abstract":abstract}}]},
                  { "_and":[ {"cpc_subgroup_id":subgroup_id_3}, {"_gte":{"patent_date":start_date}},
                  {"_lte":{"patent_date":end_date}}, {"_text_any":{"patent_abstract":abstract}}]}]},
    
    "f":["patent_title","patent_number", "patent_type","patent_date","patent_abstract",
         "patent_firstnamed_assignee_id", "patent_firstnamed_assignee_country", "patent_firstnamed_assignee_latitude",
         "patent_firstnamed_assignee_longitude","patent_firstnamed_assignee_city", "patent_firstnamed_inventor_latitude",
         "patent_firstnamed_inventor_longitude","patent_firstnamed_inventor_city", "patent_firstnamed_inventor_country",
         "patent_firstnamed_inventor_id","assignee_organization", "assignee_id", "assignee_type", "assignee_total_num_patents"], 
    
    "o":{"per_page":10000} 
}


#retrieve data from patentview
resp = requests.post(url, json=data)

#load retrieved json data
r= json.loads(resp.content)

#convert json data into dataframe
df= pd.DataFrame(list(r['patents']))

#convert assignees lists into a dataframes
df2=df['assignees'].apply(lambda x: pd.DataFrame(x)) 

#merge assignees dataframes into one dataframe
df3= pd.DataFrame(np.concatenate(df2, axis=0),
                         columns= ['assignee_organization', 'assignee_key_id','assignee_type',
                                   'assignee_total_num_patents', 'assignee_key_id'])

#remove the assignees column from original dataframe
df = df[df.columns[:-1]]
df.head(5)

#save wind patent and assignee data to csv from Y02B filter words "wind nacelle nacelles"
windY02B_patents = df.to_csv("windY02B_patents.csv", header=True, index=False)
windY02B_assignees = df3.to_csv("windY02B_assignee.csv", header=True, index=False)

# ## Wind data preparation 
# ### Wind Y02E Group data preparation
# #### repeate the previous steps

#import retrieved  wind data 
wind = pd.read_csv("windY02E_patents.csv")
#inspect the data
wind.head(2)

#import retrieved solar patent assignee data 
wind_assignee = pd.read_csv("windY02E_assignee.csv")
#inspect the data
wind_assignee.head()
#inspect the data
wind_assignee.info()
#check how many rows are unique - we don't need duplicate in this dataframe
wind_assignee.nunique()

#get the unique values (rows) by subsetting on the variable we are going to use to merge the dataframe later
wind_assignee_unique = wind_assignee.drop_duplicates(subset=['assignee_key_id'])
#reset the index
wind_assignee_unique.reset_index(inplace= True, drop=True)
#inspect the data with new index
wind_assignee_unique.head(5)
#Add "assignee_key_id" column to the wind dataframe
wind['assignee_key_id'] = wind['patent_firstnamed_assignee_id']
wind.head(2)
#check the merging criteria
wind['assignee_key_id'].isin(wind_assignee_unique['assignee_key_id']).value_counts()
#merge the two dataframes using 'assignee_key_id' 
df_wind = pd.merge(wind, wind_assignee_unique[['assignee_key_id', 'assignee_organization', 
                                        'assignee_type', 'assignee_total_num_patents' ]],
                  on='assignee_key_id')
#inspect the merged data
df_wind.info()

# ### Wind Y02B Group data preparation
#import retrieved  wind data 
wind_building = pd.read_csv("windY02B_patents.csv")
#inspect the data
wind_building.head(2)
#import retrieved solar patent assignee data 
wind_assignee_building = pd.read_csv("windY02B_assignee.csv")
#inspect the data
wind_assignee_building.head()
#inspect the data
wind_assignee_building.info()
#check how many rows are unique - we don't need duplicate in this dataframe
wind_assignee_building.nunique()
#get the unique values (rows) by subsetting on the variable we are going to use to merge the dataframe later
wind_assignee_building_unique = wind_assignee_building.drop_duplicates(subset=['assignee_key_id'])

#reset the index
wind_assignee_building_unique.reset_index(inplace= True, drop=True)
#inspect the data with new index
wind_assignee_building_unique.head(5)
#Add "assignee_key_id" column to the solar dataframe
wind_building['assignee_key_id'] = wind_building['patent_firstnamed_assignee_id']
wind_building.head(2)
#check the merging criteria
wind_building['assignee_key_id'].isin(wind_assignee_building_unique['assignee_key_id']).value_counts()
#merge the two dataframes using 'assignee_key_id' and default 
df_wind_building = pd.merge(wind_building, wind_assignee_building_unique[['assignee_key_id', 'assignee_organization', 
                                        'assignee_type', 'assignee_total_num_patents' ]],
                  on='assignee_key_id')
#inspect the merged data
df_wind_building.info()

#save wind patent and assignee data to csv from Y02B filter words "wind nacelle nacelles"
windgen_data = df_wind.to_csv("windgen.csv", header=True, index=False)
windbuild_data = df_wind_building.to_csv("windbuild.csv", header=True, index=False)



























