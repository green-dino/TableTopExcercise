import pandas as pd

data = {
    "Tactic": [
        "Active Scanning",
        "Scanning IP Blocks",
        "Vulnerability Scanning",
        "Wordlist Scanning",
        "Gather Victim Host Information",
        "Client Configurations",
        "Firmware",
        "Hardware",
        "Software",
        "Gather Victim Identity Information",
        "Credentials",
        "Email Addresses",
        "Employee Names",
        "Gather Victim Network Information",
        "DNS",
        "Domain Properties",
        "IP Addresses",
        "Network Security Appliances",
        "Network Topology",
        "Network Trust Dependencies",
        "Gather Victim Org Information",
        "Business Relationships",
        "Determine Physical Locations",
        "Identify Business Tempo",
        "Identify Roles",
        "Phishing for Information",
        "Spearphishing Attachment",
        "Spearphishing Link",
        "Spearphishing Service",
        "Spearphishing Voice",
        "Search Closed Sources",
        "Purchase Technical Data",
        "Threat Intel Vendors",
        "Search Open Technical Databases",
        "CDNs",
        "Digital Certificates",
        "DNS/Passive DNS",
        "Scan Databases",
        "WHOIS",
        "Search Open Websites/Domains",
        "Code Repositories",
        "Search Engines",
        "Social Media",
        "Search Victim-Owned Websites",
    ]
}

# Define the separators
separators = [
    "Gather Victim Host Information",
    "Gather Victim Identity Information",
    "Gather Victim Network Information",
    "Gather Victim Org Information",
    "Phishing for Information",
    "Search Closed Sources",
    "Search Open Technical Databases",
    "Search Open Websites/Domains",
]

# Split the data into multiple DataFrames based on separators
dfs = []
start_idx = 0

for separator in separators:
    end_idx = data["Tactic"].index(separator)
    df = pd.DataFrame(data["Tactic"][start_idx:end_idx], columns=["Tactic"])
    dfs.append(df)
    start_idx = end_idx

# Add the last segment
dfs.append(pd.DataFrame(data["Tactic"][start_idx:], columns=["Tactic"]))

# Print or access individual DataFrames
for i, df in enumerate(dfs):
    print(f"DataFrame {i + 1}:\n{df}\n")
