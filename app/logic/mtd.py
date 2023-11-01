# Define sets of services, weaknesses, knowledge blocks, and MTD Moving Target Defense techniques
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

# Attacker Strategies
attacker_strategies = {
    "Uniform-Uncompromised": "Selects uniformly among those servers under the defender's control.",
    "MaxProbe-Uncompromised": "Selects the server that has been probed the most since last reimage (that the attacker knows about), among those servers under the defender's control, breaking ties uniformly.",
    "Control-Threshold": "If the attacker controls less than a threshold fraction of the servers, it chooses to probe the server that has been probed the most since last reimage (as far as it is aware) among those it does not currently control. Ties are broken uniformly among all eligible servers. A minimum waiting period of one time unit separates any two consecutive actions."
}

# Defender Strategies
defender_strategies = {
    "Uniform": "Selects uniformly among all up servers.",
    "MaxProbe": "Selects the server that has been probed most since its last reimage, breaking ties uniformly.",
    "ProbeCount-or-Period": "Reimages a server whenever it detects a threshold number of probes since the last reimage or if it has been probed at least once but not within the specified period.",
    "Control-Threshold": "Reimages a server when the fraction of servers controlled falls below a threshold.",
    "Control-Target": "Similar to Control-Threshold, but based on a target rather than a threshold.",
}

# Equilibria Concepts
equilibrium_concepts = {
    "MaxDef": "Aggressively reimages servers, making it futile for the attacker to compromise servers.",
    "MaxAtt": "Attacker probes aggressively, and defender reimages infrequently or ineffectively.",
    "Share": "Moderate attack and defense levels where both players achieve their objectives.",
    "Fight": "Robust attack and defense activity, resulting in persistent contention with neither player achieving their objectives to a satisfactory degree."
}

# User interaction loop
while True:
    print("\nWelcome! Explore the available data:")
    print("1. Enter 'S' to explore Services")
    print("2. Enter 'W' for Weaknesses")
    print("3. Enter 'K' for Knowledge Blocks")
    print("4. Enter 'M' for MTD Techniques")
    print("5. Enter 'AS' for Attacker Strategies")
    print("6. Enter 'DS' for Defender Strategies")
    print("7. Enter 'EC' for Equilibrium Concepts")
    print("8. Enter 'Q' to quit")

    user_input = input("Enter your choice: ").strip().upper()

    if user_input == 'S':
        print("Services:", S)
    elif user_input == 'W':
        print("Weaknesses:", W)
    elif user_input == 'K':
        print("Knowledge Blocks:", K)
    elif user_input == 'M':
        print("MTD Techniques:", M)
    elif user_input == 'AS':
        print("Attacker Strategies:")
        for strategy, description in attacker_strategies.items():
            print(f"{strategy}: {description}")
    elif user_input == 'DS':
        print("Defender Strategies:")
        for strategy, description in defender_strategies.items():
            print(f"{strategy}: {description}")
    elif user_input == 'EC':
        print("Equilibrium Concepts:")
        for concept, description in equilibrium_concepts.items():
            print(f"{concept}: {description}")
    elif user_input == 'Q':
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid input. Please enter a valid option.")
