import pandas as pd 
import os

data = {
    "Name" : ['Ayan','Anas', 'Arsalan'],
    "Age" : [22,22,27],
    "City" : ['Rourkela', 'Sundergarh', 'Dubai']
}

df = pd.DataFrame(data)

# Adding new row to df for version 2
new_row_loc = {'Name':'Sufian','Age':25,'City':'RGP'}
df.loc[len(df.index)] = new_row_loc

# Adding new row to df for version 3
new_row_loc2 = {'Name':'Saif','Age':24,'City':'RGP'}
df.loc[len(df.index)] = new_row_loc2

# Ensures that the data directory exist at the root level
data_dir = 'data'
os.makedirs(data_dir, exist_ok= True)

# Defining file path
file_path = os.path.join(data_dir, "sample_data.csv")

# Saving data frame to a csv file
df.to_csv(file_path,index=False)

print(f"csv file has been successfully saved to file path : {file_path}")
