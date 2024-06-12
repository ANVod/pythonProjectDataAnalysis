import pandas as pd

data = {
                'name': ['Alice','Bob', 'Charlie', 'David', 'Eve'],
                'gender': ['female', 'male', 'male', 'male', 'female'],
                'department': ['HR', 'Engineering', 'Marketing', 'Engineering', 'HR']
}
df = pd.DataFrame(data)

df['gender'] = df['gender'].astype('category')
df['department'] = df['department'].astype('category')

print(df['gender'].cat.categories)
print(df['department'].cat.categories)
print(df['gender'].cat.codes)

df['department'] = df['department'].cat.remove_categories(['HR'])
print(df['department'].cat.categories)

print(df)