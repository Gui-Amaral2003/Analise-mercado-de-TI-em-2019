import pandas as pd

def fetch_data(url = "https://drive.google.com/file/d/1vDLqv2JQM6SkH7ByLWNNmsTf8MOWf2kh/view?usp=sharing"):
    
    url='https://drive.google.com/uc?id=' + url.split('/')[-2]
    df = pd.read_csv(url)
    df.drop_duplicates(inplace = True)
    
    return df