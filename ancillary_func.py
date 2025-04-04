# Functions designed to support the projects functionalities

# Define a function for enhancing the look of output tables
def get_table(df):
    styled = df.style.set_table_styles([
    {'selector': 'table', 'props': [('border-collapse', 'collapse')]},
    {'selector': 'th, td', 'props': [('border', '1px solid black'), 
                                    ('padding', '8px')]},
    {'selector': 'th', 'props': [('background-color', '#f2f2f2'),
                                ('font-weight', 'bold')]}
])
    return styled


# Define a function for displaying DataFrame Info
import pandas as pd

def df_info_table(df):
    # Create a summary DataFrame
    summary = pd.DataFrame({
        'Column': df.columns,
        'Non-Null Count': df.notnull().sum(),
        'Dtype': df.dtypes,
        'Null Count': df.isnull().sum(),
        'Unique Values': df.nunique()
    }).reset_index(drop=True)
    
    return summary

