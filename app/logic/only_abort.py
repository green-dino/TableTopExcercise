import numpy as np

def calculate_conditional_probabilities(lambdas, k):
    # Calculate P(G_{k+1} | C_{k})
    p_g_k1_given_c_k = (1 - lambdas[k])
    
    # Calculate P(B_{k+1} | C_{k})
    p_b_k1_given_c_k = lambdas[k]
    
    # Calculate P(G_{0} | A_{k})
    p_g_0_given_a_k = 1
    
    # Calculate P(B_{k+1} | B_{k})
    p_b_k1_given_b_k = 1
    
    return p_g_k1_given_c_k, p_b_k1_given_c_k, p_g_0_given_a_k, p_b_k1_given_b_k

# Input probabilities
lambdas = [0.2, 0.4, 0.6]  # Example values, you can provide your own list of lambdas
k = 1  # Example value, you can provide your own value of k

# Calculate conditional probabilities
p_g_k1_given_c_k, p_b_k1_given_c_k, p_g_0_given_a_k, p_b_k1_given_b_k = calculate_conditional_probabilities(lambdas, k)

# Display the results
print(f'P(G_{k+1} | C_{k}) = {p_g_k1_given_c_k}')
print(f'P(B_{k+1} | C_{k}) = {p_b_k1_given_c_k}')
print(f'P(G_0 | A_{k}) = {p_g_0_given_a_k}')
print(f'P(B_{k+1} | B_{k}) = {p_b_k1_given_b_k}')
