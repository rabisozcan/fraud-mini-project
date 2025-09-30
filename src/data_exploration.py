import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os




BASE_DIR = os.path.dirname(os.path.abspath(__file__))

df_path = os.path.join(BASE_DIR, '../data/worksheet.xlsx')
df = pd.read_excel(df_path)


output_dir = os.path.join(BASE_DIR, '../outputs')
os.makedirs(output_dir, exist_ok=True)

# -----------------------------
# Yaş dağılımı
# Age sütunundaki tüm müşterilerin yaş dağılımı
sns.histplot(df['age'], bins=20)
plt.title('Age Distribution')
plt.savefig(os.path.join(output_dir, 'age_distribution.png'))
plt.close()


# -----------------------------
# Total claim amount dağılımı
# total_claim_amount sütunundaki taleplerin dağılımı
sns.histplot(df['total_claim_amount'], bins=30)
plt.title('Total Claim Amount Distribution')
plt.savefig(os.path.join(output_dir, 'total_claim_amount_distribution.png'))
plt.close()


# -----------------------------
# Fraud rapor sayıları
# fraud_reported sütununda kaç kişinin dolandırıcılık raporu olduğu 
sns.countplot(x='fraud_reported', data=df)
plt.title('Fraud Reported Counts')
plt.savefig(os.path.join(output_dir, 'fraud_reported_counts.png'))
plt.close()


# -----------------------------
# Incident severity dağılımı
# incident_severity sütununa göre olayların şiddet dağılımı
sns.countplot(x='incident_severity', data=df)
plt.title('Incident Severity Distribution')
plt.savefig(os.path.join(output_dir, 'incident_severity_distribution.png'))
plt.close()


# -----------------------------
# Policies per state
# policy_state sütununa göre hangi eyalette kaç poliçe (sigorta sözleşmesi) var gösterir.
sns.countplot(x='policy_state', data=df)
plt.title('Policies per State')
plt.xticks(rotation=45)
plt.savefig(os.path.join(output_dir, 'policies_per_state.png'))
plt.close()


# -----------------------------
# Cinsiyete göre dolandırıcılık
# Hangi cinsiyetten kaç kişinin fraud raporu var gösterir.
sns.countplot(x='insured_sex', hue='fraud_reported', data=df)
plt.title('Fraud Reported by Gender')
plt.savefig(os.path.join(output_dir, 'fraud_by_gender.png'))
plt.close()



plt.figure(figsize=(10,6))
sns.countplot(x='insured_education_level', hue='fraud_reported', data=df)
plt.title('Fraud by Education Level')
plt.xticks(rotation=90)
plt.tight_layout()
plt.savefig(os.path.join(output_dir, 'fraud_by_education.png'))
plt.close()