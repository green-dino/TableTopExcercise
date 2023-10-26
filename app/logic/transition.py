
# We specify example values for d, n, and k, but you should replace them with actual values relevant to your network or domain.
#  Function takes the number of flows associated with host i (d), the total number of flows (n), and the control parameter (k) as inputs.

def calculate_transition_probability(d, n, k):
    numerator = sum(range(1, d + 1))
    denominator = sum(range(1, n + 1))
    
    # Calculate the transition probability λi,j,k
    transition_probability = numerator / denominator
    
    return transition_probability

# Example values (replace with actual values)
d = 5  # Number of flows associated with host i
n = 10  # Total number of flows

# Control parameter k (specify the desired control)
k = 1

# Calculate the transition probability λi,j,k
transition_probability = calculate_transition_probability(d, n, k)

# Print the result
print(f"Transition Probability λ for control k={k}: {transition_probability}")
