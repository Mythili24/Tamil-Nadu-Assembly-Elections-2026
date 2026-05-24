import pandas as pd

# Load the data
df = pd.read_csv('/mnt/user-data/uploads/tn_2021_results.csv')

# For each constituency, sum all votes cast and get the turnout % (same for all rows in a constituency)
constituency_data = df.groupby(['ac_number', 'constituency', 'reserved', 'region']).agg(
    total_votes_cast=('votes', 'sum'),
    turnout_pct=('turnout', 'first')   # turnout is the same for all candidates in a constituency
).reset_index()

# Calculate electorate: votes_cast ÷ (turnout% / 100)
constituency_data['electorate'] = (
    constituency_data['total_votes_cast'] / (constituency_data['turnout_pct'] / 100)
).round(0).astype(int)

# Sort by constituency number
constituency_data = constituency_data.sort_values('ac_number').reset_index(drop=True)

# Display results
print(f"{'AC#':<6} {'Constituency':<25} {'Votes Cast':>12} {'Turnout %':>10} {'Electorate':>12} {'Reserved':<10} {'Region'}")
print("-" * 90)
for _, row in constituency_data.iterrows():
    print(
        f"{row['ac_number']:<6} "
        f"{row['constituency']:<25} "
        f"{row['total_votes_cast']:>12,} "
        f"{row['turnout_pct']:>9.2f}% "
        f"{row['electorate']:>12,} "
        f"{row['reserved']:<10} "
        f"{row['region']}"
    )

print(f"\nTotal constituencies: {len(constituency_data)}")
print(f"Total votes cast (state-wide): {constituency_data['total_votes_cast'].sum():,}")
print(f"Total electorate (state-wide):  {constituency_data['electorate'].sum():,}")
print(f"Average turnout: {constituency_data['turnout_pct'].mean():.2f}%")

# Save to CSV
output_path = '/mnt/user-data/outputs/tn_2021_electorate.csv'
constituency_data.to_csv(output_path, index=False)
print(f"\nResults saved to: {output_path}")
