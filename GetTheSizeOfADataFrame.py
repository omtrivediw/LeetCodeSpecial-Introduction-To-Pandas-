import pandas as pd

def getDataframeSize(players: pd.DataFrame) -> List[int]:
    tup = players.shape
    return [tup[0] , tup[1]]
    
