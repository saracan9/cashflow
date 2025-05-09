import matplotlib.pyplot as plt
import numpy as np

setup_descriptions = [
    "Annual Rent", "Deposit", "Furnishing & Decoration", "Initial Staff Salaries",
    "Construction Cost", "Ventilation & Air Conditioning", "Electrical & Mechanical Installation",
    "Bar Setup", "Lighting", "Utility Costs", "Other"
]

setup_costs = [
    3100000, 1240000, 368500, 203100, 1595000, 475500,
    366000, 535000, 70000, 96400, 20000
]

periods = list(range(1, len(setup_costs) + 1))

discount_rate = 0.10

npv = sum(cf / (1 + discount_rate)**i for i, cf in enumerate(setup_costs))

fig, ax = plt.subplots(figsize=(14, 7))
ax.axhline(0, color='black', linewidth=1)

arrow_len_factor = 5
min_cf = max(setup_costs)


for i, (x, y, desc) in enumerate(zip(periods, setup_costs, setup_descriptions)):
    scaled_len = -y / min_cf * arrow_len_factor
    ax.annotate('', xy=(x, scaled_len), xytext=(x, 0),
                arrowprops=dict(facecolor='black', edgecolor='black',
                                width=2.5, headwidth=12, headlength=12))

   
    ax.text(x, 0.3, desc, ha='center', va='bottom', fontsize=10, rotation=45)

   
    ax.text(x, scaled_len - 0.2, f"TL {y:,.0f}".replace(",", "."),
            ha='center', va='top', fontsize=10)


box_text = f"Net Present Value (NPV)\n= TL {-npv:,.0f}".replace(",", ".")
props = dict(boxstyle='round,pad=0.5', facecolor='#d0f0c0', edgecolor='black')
ax.text(0.98, 0.95, box_text, transform=ax.transAxes,
        fontsize=12, verticalalignment='top', horizontalalignment='right',
        bbox=props)


ax.set_xlim(0.5, len(periods) + 0.5)
ax.set_ylim(-6, 1.5)  
ax.set_xticks(periods)
ax.set_yticks([])
ax.set_xlabel("Period (Month)", fontsize=12)
ax.set_title("Setup Cost Timeline (Based on Breakdown)", fontsize=14)
plt.tight_layout()


plt.show()
