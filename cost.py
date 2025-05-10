import matplotlib.pyplot as plt

# Ay başlıkları
months = list(range(0, 7))
month_labels = [f"Month {m}" for m in months]

# Her ay için harcamalar (6. ayda sadece 1 "Utilities" olacak şekilde!)
monthly_items = {
    0: [("Project Prep", 0)],
    1: [("Rent", 620000), ("Deposit", 1240000), ("Furnishing & Decoration", 368500), ("Utilities", 19280)],
    2: [("Rent", 620000), ("Construction", 1595000), ("Utilities", 19280)],
    3: [("Rent", 620000), ("Ventilation & Electrical Install", 841500), ("Utilities", 19280)],
    4: [("Rent", 620000), ("Bar Setup", 535000), ("Lighting", 70000), ("Utilities", 19280)],
    5: [("Rent", 620000), ("Utilities", 19280)],
    6: [("2-Month Rent", 1240000), ("Misc. Final Items", 20000), ("Staff Salaries", 203100)]  # Utilities sade
}

# Okların x konumları (manuel, hizalı)
month_x_positions = {
    0: [0.5],
    1: [1.075, 1.41, 1.745, 2.08],
    2: [2.575, 2.91, 3.245],
    3: [3.575, 3.91, 4.245],
    4: [4.575, 4.91, 5.245, 5.58],
    5: [5.91, 6.245],
    6: [6.575, 6.91, 7.245]
}

# Yazı kaydırmaları (çakışmaları engeller)
label_offsets = {
    (1, 2): 0.05,    # Furnishing & Decoration sağa
    (3, 0): -0.05,   # Rent (Month 3) sola
    (3, 1): 0.05,    # Ventilation sağa
    (6, 1): 0.07     # Misc. Final Items sağa
}

# Ölçek
scale_factor = 30000

# Grafik oluştur
fig, ax = plt.subplots(figsize=(18, 9))
ax.axhline(0, color='red', linewidth=2)

# Ay çizgileri
for m in months:
    ax.axvline(x=m, color='lightgrey', linestyle='--', linewidth=0.75)

# Okları çiz
for month, items in monthly_items.items():
    for i, (label, cost) in enumerate(items):
        x = month_x_positions[month][i]
        length = cost / scale_factor

        ax.arrow(x, 0, 0, -length, head_width=0.06, head_length=0.4,
                 fc='black', ec='black', linewidth=1)
        ax.text(x, -length - 2.0, f"₺{cost:,}", ha='center', va='top', fontsize=8)

        offset = label_offsets.get((month, i), 0)
        ax.text(x + offset, 2.5, label, ha='center', va='bottom', fontsize=8, rotation=45)

# Eksenler
ax.set_xticks(months)
ax.set_xticklabels(month_labels)
ax.set_xlim(-0.5, 8.1)
ax.set_ylim(-100, 7)

# Stil temizliği
for spine in ['top', 'right', 'left', 'bottom']:
    ax.spines[spine].set_visible(False)
ax.tick_params(left=False, bottom=False)
ax.set_yticks([])

# Başlık
plt.title("Cash Flow Diagram – FINAL CLEAN (No Overlaps, Only One Utilities)", fontsize=14, fontweight='bold', y=1.12)
plt.tight_layout()
plt.show()
