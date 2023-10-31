import random

# Define the game parameters
T = 10  # Time horizon
N1 = 5  # Number of agents in group 1
N2 = 3  # Number of agents in group 2
N = N1 + N2  # Total number of agents

# Define state space, actions, decisions, and observations
state_space = [f'X{i}' for i in range(1, N1 + 1)]
action_space = [f'A{i}' for i in range(1, N1 + 1)]
decision_space = [f'D{i}' for i in range(1, N2 + 1)]
observation_space = [f'Y{i}' for i in range(1, N1 + 1)]

# Define transition probabilities Qn for each agent in group 1
transition_probabilities = {f'Q{i}': [[0.7, 0.3], [0.4, 0.6]] for i in range(1, N1 + 1)}

# Define agent utility functions for group 1
def utility_group1(A, D):
    utility = {}
    Wr = 0.5  # Weight for security
    Wc = 0.5  # Weight for efficiency
    u_lower = -10  # Lower bound for utility
    u_upper = 10  # Upper bound for utility
    epsilon = 0.2  # Maximum utility error

    for n in range(1, N1 + 1):
        An = A[f'A{n}']
        # Simulate observable feedback (effectiveness and cost)
        r = effectiveness(D, An)  # Calculate effectiveness
        c = cost(D)  # Calculate cost

        # Calculate utility with given weights
        u = Wr * r - Wc * c

        # Apply utility bounds and potential utility errors
        u += random.uniform(-epsilon, epsilon)  # Add utility error

        # Ensure the utility is within defined bounds
        u = max(u_lower, min(u_upper, u))

        utility[f'U{n}'] = u

    return utility

# Define effectiveness and cost functions
def effectiveness(D, A):
    # Implement your effectiveness function (e.g., number of failed attack tries)
    return random.uniform(0, 1)

def cost(D):
    # Implement your cost function (e.g., overhead induced by defense actions)
    return random.uniform(0, 1)

# Define action sets for players
action_sets = {f'A{i}': [f'a{i}_{j}' for j in range(1, T + 1)] for i in range(1, N + 1)}

# Define the Cartesian product of action sets
S = {f's{t}': {f'a{i}': action_sets[f'A{i}'][t - 1] for i in range(1, N + 1)} for t in range(1, T + 1)}

# Define utility functions for group 2
def utility_group2(Y, D, A):
    utility = {}
    for m in range(1, N2 + 1):
        Vm = 0  # Define this function
        utility[f'U{m}'] = [Vm(Y, D[f'D{m}']) - sum(D.values()) * A[f'A{i}'] for i in range(1, N1 + 1)]
    return utility

# Define informational constraints
informational_constraints = {}
for i in range(1, N + 1):
    informational_constraints[f'I{i}'] = [f'a{i}_{j}' for j in range(T)]

# Define initial private information, common information
P = {f'P{n}': state_space for n in range(1, N1 + 1)}
C = {f'C{t}': {f'A{i}': action_space, f'D{i}': decision_space, f'Y{i}': observation_space} for t in range(1, T + 1) for i in range(1, N1 + 1)}

# Define agent strategies
strategies = {}
for n in range(1, N + 1):
    strategies[f'g{n}'] = f'g{n}(P, C)'

# Print the game configuration and informational constraints
print(f'Time Horizon (T): {T}')
print(f'Number of Agents in Group 1 (N1): {N1}')
print(f'Number of Agents in Group 2 (N2): {N2}')
print(f'State Space: {state_space}')
print(f'Action Space: {action_space}')
print(f'Decision Space: {decision_space}')
print(f'Observation Space: {observation_space}')
print(f'Transition Probabilities (Qn) for Agents in Group 1: {transition_probabilities}')
print(f'Informational Constraints:')
for i in range(1, N + 1):
    print(f'Player {i} Informational Constraint: {informational_constraints[f"I{i}"]}')
