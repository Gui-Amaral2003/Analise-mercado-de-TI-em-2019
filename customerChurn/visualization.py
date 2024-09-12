import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import data_analysis
import data_fetch
import data_cleaning

df = data_fetch.fetch_data()
df = data_cleaning.remover_duplicatas(df)

age_groups = [i for i in range(0, 6)]
df["Frequency of use category"] = pd.cut(df["Frequency of use"],
                                         bins = [0, 10, 50, float("inf")],
                                         labels = ["low", "Medium", "High"])

counts = df.groupby(["Age Group", "Frequency of use category"]).nunique()["Frequency of use"]

sns.heatmap(counts.unstack(), annot=True, cmap='viridis', fmt='d')

plt.title('Number of Distinct Phone Calls by Age Group and Frequency')
plt.xlabel('Call Duration Category')
plt.ylabel('Age Group')

plt.show()

