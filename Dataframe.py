import pandas as pd

# Create a sample dataframe
data = {'name': ['Apple', 'Bob', 'Charlie', 'David'],
        'Age': [25, 30, 20, 35],
        'country': ['USA', 'Canada', 'Australia', 'UK']}

# Create a pandas DataFrame from the Dictionary
df = pd.DataFrame(data)

# Print the dataframe
print(df)

# Read a csv file into a dataframe (assuming the file is 'sample.csv')
csv_df = pd.read_csv('sample.csv')

# Print the dataframe
print(csv_df)

# Group the dataframe by country and calculate the mean age
grouped_df = df.groupby('country').mean()

# Print the grouped dataframe
print(grouped_df)