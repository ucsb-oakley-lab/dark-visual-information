# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Load the dataset
file_path = "BioluminescenceDuration.csv"
df = pd.read_csv(file_path)

# Add a column for log-transformed flash duration
df['Log Flash Duration'] = np.log10(df['Flash duration (ms)'])

# Create a new column grouping taxonomy into 3 categories
df['Taxon Group'] = df['Taxonomy'].apply(
    lambda x: 'Ostracoda' if x == 'Ostracoda' else ('Insecta' if x == 'Insecta' else 'Mechanical')
)

# Plot histogram with 3 color categories and no vertical grid lines
plt.figure(figsize=(12, 6))
sns.set(style="white")

sns.histplot(data=df, x="Log Flash Duration", hue="Taxon Group", multiple="stack", bins=50)

# Customize plot appearance
plt.xlabel("Log (Flash or Pulse Duration in ms)")
plt.ylabel("Species Count")
plt.grid(axis='y', linestyle='--', alpha=0.7)  # Only horizontal grid lines
plt.tight_layout()

# Save as SVG for Illustrator editing
output_file = "Bioluminescence_Duration_Histogram.svg"
plt.savefig(output_file, format='svg')


# Show the plot
plt.show()

