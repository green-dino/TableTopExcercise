import numpy as np

# Define the functions g_k, w_k, and the number of time steps N
N = 5  # Adjust N as needed

def g_k(x_k, u_k, w_k):
    # Define your g_k function here
    # This function should take x_k, u_k, and w_k as inputs and return a value
    return x_k + u_k + w_k  # Example function

def w_k(x_k, u_k):
    # Define your probability distribution for w_k
    # This function should take x_k and u_k as inputs and return a probability distribution
    return np.array([0.2, 0.3, 0.5])  # Example distribution

def calculate_optimal_policy(N):
    # Initialize a dictionary to store optimal policies and values for each state x_k
    optimal_policies = {}
    optimal_values = {}

    for k in range(N, -1, -1):
        for x_k in range(0, 10):  # Adjust the range for x_k as needed
            min_cost = float('inf')
            best_u_k = None

            # Iterate over possible control actions u_k
            for u_k in range(0, 5):  # Adjust the range for u_k as needed
                expected_cost = 0

                # Calculate the expected cost for this u_k using the probability distribution w_k
                for w_k_value, w_k_prob in enumerate(w_k(x_k, u_k)):
                    next_x_k = x_k  # Calculate the next state based on your system dynamics

                    # Calculate the cost for this u_k and w_k
                    cost = g_k(x_k, u_k, w_k_value)

                    # Add the expected value of the next state
                    cost += optimal_values.get((k + 1, next_x_k), 0)

                    expected_cost += w_k_prob * cost

                # Update the minimum cost and best control action
                if expected_cost < min_cost:
                    min_cost = expected_cost
                    best_u_k = u_k

            # Store the optimal policy and value for this state x_k
            optimal_policies[(k, x_k)] = best_u_k
            optimal_values[(k, x_k)] = min_cost

    return optimal_policies, optimal_values

# Calculate optimal policies and values
optimal_policies, optimal_values = calculate_optimal_policy(N)

# Display the optimal policy for each state
for k in range(N + 1):
    for x_k in range(10):
        print(f'Optimal policy at time step {k}, state {x_k}: u*_{k} = {optimal_policies[(k, x_k)]}')
