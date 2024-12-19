# -*- coding: utf-8 -*-
import pandas as pd
from scipy import stats
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

sns.set()

# Read in the main file
data = pd.read_csv("coffee.csv")

# Get the variables needed for analysis
selected = data.iloc[:, [0, 89, 90, 103]]

# Rename column(s)
selected = selected.rename(columns={"In total, much money do you typically spend on coffee in a month?": "In total, how much money do you typically spend on coffee in a month?"})

################# WORK LOCATION: REMOTE/IN-PERSON/HYBRID ANALYSIS ####################

# Make two dataframes for two chi-square tests
W1 = selected[["Do you work from home or in person?", "Approximately how much have you spent on coffee equipment in the past 5 years?"]].dropna()
W2 = selected[["Do you work from home or in person?", "In total, how much money do you typically spend on coffee in a month?"]].dropna()


# WORK LOCATION AND MONEY SPENT ON COFFEE EQUIPMENT IN PAST 5 YRS
# Create contingency table
W1contin = pd.crosstab(W1.iloc[:, 0], W1.iloc[:, 1])

# Chi-Square Test
W1chi = stats.chi2_contingency(W1contin)

print("Question: Do people with different work location configurations have different coffee equipment expenditure?")
print("NULL: Work location and Coffee Equipment expenditure are independent of each other.")
print("The p-value for the test:")
print(W1chi.pvalue)
print("We reject the null hypothesis and conclude that work location changes the amount one spends on coffee equipment.")
print("\n")


# WORK LOCATION AND MONEY SPENT ON COFFEE IN A MONTH
# Create contingency table
W2contin = pd.crosstab(W2.iloc[:, 0], W2.iloc[:, 1])

# Chi-Square Test
W2chi = stats.chi2_contingency(W2contin)

print("Question: Do people with different work location configurations spend different amounts on coffee?")
print("NULL: Work location and Coffee expenditure are independent of each other.")
print("The p-value for the test:")
print(W2chi.pvalue)
print("We reject the null hypothesis and conclude that work location changes the amount one spends on coffee.")


# PLOT WORK LOCATION COUNTS AND SAVE FIGURE
plt.figure(figsize=(20, 10))
sns.countplot(data=W1, 
              y=W1.iloc[:, 0], order=W1.iloc[:, 0].value_counts().index, hue=W1.iloc[:, 0], palette="deep", legend=False, orient = 'h')
plt.title("Do you work from home or in-person?")
plt.savefig("Work from home or in-person or hybrid.png")


# PLOT FIGURE FOR MONEY SPENT ON COFFEE EQUIPMENT IN PAST 5 YRS
plt.figure(figsize=(20, 10))
sns.countplot(data=W1, 
              y=W1.iloc[:, 1], 
              order=["Less than $20", "$20-$50", "$50-$100", "$100-$300", 
                      "$300-$500", '$500-$1000', 'More than $1,000'], 
              hue=W1.iloc[:, 1], palette="muted", legend=False, orient = 'h')
plt.title("Approximately how much have you spent on coffee equipment in the past 5 years?")
plt.savefig("Total spend on coffee equipment in last 5 yrs.png")


# PLOT FIGURE FOR MONEY SPENT ON COFFEE MONTHLY
plt.figure(figsize=(20, 10))
sns.countplot(data=W2, 
              y=W2.iloc[:, 1], 
              order=["<$20", "$20-$40", "$40-$60", "$80-$100", 
                      ">$100"], 
              hue=W2.iloc[:, 1], palette="bright", legend=False, orient = 'h')
plt.title("In total, how much money do you typically spend on coffee in a month?")
plt.savefig("Total spend on coffee per month.png")













