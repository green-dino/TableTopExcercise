# Define the cost function for maneuver assignments
def calculate_maneuver_cost(response, state_transition):
    # Define cost values (for illustration, replace with actual cost data)
    cost_abort = 100
    cost_quarantine_bad = 50
    cost_quarantine_good = 20
    
    if response == "abort":
        return cost_abort
    elif response == "quarantine" and state_transition == "bad":
        return cost_quarantine_bad
    elif response == "quarantine" and state_transition == "good":
        return cost_quarantine_good
    else:
        return 0  # Default case, no cost

# Example scenarios to evaluate maneuver costs
response_1 = "abort"
state_transition_1 = "bad"
cost_1 = calculate_maneuver_cost(response_1, state_transition_1)

response_2 = "quarantine"
state_transition_2 = "bad"
cost_2 = calculate_maneuver_cost(response_2, state_transition_2)

response_3 = "quarantine"
state_transition_3 = "good"
cost_3 = calculate_maneuver_cost(response_3, state_transition_3)

# Print the calculated maneuver costs for the scenarios
print(f"Scenario 1 - Response: {response_1}, State Transition: {state_transition_1}, Cost: {cost_1}")
print(f"Scenario 2 - Response: {response_2}, State Transition: {state_transition_2}, Cost: {cost_2}")
print(f"Scenario 3 - Response: {response_3}, State Transition: {state_transition_3}, Cost: {cost_3}")
