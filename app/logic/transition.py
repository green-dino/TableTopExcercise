class TransitionProbabilityCalculator:
    def calculate_transition_probability(self, d, n, k):
        numerator = sum(range(1, d + 1))
        denominator = sum(range(1, n + 1))
    
        # Calculate the transition probability λi,j,k
        transition_probability = numerator / denominator
    
        return transition_probability

def main():
    # Example values (replace with actual values)
    d = 5  # Number of flows associated with host i
    n = 10  # Total number of flows

    # Create an instance of the TransitionProbabilityCalculator
    probability_calculator = TransitionProbabilityCalculator()

    # Control parameter k (specify the desired control)
    k = 1

    # Calculate the transition probability λi,j,k
    transition_probability = probability_calculator.calculate_transition_probability(d, n, k)

    # Print the result
    print(f"Transition Probability λ for control k={k}: {transition_probability}")

if __name__ == "__main__":
    main()
