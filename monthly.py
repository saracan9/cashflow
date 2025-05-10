import matplotlib.pyplot as plt

# 📌 Veriler
items = ["Electricity", "Water", "Natural Gas", "Internet"]
setup_fees = [14000, 14000, 36000, 2400]
monthly_costs = [2500, 1500, 2000, 0]
months = [1, 2, 3, 4, 5]

# 📍 Diagram verileri
x_pos = []
y_text = []
labels = []
arrow_lengths = []

# 🔢 Offset'ler
item_offsets = [0, 0.2, 0.4, 0.6]

# 🎯 Ölçek: En uzun olan (36.000) biraz kısaltılıyor, diğerleri uzun kalıyor
max_value = max(setup_fees + monthly_costs)
normal_scale = 10 / max_value
reduced_scale = 7 / max_value  # 36.000 için daha kısa

# 0. ay: Setup ücretleri
for i, (item, fee) in enumerate(zip(items, setup_fees)):
    if fee == 0:
        continue
    x = 0 + item_offsets[i]
    x_pos.append(x)
    y_text.append(f"{fee:,.0f}")
    labels.append(item)
    scale = reduced_scale if fee == 36000 else normal_scale
    arrow_lengths.append(fee * scale)

# 1–5. aylar: Aylık giderler
for month in months:
    for j, (item, cost) in enumerate(zip(items, monthly_costs)):
        if cost == 0:
            continue
        x = month + item_offsets[j]
        x_pos.append(x)
        y_text.append(f"{cost:,.0f}")
        labels.append(item)
        arrow_lengths.append(cost * normal_scale)

# 💵 Toplam maliyet
total_cost = sum(setup_fees) + sum([c * 5 for c in monthly_costs])

# ✏️ Çizim
plt.figure(figsize=(22, 8))
plt.title("Utility Cash Outflows Over 5 Months (with Setup Costs at Month 0)")

for x, y, label, arrow_len in zip(x_pos, y_text, labels, arrow_lengths):
    plt.annotate("",
                 xy=(x, -arrow_len),
                 xytext=(x, 0),
                 arrowprops=dict(arrowstyle='-|>', lw=2, color='black'))
    plt.text(x, -arrow_len - 0.3, y, ha='center', va='center', fontsize=10)
    plt.text(x, 0.25, label, ha='center', va='bottom', fontsize=9, rotation=45)

# 🔴 X ekseni çizgisi
plt.axhline(y=0, color='red', linewidth=2)

# 🟨 Toplam kutusu
plt.text(6.3, 1, f"Total Utility Cost (5 Months)\n= TL {total_cost:,}",
         bbox=dict(boxstyle="round,pad=0.4", fc="yellow", ec="black", lw=1.5),
         fontsize=10, ha="center")

plt.xticks(range(6))
plt.xlim(-0.5, 6.9)
plt.ylim(-11, 1.5)
plt.xlabel("Month")
plt.yticks([])
plt.tight_layout()
plt.grid(False)
plt.box(False)
plt.show()
