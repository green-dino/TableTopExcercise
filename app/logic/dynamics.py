import numpy as np

class DynamicSystem:
    def __init__(self, N, x_range, g_k, w_k):
        self.N = N
        self.x_range = x_range
        self.g_k = g_k
        self.w_k = w_k

    def calculate_optimal_policy(self):
        optimal_policies = {}
        optimal_values = {}

        for k in range(self.N, -1, -1):
            for x_k in self.x_range:
                min_cost = float('inf')
                best_u_k = None

                for u_k in range(0, 5):  # Adjust the range for u_k as needed
                    expected_cost = 0

                    for w_k_value, w_k_prob in enumerate(self.w_k(x_k, u_k)):
                        next_x_k = x_k  # Calculate the next state based on your system dynamics

                        cost = self.g_k(x_k, u_k, w_k_value)

                        cost += optimal_values.get((k + 1, next_x_k), 0)

                        expected_cost += w_k_prob * cost

                    if expected_cost < min_cost:
                        min_cost = expected_cost
                        best_u_k = u_k

                optimal_policies[(k, x_k)] = best_u_k
                optimal_values[(k, x_k)] = min_cost

        return optimal_policies, optimal_values

def main():
    N = 5
    x_range = range(10)  # Adjust the range for x_k as needed

    # Define your g_k function here
    def g_k(x_k, u_k, w_k_value):
        return x_k + u_k + w_k_value  # Example function

    # Define your probability distribution for w_k
    def w_k(x_k, u_k):
        return np.array([0.2, 0.3, 0.5])  # Example distribution

    dynamic_system = DynamicSystem(N, x_range, g_k, w_k)
    optimal_policies, optimal_values = dynamic_system.calculate_optimal_policy()

    for k in range(dynamic_system.N + 1):
        for x_k in dynamic_system.x_range:
            print(f'Optimal policy at time step {k}, state {x_k}: u*_{k} = {optimal_policies[(k, x_k)]}')

if __name__ == "__main__":
    main()
