import pandas as pd

def findHeavyAnimals(animals: pd.DataFrame) -> pd.DataFrame:
#Sol 1
    df = animals.where(animals['weight'] > 100)
    df2 = df[df.name.notnull()]
    df3 = df2.sort_values(by = 'weight', ascending = False)
    return df3[['name']]
#Sol 2
    return animals[animals['weight'] > 100].sort_values('weight', ascending=False)[
        ['name']
  ]
