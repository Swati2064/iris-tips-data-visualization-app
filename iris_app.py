import streamlit as st
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

st.title('Miss Swati Jadhav seaborn bootcamp iris data visualization app')
st.write("This is a simple app to visualize the iris dataset using seaborn.")

# Title
st.title("Iris Dataset Visualization")

# Load dataset
iris = sns.load_dataset("iris")

# Create plot
fig, ax = plt.subplots()
sns.countplot(x='species', data=iris, ax=ax)

# Display plot in Streamlit
st.pyplot(fig)

iris = sns.load_dataset("iris")

# Create jointplot
g = sns.jointplot(x='sepal_length', y='sepal_width', data=iris)

# Display in Streamlit
st.pyplot(g.fig)

# Title
st.title("Iris Joint Plot with Regression")

# Load dataset
iris = sns.load_dataset("iris")

# Create jointplot
g = sns.jointplot(x="sepal_length", y="sepal_width", data=iris, kind="reg")

# Display in Streamlit
st.pyplot(g.fig)

# Title
st.title("Iris Joint Plot (Hex)")

# Load dataset
iris = sns.load_dataset("iris")

# Create jointplot
g = sns.jointplot(
    x="sepal_length",
    y="sepal_width",
    kind="hex",
    data=iris
)

# Display in Streamlit
st.pyplot(g.fig)

# Title
st.title("Iris FacetGrid Scatter Plot")

# Load dataset
iris = sns.load_dataset("iris")

# Create FacetGrid
g = sns.FacetGrid(iris, hue='species', height=5)
g.map(plt.scatter, 'sepal_length', 'sepal_width')
g.add_legend()

# Display in Streamlit
st.pyplot(g.fig)

# Title
st.title("Iris Boxplot Visualization")

# Load dataset
iris = sns.load_dataset("iris")

# Create figure
fig = plt.figure(figsize=(10, 7))

# Create boxplot
sns.boxplot(
    x='species',
    y='petal_length',
    data=iris,
    order=['virginica', 'versicolor', 'setosa'],
    linewidth=2.5,
    dodge=False
)

# Display in Streamlit
st.pyplot(fig)

# Title
st.title("Iris Boxplot by Species")

# Load dataset
iris = sns.load_dataset("iris")

# Create figure
fig, ax = plt.subplots(figsize=(12, 6))

# Create boxplot
iris.boxplot(by="species", ax=ax)

# Remove automatic pandas title
plt.suptitle("")  

# Optional labels
ax.set_title("Boxplot of Iris Features by Species")
ax.set_xlabel("Species")
ax.set_ylabel("Values")

# Display in Streamlit
st.pyplot(fig)

# Create figure
fig, ax = plt.subplots(figsize=(10, 7))

# Create strip plot
sns.stripplot(
    x='species',
    y='sepal_length',
    data=iris,
    jitter=True,
    edgecolor='gray',
    size=8,
    palette='winter',
    ax=ax
)

# Labels
ax.set_title("Sepal Length Distribution by Species")
ax.set_xlabel("Species")
ax.set_ylabel("Sepal Length")

# Display in Streamlit
st.pyplot(fig)

# Title
st.title("Iris Boxplot + Stripplot")

# Load dataset
iris = sns.load_dataset("iris")

# Create figure
fig, ax = plt.subplots(figsize=(10, 7))

# Boxplot
sns.boxplot(
    x='species',
    y='sepal_length',
    data=iris,
    ax=ax
)

# Stripplot (overlay)
sns.stripplot(
    x='species',
    y='sepal_length',
    data=iris,
    jitter=True,
    edgecolor='gray',
    color='black',   # better visibility
    ax=ax
)

# Labels
ax.set_title("Sepal Length Distribution with Individual Points")
ax.set_xlabel("Species")
ax.set_ylabel("Sepal Length")

# Display in Streamlit
st.pyplot(fig)

# Title
st.title("Iris Violin Plot")

# Load dataset
iris = sns.load_dataset("iris")

# Create figure
fig, ax = plt.subplots(figsize=(10, 7))

# Create violin plot
sns.violinplot(
    x='species',
    y='sepal_length',
    data=iris,
    ax=ax
)

# Labels
ax.set_title("Sepal Length Distribution by Species")
ax.set_xlabel("Species")
ax.set_ylabel("Sepal Length")

# Display in Streamlit
st.pyplot(fig)

# Title
st.title("Iris Multi Violin Plots")

# Load dataset
iris = sns.load_dataset("iris")

