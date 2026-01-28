import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("quotes_data.csv", skiprows= 1 , names= ["Author","Quote"])
author_counts = df["Author"].value_counts().head(10)
print("The most repeated authors: \n")
print(author_counts)

author_counts.plot(kind="bar", color = "skyblue")
plt.title("Top 10 authors by quote count")
plt.xlabel('Author')
plt.ylabel('Number of Quotes')
plt.xticks(rotation=45)
plt.tight_layout()


plt.savefig('authors_chart.png')
plt.show()