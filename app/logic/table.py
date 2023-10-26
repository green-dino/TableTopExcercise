# Sample data from Tables I and II (to be replaced with actual data)
table_I_values = [1, 2, 3, 4, 5]  # Replace with actual values
table_II_values = [0.1, 0.2, 0.3, 0.4, 0.5]  # Replace with actual values

# Define system states, attack vectors, and maneuver cost assignments
system_states = ["s1", "s2", "s3", "s4", "s5"]
attack_vectors = ["λ1", "λ2", "λ3", "λ4", "λ5"]
maneuver_cost_assignments = [10, 20, 30, 40, 50]

# Initialize a dictionary to store optimal control policies (π) for each state
optimal_policies = {}

# Assign the optimal control policies based on tables I and II
for i, state in enumerate(system_states):
    if table_I_values[i] > table_II_values[i]:
        optimal_policies[state] = "Policy_A"
    else:
        optimal_policies[state] = "Policy_B"

# Print the optimal control policies obtained for each state
print("Optimal Control Policies (π) for Each State:")
for state, policy in optimal_policies.items():
    print(f"{state}: {policy}")

# Define different variable assignments to explore flexibility
attack_vectors = ["λ1", "λ2", "λ3", "λ4", "λ5"]  # Change attack vectors
maneuver_cost_assignments = [5, 15, 25, 35, 45]  # Change maneuver cost assignments

# Reassign optimal policies based on new variable assignments
for i, state in enumerate(system_states):
    if table_I_values[i] > table_II_values[i]:
        optimal_policies[state] = "New_Policy_A"
    else:
        optimal_policies[state] = "New_Policy_B"

# Print the updated optimal control policies for different variable assignments
print("\nUpdated Optimal Control Policies (π) for Each State:")
for state, policy in optimal_policies.items():
    print(f"{state}: {policy}")