# Create figure
fig, axes = plt.subplots(2, 2, figsize=(15, 10))

# Plot each violin plot
sns.violinplot(x='species', y='petal_length', data=iris, ax=axes[0, 0])
axes[0, 0].set_title("Petal Length")

sns.violinplot(x='species', y='petal_width', data=iris, ax=axes[0, 1])
axes[0, 1].set_title("Petal Width")

sns.violinplot(x='species', y='sepal_length', data=iris, ax=axes[1, 0])
axes[1, 0].set_title("Sepal Length")

sns.violinplot(x='species', y='sepal_width', data=iris, ax=axes[1, 1])
axes[1, 1].set_title("Sepal Width")

# Adjust layout
plt.tight_layout()

# Display in Streamlit
st.pyplot(fig)

# Title
st.title("Iris Pairplot")

# Load dataset
iris = sns.load_dataset("iris")

# Create pairplot
g = sns.pairplot(data=iris, kind='scatter')

# Display in Streamlit
st.pyplot(g.fig)

# Title
st.title("Iris Pairplot with Species")

# Load dataset
iris = sns.load_dataset("iris")

# Create pairplot
g = sns.pairplot(iris, hue='species')

# Display in Streamlit
st.pyplot(g.fig)

# Title
st.title("Iris Correlation Heatmap")

# Load dataset
iris = sns.load_dataset("iris")

# Create figure
fig, ax = plt.subplots(figsize=(10, 7))

# Heatmap
sns.heatmap(
    iris.corr(numeric_only=True),
    annot=True,
    cmap='cubehelix',
    linewidths=1,
    linecolor='k',
    square=True,
    vmin=-1,
    vmax=1,
    cbar_kws={"orientation": "vertical"},
    ax=ax
)

# Display in Streamlit
st.pyplot(fig)

# Title
st.title("Iris Histogram Plots")

# Load dataset
iris = sns.load_dataset("iris")

# Create figure
fig, ax = plt.subplots(figsize=(12, 6))

# Histogram (pandas built-in)
iris.hist(edgecolor='black', linewidth=1.2, ax=ax)

# Display in Streamlit
st.pyplot(fig)

# Title
st.title("Iris Swarm Plot")

# Style
sns.set(style="darkgrid")

# Load dataset
iris = sns.load_dataset("iris")

# Create figure
fig, ax = plt.subplots(figsize=(10, 7))

# Swarm plot
sns.swarmplot(
    x="species",
    y="petal_length",
    data=iris,
    ax=ax
)

# Labels
ax.set_title("Petal Length Distribution by Species")
ax.set_xlabel("Species")
ax.set_ylabel("Petal Length")

# Display in Streamlit
st.pyplot(fig)

# Title
st.title("Iris Violin + Swarm Plot")

# Style
sns.set(style="whitegrid")

# Load dataset
iris = sns.load_dataset("iris")

# Create figure
fig, ax = plt.subplots(figsize=(10, 7))

# Violin plot
sns.violinplot(
    x="species",
    y="petal_length",
    data=iris,
    inner=None,
    ax=ax
)

# Swarm plot (overlay)
sns.swarmplot(
    x="species",
    y="petal_length",
    data=iris,
    color="white",
    edgecolor="black",
    ax=ax
)

# Labels
ax.set_title("Petal Length Distribution with Data Points")
ax.set_xlabel("Species")
ax.set_ylabel("Petal Length")

# Display in Streamlit
st.pyplot(fig)

# Title
st.title("Iris Linear Regression Plot")

# Load dataset
iris = sns.load_dataset("iris")

# Create lmplot
g = sns.lmplot(
    x="petal_length",
    y="petal_width",
    data=iris
)

# Display in Streamlit
st.pyplot(g.fig)

# Title
st.title("Iris KDE Plot by Species")

# Load dataset
iris = sns.load_dataset("iris")

# Create FacetGrid with KDE
g = sns.FacetGrid(iris, hue="species", height=6)
g.map(sns.kdeplot, "petal_length")
g.add_legend()

# Display in Streamlit
st.pyplot(g.fig)

# Title
st.title("Iris Bar Plot (Catplot)")

# Load dataset
iris = sns.load_dataset("iris")

# Create catplot
g = sns.catplot(
    x="species",
    y="sepal_length",
    data=iris,
    kind="bar",
    height=6
)

# Display in Streamlit
st.pyplot(g.fig)

# Title
st.title("Iris Boxen Plot")

