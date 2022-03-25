import requests
import pandas as pd
import json
from os import getcwd

class CISA:
    def __init__(self, url) -> None:
        self.url = url
    
    # returns a dataframe
    def _get_data_to_df(self):
        response = requests.get(self.url)

        dict = json.loads(response.text)
        df = pd.json_normalize(dict['vulnerabilities'])
        
        return df
    
    def convert_to_csv(self,name):
        cwd = getcwd()
        return self._get_data_to_df().to_csv(f'{cwd}\\{name}.csv')


def main():
    CISA(url="https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json").convert_to_csv(name='cisa_db')

    
if __name__ == '__main__':
    main()
