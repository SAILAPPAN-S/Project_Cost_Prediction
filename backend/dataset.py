import numpy as np
import pandas as pd

np.random.seed(42)

# -----------------------------
# CONFIGURATION
# -----------------------------
n_projects = 5000
base_salary_per_dev_per_month = 50000   # Reduced for realistic scale
    
project_types = [
    'Web Application',
    'Mobile Application',
    'AI/ML Solution',
    'ERP System',
    'CRM System',
    'DevOps Automation',
    'Cloud Migration',
    'Cybersecurity Implementation',
    'Data Engineering Pipeline',
    'Business Intelligence Dashboard',
    'IoT System',
    'Blockchain Solution',
    'E-commerce Platform',
    'SaaS Product',
    'Legacy System Modernization'
]

client_industries = ['Finance', 'Healthcare', 'Retail', 'Education', 'Startup']

# Softer multipliers
complexity_multiplier_map = {
    1: 1.0,
    2: 1.1,
    3: 1.2,
    4: 1.3,
    5: 1.4
}

industry_multiplier_map = {
    'Finance': 1.2,
    'Healthcare': 1.15,
    'Retail': 1.05,
    'Education': 1.0,
    'Startup': 0.95
}

project_type_multiplier_map = {
    'Web Application': 1.05,
    'Mobile Application': 1.10,
    'AI/ML Solution': 1.25,
    'ERP System': 1.20,
    'CRM System': 1.15,
    'DevOps Automation': 1.10,
    'Cloud Migration': 1.15,
    'Cybersecurity Implementation': 1.20,
    'Data Engineering Pipeline': 1.15,
    'Business Intelligence Dashboard': 1.05,
    'IoT System': 1.20,
    'Blockchain Solution': 1.30,
    'E-commerce Platform': 1.10,
    'SaaS Product': 1.15,
    'Legacy System Modernization': 1.10
}

# -----------------------------
# GENERATE FEATURES
# -----------------------------
data = pd.DataFrame()

data['project_type'] = np.random.choice(project_types, n_projects)
data['client_industry'] = np.random.choice(client_industries, n_projects)

data['estimated_timeline_months'] = np.random.randint(1, 19, n_projects)
data['team_allocation'] = np.random.randint(2, 16, n_projects)
data['complexity_score'] = np.random.randint(1, 6, n_projects)
data['revision_count'] = np.random.randint(0, 11, n_projects)

# -----------------------------
# COST CALCULATION
# -----------------------------

# Base cost
data['base_cost'] = (
    data['estimated_timeline_months']
    * data['team_allocation']
    * base_salary_per_dev_per_month
)

# Apply multipliers
data['complexity_multiplier'] = data['complexity_score'].map(complexity_multiplier_map)
data['industry_multiplier'] = data['client_industry'].map(industry_multiplier_map)
data['project_type_multiplier'] = data['project_type'].map(project_type_multiplier_map)

# Revision impact (1% per revision)
data['revision_multiplier'] = 1 + (0.01 * data['revision_count'])

# Small noise (±5%)
noise = np.random.normal(1, 0.05, n_projects)

# Final billed amount
data['final_billed_amount'] = (
    data['base_cost']
    * data['complexity_multiplier']
    * data['industry_multiplier']
    * data['project_type_multiplier']
    * data['revision_multiplier']
    * noise
)

# -----------------------------
# ADD UNDERPRICED PROJECTS (15%)
# -----------------------------
underpriced_indices = np.random.choice(
    data.index,
    size=int(0.15 * n_projects),
    replace=False
)

data.loc[underpriced_indices, 'final_billed_amount'] *= 0.85   # Softer reduction

# -----------------------------
# ADD EXTREME OUTLIERS (5%)
# -----------------------------
outlier_indices = np.random.choice(
    data.index,
    size=int(0.05 * n_projects),
    replace=False
)

data.loc[outlier_indices, 'final_billed_amount'] *= np.random.uniform(1.4, 1.8)

# -----------------------------
# CLEANUP
# -----------------------------
data['final_billed_amount'] = data['final_billed_amount'].round(2)

data = data.drop(columns=[
    'base_cost',
    'complexity_multiplier',
    'industry_multiplier',
    'project_type_multiplier',
    'revision_multiplier'
])

data.to_csv("synthetic_project_cost_dataset_realistic.csv", index=False)

print("Realistic Dataset Generated Successfully!")
print(data.head())