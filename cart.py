import pandas as pd

# Load your data from the "cart_data.csv" file
data = pd.read_csv("navie_bayes_cat_training.csv")

# Define a function to calculate the Gini impurity
def calculate_gini(labels):
    total_samples = len(labels)
    if total_samples == 0:
        return 0.0

    unique_labels = labels.unique()
    gini = 1.0

    for label in unique_labels:
        proportion = (labels == label).sum() / total_samples
        gini -= proportion ** 2

    return round(gini, 3)

# Choose the best attribute and split value
attributes = data.iloc[:, :-1]
labels = data.iloc[:, -1]
best_gini = 1.0
best_attribute = None
best_split_value = None

for attribute in attributes.columns:
    unique_values = attributes[attribute].unique()

    for value in unique_values:
        left_split = labels[attributes[attribute] <= value]
        right_split = labels[attributes[attribute] > value]

        gini = (len(left_split) / len(labels)) * calculate_gini(left_split) + (len(right_split) / len(labels)) * calculate_gini(right_split)
        print("len(left_split:",len(left_split),"\tlen(right_split):",len(right_split),"\tgini:",gini)

        if gini < best_gini:
            best_gini = gini
            best_attribute = attribute
            best_split_value = value

print("Best Attribute:", best_attribute)
print("Best Split Value:", best_split_value)
print("Best Gini:", best_gini)
