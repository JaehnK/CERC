import os
import requests

import pandas as pd
import numpy as np

class GoogleCSEsearch:
    def __init__(self, query, API, ENGINE_ID):
        self.query = query
        self.API = API
        self.ENGINE_ID = ENGINE_ID
    
    def get_response(self, query, idx):
        url = f"https://www.googleapis.com/customsearch/v1?key={API}&cx={ENGINE_ID}&q={QUERY}"
        response = requests.get(url).json()
        return response
    
    def run(self):
        idx = 1
        while True:
            resp = get_response(API, ENGINE_ID, query, idx)
            if ('items' in resp.keys()):
                for idx_ in range(len(resp['items'])):
                    item = resp['items'][idx_]
                    titles.append(item['title'])
                    snippets.append(item['snippet'])
                    furls.append(item['formattedUrl'])
                idx += 1
                print(idx)
            else:
                break 
        
        df = pd.DataFrame(data = {'title' : titles,
                    'snippet' : snippets,
                    'FormattedUrl' : furls})
        return df;
    
    def to_csv(self, folder_path = './', file_name = query):
        df.to_csv(os.path.join(folder_path, file_name), encoding = 'utf-8-sig')
