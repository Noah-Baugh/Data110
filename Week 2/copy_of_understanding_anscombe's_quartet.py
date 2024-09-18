# -*- coding: utf-8 -*-
"""Copy of Understanding_Anscombe's_Quartet.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/19RvHlXV2sGyrFzenkOrtlErFwJ6g_0oe

---

## Understanding Anscombe's Quartet

**Anscombe's Quartet** consists of multiple datasets, each comprising (x, y) pairs. These datasets are unique in that they share several statistical properties:

- **Mean**: The average value of the datasets is consistent across both x and y components.
- **Standard Deviation**: Measures of how data points are dispersed in the dataset remain constant.
- **Regression Line**: Linear regressions drawn from these datasets tend to follow the same line.

However, despite these similarities in basic statistical metrics, each dataset in the quartet tells a different story when plotted graphically. They exhibit distinct patterns and relationships between the x and y variables.

### The Significance of Anscombe's Quartet

The primary lesson of **Anscombe's Quartet** is twofold:

1. **Visual Analysis**: It highlights the critical importance of visually inspecting your data. Graphical representations can uncover underlying patterns, trends, and outliers that summary statistics might miss.

2. **Beyond Statistics**: While statistical measures are invaluable, relying solely on them can be deceptive. The quartet demonstrates that datasets with identical statistical properties can indeed have drastically different distributions and relationships.

Anscombe's Quartet is a powerful reminder that in data analysis, the true essence and story of the data often lie beyond mere numbers and summary statistics.

---
"""

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

x = [10, 8, 13, 9, 11, 14, 6, 4, 12, 7, 5]
y1 = [8.04, 6.95, 7.58, 8.81, 8.33, 9.96, 7.24, 4.26, 10.84, 4.82, 5.68]
y2 = [9.14, 8.14, 8.74, 8.77, 9.26, 8.10, 6.13, 3.10, 9.13, 7.26, 4.74]
y3 = [7.46, 6.77, 12.74, 7.11, 7.81, 8.84, 6.08, 5.39, 8.15, 6.42, 5.73]
x4 = [8, 8, 8, 8, 8, 8, 8, 19, 8, 8, 8]
y4 = [6.58, 5.76, 7.71, 8.84, 8.47, 7.04, 5.25, 12.50, 5.56, 7.91, 6.89]

"""## Task1:
 Run the code below and check if all these graph look different.
"""

ys=[y1,y2,y3,y4]
titles=['Plot 1','Plot 2','Plot 3','Plot 4']
colors=['r','g','b','y']
fig, axs =plt.subplots(2,2,figsize=(10,10))

for i, ax in enumerate(axs.flat):
  ax.scatter(x,ys[i],color=colors[i])
  ax.set_title(titles[i])

"""## Task2:
Run the code below and find the statisical information about the dataset y1
"""

# Convert the list y1 into a Pandas Series object. This allows us to use powerful data analysis tools provided by Pandas on the dataset.
y1_series = pd.Series(y1)

# Generate descriptive statistics of the y1 series. This includes count, mean, standard deviation, minimum, 25th percentile (Q1), median (50th percentile), 75th percentile (Q3), and maximum.
# It provides a quick overview of the central tendency, dispersion, and shape of the dataset's distribution.
y1_description = y1_series.describe()

# Print the descriptive statistics to the console. This output can be used to quickly understand the statistical characteristics of the data in y1.
print(y1_description)

"""## Task 3:  
Replicate Analysis for Additional Datasets You've successfully completed the descriptive analysis for the dataset `y1`. Now, apply the same process to analyze the additional datasets: `y2`, `y3`, and `y4`.

For each dataset (`y2`, `y3`, and `y4`). and Print the result using `print` function.
"""

y2_series = pd.Series(y2)
y2_description = y2_series.describe()


y3_series = pd.Series(y3)
y3_description = y3_series.describe()


y4_series = pd.Series(y4)
y4_description = y4_series.describe()
print(y2_description)
print(y3_description)
print(y4_description)

"""---

## Task 4: Reflection and Comparative Analysis

Having computed the descriptive statistics for each of the datasets (`y1`, `y2`, `y3`, and `y4`), it's now time to reflect on your findings and conduct a comparative analysis.

**Objectives:**

- Understand the implications of the statistical summaries.
- Identify any underlying patterns or anomalies across the datasets.
- Relate your observations to the principles highlighted by Anscombe's quartet.

**Instructions:**

1. **Summarize Your Observations:**
    - Begin by summarizing the descriptive statistics for each dataset. Highlight any notable similarities or differences in terms of mean, standard deviation, quartiles, and range.

3. **Analytical Reflection:**
    - Discuss how the datasets compare to each other. Are there any datasets that appear statistically similar but differ significantly when visualized?
    - Reflect on how Anscombe's quartet demonstrates the importance of both statistical analysis and data visualization in understanding data.

4. **Concluding Thoughts:**
    - Conclude by discussing the significance of descriptive statistics and data visualization in data analysis.
    - Mention any insights or lessons learned from this exercise about the potential pitfalls of relying solely on numerical summaries to

---------

### Task 4 Submission

Please provide your comprehensive answer for Task 4 here. Ensure your response is well-structured and utilizes Markdown formatting for clarity and organization.

# Summaries

Mean:
* All four datasets (y1, y2, y3, y4) have nearly identical mean values around 7.5, indicating that their central tendencies are similar.

Standard Deviation:
* The standard deviations of the datasets are also close, suggesting similar levels of dispersion in the data.

Quartiles and Range:
* Despite the similarity in means and standard deviations, there are variations in the quartiles and range. For instance, y2 has a minimum value of 3.1, while y3 and y4 have maximum values over 12. The slight but present differences show variations in data distribution.

---

# Analytical Reflection

These datasets are statistically fairly indistinguishable from each other; however, as Anscombe's quartet now shows, when plotted, the relationships behind these two datasets are wildly different:

* yy2 can represent a curvilinear trend—patterns of non-linearity.
* y3 could be affected by an anomaly, which would misrepresent the shape of the pattern visually; the descriptive statistics do not show that.
* We should expect y4 to have some clustering with one influential point unknown by summary metrics.

This means that even for datasets with the same means, standard deviations, and other summary statistics, their real nature can only be demonstrated by graphical representation. Without visualization, one can easily miss crucial patterns—for instance, outliers, non-linear relationships, and special distributions.

---

# Concluding Thoughts

* Summary statistics mask the important differences of a data set, even when they share similar statistical properties; they may show different structures and behaviors when plotted.
* The most important thing is to visualize data; plotting data gives a fuller picture that helps in identifying the trend, outlier, and relationship which cannot be arrived at with statistics.
"""