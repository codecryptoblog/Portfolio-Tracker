# tracker.py
import csv
from decimal import Decimal

def read_holdings(path='holdings.csv'):
    rows = []
    with open(path, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for r in reader:
            rows.append(r)
    return rows

def total_eur(rows):
    total = Decimal('0')
    for r in rows:
        v = r.get('Current value (EUR)', '').replace(',', '').strip()
        try:
            total += Decimal(v) if v else Decimal('0')
        except Exception:
            # bad value => skip
            pass
    return total

if __name__ == '__main__':
    rows = read_holdings()
    print(f"Holdings rows: {len(rows)}")
    print("Top rows sample:")
    for r in rows[:10]:
        print(f" - {r.get('Asset type')} | {r.get('Asset name')} | {r.get('Quantity')} | {r.get('Current value (EUR)')}")
    print('---')
    print('TOTAL EUR:', total_eur(rows))
