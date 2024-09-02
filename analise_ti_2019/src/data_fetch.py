import pandas as pd
import matplotlib.pyplot as plt

def fetch_data(url = "https://drive.google.com/file/d/1jq9LFaAVQrQIn6la5F1ioU8gAfkJwUiY/view?usp=sharing"):
    
    url='https://drive.google.com/uc?id=' + url.split('/')[-2]
    df = pd.read_csv(url)
    
    return df