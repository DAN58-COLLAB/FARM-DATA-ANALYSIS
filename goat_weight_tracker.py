import pandas as pd

data = {
    "goat": ["Simba", "Kijana", "Mzee", "Damu", "Furaha", "Pendo", "Jasiri"],
    "breed": ["Boer", "Galla", "Boer", "Galla", "Boer", "Galla", "Boer"],
    "weight_kg": [28, 19, 35, 14, 32, 22, 17],
    "age_months": [18, 12, 36, 8, 24, 15, 10],
}

df = pd.DataFrame(data)

# Simple illustrative thresholds for this exercise only.
TARGET_WEIGHT = {"Boer": 25, "Galla": 18}


def weight_status(row):
    target = TARGET_WEIGHT.get(row["breed"])
    if target is None:
        return "Review breed threshold"
    return "OK" if row["weight_kg"] >= target else "Below sample threshold"


df["status"] = df.apply(weight_status, axis=1)
df["weight_gap_kg"] = df.apply(
    lambda row: max(0, TARGET_WEIGHT.get(row["breed"], row["weight_kg"]) - row["weight_kg"]),
    axis=1,
)
priority = df[df["status"] == "Below sample threshold"].sort_values(
    "weight_gap_kg", ascending=False
)
print("GOAT WEIGHT RECORDS")
print(df.to_string(index=False))
print("\nANIMALS BELOW THE EXERCISE THRESHOLD")
if priority.empty:
    print("None")
else:
    print(priority[["goat", "breed", "weight_kg", "weight_gap_kg"]].to_string(index=False))
