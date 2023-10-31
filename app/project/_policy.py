class OptimalPolicyAssigner:
    def __init__(self, system_states, table_I_values, table_II_values):
        self.system_states = system_states
        self.table_I_values = table_I_values
        self.table_II_values = table_II_values
        self.optimal_policies = {}

    def assign_optimal_policies(self):
        for i, state in enumerate(self.system_states):
            if self.table_I_values[i] > self.table_II_values[i]:
                self.optimal_policies[state] = "Policy_A"
            else:
                self.optimal_policies[state] = "Policy_B"

    def print_optimal_policies(self):
        print("Optimal Control Policies (π) for Each State:")
        for state, policy in self.optimal_policies.items():
            print(f"{state}: {policy}")

def calculate_optimal_policies(system_states, table_I_values, table_II_values):
    optimal_policies = {}
    for i, state in enumerate(system_states):
        if table_I_values[i] > table_II_values[i]:
            optimal_policies[state] = "Policy_A"
        else:
            optimal_policies[state] = "Policy_B"
    return optimal_policies

def print_optimal_policies(optimal_policies):
    print("Optimal Control Policies (π) for Each State:")
    for state, policy in optimal_policies.items():
        print(f"{state}: {policy}")

def main():
    # Sample data from Tables I and II (to be replaced with actual data)
    table_I_values = [1, 2, 3, 4, 5]  # Replace with actual values
    table_II_values = [0.1, 0.2, 0.3, 0.4, 0.5]  # Replace with actual values

    # Define system states
    system_states = ["s1", "s2", "s3", "s4", "s5"]

    # Using the class-based approach
    optimal_policy_assigner = OptimalPolicyAssigner(system_states, table_I_values, table_II_values)
    optimal_policy_assigner.assign_optimal_policies()
    optimal_policy_assigner.print_optimal_policies()

    # Using the function-based approach
    optimal_policies = calculate_optimal_policies(system_states, table_I_values, table_II_values)
    print_optimal_policies(optimal_policies)

if __name__ == "__main__":
    main()
