num_data = dataset.select_dtypes(include='number')

plt.figure(figsize=(10, 5))
corr_matrix = num_data.corr()

sns.heatmap(corr_matrix,
            annot=True,
            linewidth=1.5,
            cmap="coolwarm",
            fmt=".2f")
plt.title("Correlation Heatmap", fontsize=14)
plt.show()
