import numpy as np

class DynamicSystem:
    def __init__(self):
        # Initialize system parameters and state
        self.N = 5
        self.x_k = 0

    def f_k(self, x_k, u_k, w_k):
        # Define your system dynamics function here
        return x_k + u_k + w_k  # Example dynamics

    def calculate_cost(self, x, u):
        # Define your cost function here
        return np.sum(x) + np.sum(u)  # Example cost function

    def calculate_optimal_policy(self):
        optimal_policies = []
        optimal_values = []

        for k in range(self.N, -1, -1):
            min_cost = float('inf')
            best_u_k = None

            for u_k in range(0, 5):  # Adjust the range for u_k as needed
                expected_cost = 0

                next_x_k = self.f_k(self.x_k, u_k, 0)  # Assuming w_k is 0 for simplicity

                cost = self.calculate_cost(next_x_k, u_k)

                cost += optimal_values[-1] if optimal_values else 0

                expected_cost += cost

                if expected_cost < min_cost:
                    min_cost = expected_cost
                    best_u_k = u_k

            optimal_policies.insert(0, best_u_k)
            optimal_values.insert(0, min_cost)

            self.x_k = self.f_k(self.x_k, best_u_k, 0)

        return optimal_policies, optimal_values

def main():
    system = DynamicSystem()
    optimal_policies, optimal_values = system.calculate_optimal_policy()

    for k in range(system.N + 1):
        print(f'Optimal policy at time step {k}: u*_{k} = {optimal_policies[k]}')

    print(f'Optimal cost at time step 0: J_0 = {optimal_values[0]}')

if __name__ == "__main__":
    main()
