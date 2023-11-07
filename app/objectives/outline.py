import pandas as pd

population_data = {
    'Criteria': ['Population'],
    'Terms': ['Threat Modeling'],
    'Synonyms': ['Threat Model - Threat Intelligence - Threat Trees - Threat Analysis - Attack Simulations']
}

pop_df = pd.DataFrame(population_data)
print(pop_df)


intervention_data = {
    'Criteria': ['Intervention'],
    'Terms': ['Risk Management'],
    'Synonyms': ['Security Risk Assessment - Secure Configuration – Requirements - Requirements Engineering - Security Requirements Elicitation - Anti- Requirements - Secure Software Engineering - Secure Software - Security Testing - Security Risk – Measurement - Security and Privacy Controls']
}

intervene_df = pd.DataFrame(intervention_data)
print(intervene_df)


context_data = {
    'Criteria': ['Context'],
    'Terms': ['Cyber Security'],
    'Synonyms': ['Security - Computer Security - Information Security – Vulnerability – Data Security – Cloud-Security – Security Architecture – Cyber-Attacks – Attack – Adversary – Data Protection by Design – Privacy by Design – Privacy Engineering – System Analysis – Design – Software Design – Solution Design – System Model – Software Development – Secure Development Life- Cycle (SDLC)']
}

context_df = pd.DataFrame(context_data)
print(context_df)
