import numpy as np

class SystemModel:
    def __init__(self, N, system_states, detection_outputs, num_flows_per_host, attack_probabilities):
        """
        Initialize the SystemModel with parameters and data.

        Args:
            N (int): The number of time periods.
            system_states (list): List of system states for each time period.
            detection_outputs (list): List of detection outputs for each time period.
            num_flows_per_host (list): List of the number of flows associated with each host for each time period.
            attack_probabilities (list): List of attack probabilities for each time period.
        """
        self.N = N
        self.system_states = system_states
        self.detection_outputs = detection_outputs
        self.num_flows_per_host = num_flows_per_host
        self.attack_probabilities = attack_probabilities

    def f_k(self, x_k, u_k, w_k):
        """
        Define the system dynamics function.

        Args:
            x_k (str): Current system state.
            u_k (str): Control action.
            w_k (float): System noise.

        Returns:
            str: Next system state.
        """
        # Replace with actual system dynamics
        if x_k == 'normal':
            if u_k == 'quarantine' and w_k < 0.5:
                return 'quarantined'
            else:
                return 'normal'
        elif x_k == 'quarantined':
            if u_k == 'abort' or (u_k == 'quarantine' and w_k >= 0.5):
                return 'normal'
            else:
                return 'quarantined'

    def calculate_cost(self, x, u, k):
        """
        Define the cost function.

        Args:
            x (str): Current system state.
            u (str): Control action.
            k (int): Time period.

        Returns:
            float: Cost value.
        """
        # Replace with actual cost calculation
        cost = 0.0  # Initialize cost

        if x == 'normal':
            cost += self.detection_outputs[k] * self.num_flows_per_host[k]
        elif x == 'quarantined':
            if u == 'abort':
                cost += 100
            elif u == 'quarantine':
                if self.attack_probabilities[k] > 0.3:
                    cost += 50
                else:
                    cost += 20

        return cost

class ManeuverCostCalculator:
    def __init__(self):
        """
        Initialize the ManeuverCostCalculator with cost values.
        """
        self.cost_abort = 100
        self.cost_quarantine_bad = 50
        self.cost_quarantine_good = 20

    def calculate_maneuver_cost(self, response, state_transition):
        """
        Calculate the cost associated with a maneuver.

        Args:
            response (str): Maneuver response ('abort' or 'quarantine').
            state_transition (str): State transition ('good' or 'bad').

        Returns:
            int: Cost value.
        """
        if response == "abort":
            return self.cost_abort
        elif response == "quarantine" and state_transition == "bad":
            return self.cost_quarantine_bad
        elif response == "quarantine" and state_transition == "good":
            return self.cost_quarantine_good
        else:
            return 0  # Default case, no cost

class OptimalPolicyAssigner:
    def __init__(self, system_states, table_I_values, table_II_values):
        """
        Initialize the OptimalPolicyAssigner with system states and tables.

        Args:
            system_states (list): List of system states.
            table_I_values (list): List of values from Table I.
            table_II_values (list): List of values from Table II.
        """
        self.system_states = system_states
        self.table_I_values = table_I_values
        self.table_II_values = table_II_values
        self.optimal_policies = {}

    def assign_optimal_policies(self):
        """
        Assign optimal control policies based on table values.
        """
        for i, state in enumerate(self.system_states):
            if self.table_I_values[i] > self.table_II_values[i]:
                self.optimal_policies[state] = "Policy_A"
            else:
                self.optimal_policies[state] = "Policy_B"

    def print_optimal_policies(self):
        """
        Print the assigned optimal control policies for each state.
        """
        print("Optimal Control Policies (π) for Each State:")
        for state, policy in self.optimal_policies.items():
            print(f"{state}: {policy}")

class TransitionProbabilityCalculator:
    def calculate_transition_probability(self, d, n, k):
        """
        Calculate transition probability λi,j,k.

        Args:
            d (int): Number of flows associated with host i.
            n (int): Total number of flows.
            k (int): Control parameter.

        Returns:
            float: Transition probability.
        """
        numerator = sum(range(1, d + 1))
        denominator = sum(range(1, n + 1))
    
        # Calculate the transition probability λi,j,k
        transition_probability = numerator / denominator
    
        return transition_probability
