import pandas as pd

# Replace 'file.csv' with your file path
df = pd.read_csv('file.csv')

# Print the DataFrame
print(df)

# save the DataFrame to a new CSV file
df.to_csv('new_file.csv', index=False)
