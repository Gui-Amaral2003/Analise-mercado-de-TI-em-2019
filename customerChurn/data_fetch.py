import pandas as pd
import matplotlib.pyplot as plt

def fetch_data(url = "https://drive.google.com/file/d/11IxO_FjnoHhUb164l22A4zEE_Rl-ZzX6/view?usp=sharing"):
    
    url='https://drive.google.com/uc?id=' + url.split('/')[-2]
    df = pd.read_csv(url)
    
    return df