# Load dataset
iris = sns.load_dataset("iris")

# Create figure
fig, ax = plt.subplots(figsize=(10, 7))

# Boxen plot
sns.boxenplot(
    x="species",
    y="sepal_length",
    data=iris,
    ax=ax
)

# Labels
ax.set_title("Sepal Length Distribution by Species")
ax.set_xlabel("Species")
ax.set_ylabel("Sepal Length")

# Display in Streamlit
st.pyplot(fig)

# Title
st.title("Iris Setosa KDE Plot")

# Load dataset
iris = sns.load_dataset("iris")

# Filter data
sub = iris[iris["species"] == "setosa"]

# Create figure
fig, ax = plt.subplots(figsize=(10, 7))

# KDE plot
sns.kdeplot(
    x="sepal_length",
    y="sepal_width",
    data=sub,
    fill=True,
    cmap="plasma",
    ax=ax
)

# Labels
ax.set_title("Iris - Setosa")
ax.set_xlabel("Sepal Length")
ax.set_ylabel("Sepal Width")

# Display in Streamlit
st.pyplot(fig)

feature = st.selectbox(
    "Select feature",
    ["petal_length", "petal_width", "sepal_length", "sepal_width"]
)

fig, axes = plt.subplots(2, 2, figsize=(15, 15))

sns.boxplot(x="species", y=feature, data=iris, ax=axes[0, 0])
sns.violinplot(x="species", y=feature, data=iris, ax=axes[0, 1])
sns.stripplot(x="species", y=feature, data=iris, ax=axes[1, 0])
axes[1, 1].hist(iris[feature], bins=30)

plt.tight_layout()
st.pyplot(fig)

# Title
st.title("Iris Dataset - Category Conversion")

# Load dataset
iris = sns.load_dataset("iris")

# Before conversion
st.write("Before conversion:", iris['species'].dtype)

# Convert to category
iris['species'] = iris['species'].astype('category')

# After conversion
st.write("After conversion:", iris['species'].dtype)

# Show categories
st.write("Categories:", iris['species'].cat.categories)

# Title
st.title("Stacked Histogram of Sepal Length by Species")

# Load dataset
iris = sns.load_dataset("iris")

# Clean column names
iris.columns = iris.columns.str.strip()

# Convert to category
iris['species'] = iris['species'].astype('category')

list1 = []
mylabels = []

# Prepare data
for gen in iris['species'].cat.categories:
    list1.append(iris.loc[iris['species'] == gen, 'sepal_length'].values)
    mylabels.append(gen)

# Create figure
fig, ax = plt.subplots(figsize=(10, 7))

# Plot histogram
ax.hist(list1, bins=30, stacked=True, label=mylabels)

# Legend & labels
ax.legend()
ax.set_title("Stacked Histogram of Sepal Length")
ax.set_xlabel("Sepal Length")
ax.set_ylabel("Frequency")

# Display in Streamlit
st.pyplot(fig)

# Title
st.title("Data Type Conversion in Iris Dataset")

# Load dataset
iris = sns.load_dataset("iris")

# Show before conversion
st.subheader("Before Conversion")
st.write(iris.dtypes)

# Columns to convert
cols = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width']

# Convert to numeric
for col in cols:
    iris[col] = pd.to_numeric(iris[col], errors='coerce')

# Show after conversion
st.subheader("After Conversion")
st.write(iris.dtypes)

# Show data
st.subheader("Preview Data")
st.dataframe(iris.head())

# Title
st.title("Iris Area Plot")

# Load dataset
iris = sns.load_dataset("iris")

# Create figure
fig, ax = plt.subplots(figsize=(12, 6))

# Area plot
iris.plot.area(
    y=['sepal_length', 'sepal_width', 'petal_length', 'petal_width'],
    alpha=0.4,
    ax=ax
)

# Title
ax.set_title("Area Plot of Iris Features")

# Display in Streamlit
st.pyplot(fig)

# Title
st.title("Distribution Plot - Sepal Length")

# Load dataset
iris = sns.load_dataset("iris")

# Create figure
fig, ax = plt.subplots(figsize=(10, 6))

# Distribution plot (modern replacement)
sns.histplot(
    iris['sepal_length'],
    kde=True,
    bins=20,
    ax=ax
)

# Labels
ax.set_title("Distribution of Sepal Length")
ax.set_xlabel("Sepal Length")
ax.set_ylabel("Frequency")

# Display in Streamlit
st.pyplot(fig)