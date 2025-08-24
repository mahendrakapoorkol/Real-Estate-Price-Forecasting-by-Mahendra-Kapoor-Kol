plt.figure(figsize=(18, 36))
plt.suptitle("Categorical Features: Distribution", fontsize=16)

for i, col in enumerate(object_cols, start=1):
    counts = dataset[col].value_counts()
    plt.subplot(11, 4, i)
    sns.barplot(x=counts.index, y=counts.values, palette="Set2")
    plt.xticks(rotation=90)
    plt.title(col)

plt.tight_layout(rect=[0, 0, 1, 0.97])
plt.show()
