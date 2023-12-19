import pandas as pd

def modifySalaryColumn(employees: pd.DataFrame) -> pd.DataFrame:
    return employees.assign(salary = 2 * employees['salary']) #One way
    employees.salary = 2 * employees.salary #Another Way
    return employees
