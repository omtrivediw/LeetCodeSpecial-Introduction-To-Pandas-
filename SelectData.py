import pandas as pd

def selectData(students: pd.DataFrame) -> pd.DataFrame:
    return students[["name" , "age"]] [students["student_id"] == 101] #Method 1
    return students.loc[students['student_id'] == 101, ['name', 'age']] #Method 2
