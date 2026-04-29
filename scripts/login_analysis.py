import pandas as pd

# Load dataset
df = pd.read_csv("../logs/cybersecurity_intrusion_data.csv")

print("\nDataset Info:")
df.info()

print("\nFirst 5 rows:")
print(df.head())

# -------------------------
# 1. Attack vs Normal
# -------------------------
print("\nAttack vs Normal:")
print(df['attack_detected'].value_counts())

# -------------------------
# 2. Failed login patterns
# -------------------------
print("\nAverage failed logins:")
print(df['failed_logins'].mean())

# -------------------------
# 3. Suspicious sessions
# -------------------------
suspicious = df[df['attack_detected'] == 1]

print("\nSuspicious Sessions Count:")
print(len(suspicious))

# -------------------------
# 4. High-risk IPs
# -------------------------
print("\nLow Reputation IPs (possible risk):")
print(df[df['ip_reputation_score'] < 0.3].head())

# -------------------------
# 5. Unusual time access
# -------------------------
print("\nUnusual time access count:")
print(df['unusual_time_access'].value_counts())

# -------------------------
# Suspicious behavior rule
# -------------------------

suspicious_rule = df[
    (df['failed_logins'] > 2) &
    (df['unusual_time_access'] == 1)
]

print("\nSessions flagged by rule:")
print(len(suspicious_rule))

# Compare with actual attacks
true_attacks = suspicious_rule[suspicious_rule['attack_detected'] == 1]

print("\nCorrectly identified attacks:")
print(len(true_attacks))

# -------------------------
# Expanded detection rule
# -------------------------

rule2 = df[
    (df['failed_logins'] > 1) |
    (df['ip_reputation_score'] < 0.2)
]

print("\nRule 2 flagged sessions:")
print(len(rule2))

correct_rule2 = rule2[rule2['attack_detected'] == 1]

print("\nRule 2 correct attacks:")
print(len(correct_rule2))

import matplotlib.pyplot as plt

# -------------------------
# Chart: Rule Comparison
# -------------------------

rules = ['Rule 1', 'Rule 2']
correct = [24, 290]
flagged = [24, 562]

x = range(len(rules))

plt.bar(x, flagged, label='Flagged Sessions')
plt.bar(x, correct, label='Correct Attacks')

plt.xticks(x, rules)
plt.title("Detection Rule Comparison")
plt.ylabel("Number of Sessions")
plt.legend()

plt.savefig("../notes/rule_comparison.png")
plt.close()