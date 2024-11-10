import pandas as pd
def fetch_data(url = 'https://drive.google.com/file/d/1a2zLIjnfJ0cxbqclopiqa5wc3IoBWdVY/view?usp=sharing'):
    
    url='https://drive.google.com/uc?id=' + url.split('/')[-2]
    df = pd.read_parquet(url)
    
    return df