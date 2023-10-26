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

def main():
    # Sample data from Tables I and II (to be replaced with actual data)
    table_I_values = [1, 2, 3, 4, 5]  # Replace with actual values
    table_II_values = [0.1, 0.2, 0.3, 0.4, 0.5]  # Replace with actual values

    # Define system states
    system_states = ["s1", "s2", "s3", "s4", "s5"]

    # Create an instance of the OptimalPolicyAssigner
    optimal_policy_assigner = OptimalPolicyAssigner(system_states, table_I_values, table_II_values)

    # Assign optimal policies based on the provided data
    optimal_policy_assigner.assign_optimal_policies()

    # Print the optimal control policies
    optimal_policy_assigner.print_optimal_policies()

if __name__ == "__main__":
    main()
