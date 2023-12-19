import pandas as pd

def dropMissingData(students: pd.DataFrame) -> pd.DataFrame:
    df2 = students[students.name.notnull()]
    return df2
