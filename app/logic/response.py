class ManeuverCostCalculator:
    def __init__(self):
        # Define cost values (for illustration, replace with actual cost data)
        self.cost_abort = 100
        self.cost_quarantine_bad = 50
        self.cost_quarantine_good = 20

    def calculate_maneuver_cost(self, response, state_transition):
        if response == "abort":
            return self.cost_abort
        elif response == "quarantine" and state_transition == "bad":
            return self.cost_quarantine_bad
        elif response == "quarantine" and state_transition == "good":
            return self.cost_quarantine_good
        else:
            return 0  # Default case, no cost

def main():
    maneuver_cost_calculator = ManeuverCostCalculator()

    response_1 = "abort"
    state_transition_1 = "bad"
    cost_1 = maneuver_cost_calculator.calculate_maneuver_cost(response_1, state_transition_1)

    response_2 = "quarantine"
    state_transition_2 = "bad"
    cost_2 = maneuver_cost_calculator.calculate_maneuver_cost(response_2, state_transition_2)

    response_3 = "quarantine"
    state_transition_3 = "good"
    cost_3 = maneuver_cost_calculator.calculate_maneuver_cost(response_3, state_transition_3)

    # Print the calculated maneuver costs for the scenarios
    print(f"Scenario 1 - Response: {response_1}, State Transition: {state_transition_1}, Cost: {cost_1}")
    print(f"Scenario 2 - Response: {response_2}, State Transition: {state_transition_2}, Cost: {cost_2}")
    print(f"Scenario 3 - Response: {response_3}, State Transition: {state_transition_3}, Cost: {cost_3}")

if __name__ == "__main__":
    main()
