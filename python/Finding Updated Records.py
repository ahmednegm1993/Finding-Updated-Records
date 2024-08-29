import pandas as pd

# Load the dataset
df = pd.read_excel(r'E:\\Data_analysis_projects\\Finding Updated Records\dataset\\Finding Updated Records.xlsx')

df1 = df.groupby('id', as_index=False).agg({
    'first_name': 'first',   
    'last_name': 'first',    
    'department_id': 'first',
    'salary': 'max'          
})

print(df1)