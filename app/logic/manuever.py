import numpy as np

# Define the functions f_k, N, and other parameters as needed
N = 5  # Adjust N as needed

def f_k(x_k, u_k, w_k):
    # Define your system dynamics function here
    # This function should take x_k, u_k, and w_k as inputs and return x_k+1
    return x_k + u_k + w_k  # Example dynamics

def calculate_cost(x, u, N):
    # Define your cost function here
    # This function should take x, u, and N as inputs and return the cost J_k
    return np.sum(x) + np.sum(u)  # Example cost function

def calculate_optimal_policy(N, maneuver_policy):
    # Initialize lists to store optimal policies and values for each time step
    optimal_policies = []
    optimal_values = []

    x_k = 0  # Initial state, adjust as needed

    for k in range(N, -1, -1):
        min_cost = float('inf')
        best_u_k = None

        # Apply maneuver policy for the current time step
        if k < len(maneuver_policy):
            u_k = maneuver_policy[k]
        else:
            u_k = 'C'  # Continue by default

        expected_cost = 0

        # Calculate the next state x_k+1 using the system dynamics f_k
        next_x_k = f_k(x_k, u_k, 0)  # Assuming w_k is 0 for simplicity

        # Calculate the cost for this u_k and x_k
        cost = calculate_cost(next_x_k, u_k, k)

        # Add the expected value of the next state
        cost += optimal_values[-1] if optimal_values else 0

        expected_cost += cost

        # Update the minimum cost and best control action
        if expected_cost < min_cost:
            min_cost = expected_cost
            best_u_k = u_k

        # Store the optimal policy and value for this time step
        optimal_policies.insert(0, best_u_k)
        optimal_values.insert(0, min_cost)

        # Update the state for the next time step
        x_k = f_k(x_k, best_u_k, 0)  # Assuming w_k is 0 for simplicity

    return optimal_policies, optimal_values

# Define maneuver policies and their corresponding attack estimations and costs
policies = [
    {'policy': ['C', 'C', 'C', 'C', 'C'], 'attack_estimation': [0, 0, 0, 0, 0], 'cost': 1},
    {'policy': ['C', 'C', 'C', 'A', 'C'], 'attack_estimation': [0, 0, 0, 0, 0], 'cost': 10},
    {'policy': ['C', 'C', 'C', 'C', 'C'], 'attack_estimation': [0, 0, 0, 1, 0], 'cost': 5},
]

for i, policy_info in enumerate(policies):
    maneuver_policy = policy_info['policy']
    optimal_policies, optimal_values = calculate_optimal_policy(N, maneuver_policy)

    # Display the optimal policy for each time step
    print(f'Policy {i + 1}: {maneuver_policy}')
    for k in range(N + 1):
        print(f'Optimal policy at time step {k}: u*_{k} = {optimal_policies[k]}')

    # Display the optimal cost at time step 0
    print(f'Optimal cost at time step 0: J_0 = {optimal_values[0]}')

    print("\n")
