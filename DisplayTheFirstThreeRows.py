import pandas as pd

def selectFirstRows(employees: pd.DataFrame) -> pd.DataFrame:
    return employees.iloc[[0,1,2]] #Method 1
    return employees.head(3)       #Method 2
    
