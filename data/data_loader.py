from ucimlrepo import fetch_ucirepo
import pandas as pd

class ProcessedData:
    def __init__(self):
        heart_disease = fetch_ucirepo(id=45)
        df = pd.DataFrame(heart_disease['data']['features'])
        df['ill'] = heart_disease['data']['targets']
        df['ill'] = (df['ill'] > 0).astype(int)
        df['ill'] = df['ill'].astype('category')
        self.df = df

    def get_data(self):
        return self.df
