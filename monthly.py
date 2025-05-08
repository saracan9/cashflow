import matplotlib.pyplot as plt

# 🧾 Veriler
months = [1, 2, 3, 4, 5]
utility_items = ["Electricity", "Water", "Natural Gas", "Internet"]
monthly_costs = [2500, 1500, 2000, 0]

# 📊 Ay ve kalem eşleşmelerini hazırla
positions = []
amounts = []
labels = []

for i, month in enumerate(months):
    for j, (item, cost) in enumerate(zip(utility_items, monthly_costs)):
        x = month + j * 0.15  # Aynı ay içinde kalemleri biraz kaydır
        positions.append(x)
        amounts.append(cost)
        labels.append(item)

# 💥 Grafik ayarları
fig, ax = plt.subplots(figsize=(14, 5))
ax.axhline(0, color='black', linewidth=1)

# Okları çiz
max_cost = max(amounts) if max(amounts) > 0 else 1
arrow_len_factor = 2

for x, y, label in zip(positions, amounts, labels):
    scaled_len = -y / max_cost * arrow_len_factor
    ax.annotate('', xy=(x, scaled_len), xytext=(x, 0),
                arrowprops=dict(facecolor='black', width=2.5, headwidth=10, headlength=10))

    ax.text(x, 0.3, label, ha='center', va='bottom', fontsize=9, rotation=45)
    ax.text(x, scaled_len - 0.2, f"TL {y:,.0f}".replace(",", "."), ha='center', va='top', fontsize=9)

# 🧾 Toplam kutusu
total = sum(monthly_costs) * 5 + 14000 + 14000 + 36000 + 2400  # setup fees + 5x monthly
box_text = f"Total Utility Cost (5 Months)\n= TL {total:,.0f}".replace(",", ".")
props = dict(boxstyle='round,pad=0.4', facecolor='#fdfd96', edgecolor='black')
ax.text(0.98, 0.95, box_text, transform=ax.transAxes,
        fontsize=11, verticalalignment='top', horizontalalignment='right',
        bbox=props)

# Eksen ayarları
ax.set_xlim(0.5, 5.8)
ax.set_ylim(-6, 1.2)
ax.set_xticks(months)
ax.set_xlabel("Month", fontsize=11)
ax.set_yticks([])
ax.set_title("Utility Cash Outflows Over 5 Months", fontsize=13)
plt.tight_layout()

plt.show()
