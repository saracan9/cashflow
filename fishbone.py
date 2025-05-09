import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(16, 10))
ax.axis("off")

# Ana çizgi
ax.arrow(0.1, 0.5, 0.75, 0, head_width=0.02, head_length=0.02, fc='blue', ec='blue', linewidth=3)
ax.text(0.88, 0.5, "Project Failure", fontsize=16, fontweight='bold', va='center', color='black')

# === Üst Dallar (eğik sola yukarı, daha geniş aralık) ===
# Sol üst: Management
ax.plot([0.45, 0.35], [0.5, 0.7], color='blue', linewidth=2)
ax.text(0.33, 0.72, "Management", fontsize=12, fontweight='bold', ha='right')
management_issues = ["Poor Communication", "Coordination Failures", "Planning Delays"]
for i, issue in enumerate(management_issues):
    ax.text(0.33, 0.72 - (i + 1) * 0.04, f"** {issue}", fontsize=11, ha='right')

# Sağ üst: Technical
ax.plot([0.65, 0.55], [0.5, 0.7], color='blue', linewidth=2)
ax.text(0.53, 0.72, "Technical", fontsize=12, fontweight='bold', ha='right')
technical_issues = ["System Integration Faults", "Power Infrastructure Delays", "HVAC Installation Issues"]
for i, issue in enumerate(technical_issues):
    ax.text(0.53, 0.72 - (i + 1) * 0.04, f"** {issue}", fontsize=11, ha='right')

# === Alt Dallar (eğik sola aşağı, daha geniş aralık) ===
# Sol alt: Finance
ax.plot([0.45, 0.35], [0.5, 0.3], color='blue', linewidth=2)
ax.text(0.33, 0.28, "Finance", fontsize=12, fontweight='bold', ha='right')
finance_issues = ["Unexpected Material Cost", "Payment Delays", "Exchange Rate Fluctuation"]
for i, issue in enumerate(finance_issues):
    ax.text(0.33, 0.28 - (i + 1) * 0.04, f"** {issue}", fontsize=11, ha='right')

# Sağ alt: Operations
ax.plot([0.65, 0.55], [0.5, 0.3], color='blue', linewidth=2)
ax.text(0.53, 0.28, "Operations", fontsize=12, fontweight='bold', ha='right')
operations_issues = ["Furniture Delivery Delays", "Insufficient Staff", "Cleaning Oversights"]
for i, issue in enumerate(operations_issues):
    ax.text(0.53, 0.28 - (i + 1) * 0.04, f"** {issue}", fontsize=11, ha='right')

plt.title("Fishbone Diagram – Project Failure (IE270)", fontsize=16, fontweight='bold', pad=20)
plt.tight_layout()
plt.show()
