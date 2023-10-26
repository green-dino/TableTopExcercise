import numpy as np

class ConditionalProbabilityCalculator:
    def __init__(self, lambdas):
        self.lambdas = lambdas

    def calculate_conditional_probabilities(self, k):
        p_g_k1_given_c_k = (1 - self.lambdas[k])
        p_b_k1_given_c_k = self.lambdas[k]
        p_g_0_given_a_k = 1
        p_b_k1_given_b_k = 1

        return p_g_k1_given_c_k, p_b_k1_given_c_k, p_g_0_given_a_k, p_b_k1_given_b_k

def main():
    # Input probabilities
    lambdas = [0.2, 0.4, 0.6]  # Example values, you can provide your own list of lambdas
    k = 1  # Example value, you can provide your own value of k

    # Create an instance of the ConditionalProbabilityCalculator
    calculator = ConditionalProbabilityCalculator(lambdas)

    # Calculate conditional probabilities
    p_g_k1_given_c_k, p_b_k1_given_c_k, p_g_0_given_a_k, p_b_k1_given_b_k = calculator.calculate_conditional_probabilities(k)

    # Display the results
    print(f'P(G_{k+1} | C_{k}) = {p_g_k1_given_c_k}')
    print(f'P(B_{k+1} | C_{k}) = {p_b_k1_given_c_k}')
    print(f'P(G_0 | A_{k}) = {p_g_0_given_a_k}')
    print(f'P(B_{k+1} | B_{k}) = {p_b_k1_given_b_k}')

if __name__ == "__main__":
    main()
