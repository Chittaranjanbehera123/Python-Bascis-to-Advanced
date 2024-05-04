import pandas as pd

# create asample dataframe 
df = pd.DataFrame({'Name':['John','Emma','Peter','Maria'],
                   'Age':[25, 30, 20, 35],
                   'Gender':['male','Female','Male','Female']})

# Print the dataframe 
print(df)

df.to_csv("sample.csv")

#Read a csv file into a dataframe 
csv_df = pd.read_csv('sample.csv')

# print the dataframe
print(csv_df)

