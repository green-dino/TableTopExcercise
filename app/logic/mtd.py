# Define sets of services, weaknesses, knowledge blocks, and MTD techniques
S = {"Service1", "Service2", "Service3"}
W = {"Weakness1", "Weakness2", "Weakness3"}
K = {"KnowledgeBlock1", "KnowledgeBlock2", "KnowledgeBlock3"}
M = {"MTDTechnique1", "MTDTechnique2", "MTDTechnique3"}

# Define relationships between services and common weaknesses
RSW = {("Service1", "Weakness1"), ("Service2", "Weakness2"), ("Service3", "Weakness3")}

# Define relationships between weaknesses and knowledge blocks
RWK = {("Weakness1", "KnowledgeBlock1"), ("Weakness2", "KnowledgeBlock2"), ("Weakness3", "KnowledgeBlock3")}

# Define relationships between knowledge blocks and MTD techniques
RKM = {("KnowledgeBlock1", "MTDTechnique1"), ("KnowledgeBlock2", "MTDTechnique2"), ("KnowledgeBlock3", "MTDTechnique3")}

# Print the 7-tuple
print("7-tuple (S, RSW, W, RWK, K, RKM, M):")
print("S (Services):", S)
print("RSW (Relationships between Services and Weaknesses):", RSW)
print("W (Weaknesses):", W)
print("RWK (Relationships between Weaknesses and Knowledge Blocks):", RWK)
print("K (Knowledge Blocks):", K)
print("RKM (Relationships between Knowledge Blocks and MTD Techniques):", RKM)
print("M (MTD Techniques):", M)
