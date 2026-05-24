import csv
import pandas as pd

# ── 1. Load 2021 electorate ──────────────────────────────────────────────────
electorate_df = pd.read_csv('/mnt/user-data/uploads/tn_2021_electorate.csv')
electorate_df = electorate_df[['ac_number', 'constituency', 'electorate', 'reserved', 'region']]

# ── 2. Parse election_turnout.csv — each line is a quoted CSV string ─────────
total_rows = []
with open('/mnt/user-data/uploads/election_turnout.csv') as f:
    lines = f.readlines()

for line in lines[1:]:          # skip header
    inner = line.strip().strip('"')
    parsed = next(csv.reader([inner]))
    if len(parsed) == 8 and parsed[0].strip() == '' and parsed[1].strip().lower() == 'total':
        # ['', 'Total', '', evm, postal, total_votes, '', ac_number]
        ac_num      = int(parsed[7].strip())
        evm_votes   = int(parsed[3].strip())
        postal_votes = int(parsed[4].strip())
        total_votes = int(parsed[5].strip())
        total_rows.append({
            'ac_number':          ac_num,
            'evm_votes_2026':     evm_votes,
            'postal_votes_2026':  postal_votes,
            'total_votes_2026':   total_votes
        })

totals_df = pd.DataFrame(total_rows)

# ── 3. Merge with electorate data ────────────────────────────────────────────
merged = pd.merge(totals_df, electorate_df, on='ac_number', how='left')

# ── 4. Calculate Turnout 2026% = Votes Cast 2026 ÷ Electorate (2021) × 100 ──
merged['turnout_2026_pct'] = (merged['total_votes_2026'] / merged['electorate'] * 100).round(2)
merged = merged.sort_values('ac_number').reset_index(drop=True)

# ── 5. Print results ─────────────────────────────────────────────────────────
print(f"{'AC#':<6} {'Constituency':<26} {'EVM Votes':>10} {'Postal':>8} {'Total 2026':>11} {'Electorate':>11} {'Turnout 2026%':>14}")
print("-" * 92)
for _, row in merged.iterrows():
    print(
        f"{int(row['ac_number']):<6} "
        f"{row['constituency']:<26} "
        f"{int(row['evm_votes_2026']):>10,} "
        f"{int(row['postal_votes_2026']):>8,} "
        f"{int(row['total_votes_2026']):>11,} "
        f"{int(row['electorate']):>11,} "
        f"{row['turnout_2026_pct']:>13.2f}%"
    )

# ── 6. Summary stats ─────────────────────────────────────────────────────────
print(f"\nTotal constituencies processed: {len(merged)}")
print(f"Total votes cast 2026:          {merged['total_votes_2026'].sum():>12,.0f}")
print(f"Total electorate (2021 base):   {merged['electorate'].sum():>12,.0f}")
state_turnout = merged['total_votes_2026'].sum() / merged['electorate'].sum() * 100
print(f"State-wide Turnout 2026:        {state_turnout:>11.2f}%")
print(f"Average constituency turnout:   {merged['turnout_2026_pct'].mean():>11.2f}%")
print(f"Highest: {merged.loc[merged['turnout_2026_pct'].idxmax(), 'constituency']} "
      f"({merged['turnout_2026_pct'].max():.2f}%)")
print(f"Lowest:  {merged.loc[merged['turnout_2026_pct'].idxmin(), 'constituency']} "
      f"({merged['turnout_2026_pct'].min():.2f}%)")

# ── 7. Save output CSV ────────────────────────────────────────────────────────
out_cols = ['ac_number', 'constituency', 'reserved', 'region',
            'evm_votes_2026', 'postal_votes_2026', 'total_votes_2026',
            'electorate', 'turnout_2026_pct']
merged[out_cols].to_csv('/mnt/user-data/outputs/election_turnout_with_2026pct.csv', index=False)
print("\nSaved → /mnt/user-data/outputs/election_turnout_with_2026pct.csv")
