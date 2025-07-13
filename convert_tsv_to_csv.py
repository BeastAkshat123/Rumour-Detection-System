import pandas as pd

# Read the TSV file (tab-separated)
df = pd.read_csv("train.tsv", sep='\t', header=None)

# Optional: assign column names if needed
df.columns = [
    "id", "label", "statement", "subject", "speaker", "job", "state", "party",
    "barely_true_counts", "false_counts", "half_true_counts", "mostly_true_counts",
    "pants_on_fire_counts", "venue"
]

# Save as CSV
df.to_csv("train.csv", index=False)
print("✅ train.tsv successfully converted to train.csv")
