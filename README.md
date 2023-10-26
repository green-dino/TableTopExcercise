# Tabletop Tool 

Achieving mission objectives in complex and increasingly adversarial networks is difficult even under the best of circumstances. Currently, there are few tools for reasoning about how to react to rapid changes in a given network's environmental state; that is, we do not know how to cope with adversarial actions in hostile environments. Consider a preliminary operational model that combines the states, detection outputs, and agility maneuvers associated with a cyber-operation in hostile networks. The goal is positing the development of an operational model to aid in the successful completion of mission objectives with a minimal maneuver cost.

Many challenges arise in cyber-decision making—what is the best action (maneuver) to take in a given environment based on understanding of the current state (situational awareness) and mission needs? Proper responses to changes in system states, detection outputs, and agility maneuvers are necessary in order to achieve mission objectives. However, today's conventional cyber-defense mostly considers static attack responses in each interval of a finite horizon.

How do defenders select maneuvers to optimize the security outcomes in uncertain environments? To address this question, we present a graphical representation of an operational model. This representation incorporates nodes (states), transitions, and control variables. We define detection and agility as they pertain to the proposed model. These areas, in concert with the model we have described, form the grounding necessary to reason through a policy that must be created to guide the best action to take for minimizing the overall attack response costs.

To address these aspects, we can use the dynamic programming approach discussed earlier to find the optimal policy for controlling network operations. This approach considers the impact of adversarial actions, costs of control actions, and the mission objective of securing the network in a hostile cyber environment.

Operational Model:

Dynamic System: A computer network with multiple hosts and communication links.
State Space: The state of the network represented by the health status of individual hosts and network traffic.
Control Actions: Actions to protect and maintain the network, such as implementing security measures, applying patches, or isolating compromised hosts.
System Dynamics: The state of the network evolves over discrete time steps, influenced by host status, network traffic, and adversarial actions.
Cost Function: The cost of maintaining the network, handling adversarial actions, and implementing control measures.
Mission Objective:

Objective: Ensure the reliability and security of the computer network.
Optimal Policy: Find the optimal policy for taking control actions to minimize network vulnerabilities and potential attacks.
Adversarial Action:

Adversary: An attacker attempting to compromise network hosts or disrupt network operations.
Attack Estimation: The probability of an attack occurring at each time step.
Adversarial Maneuvers: The attacker's actions to exploit vulnerabilities and disrupt network operations.
Hostile Environment:

Network Threats: The network operates in a hostile environment where various cyber threats are constantly present.
Vulnerabilities: Hosts may have vulnerabilities that could be exploited by attackers.
Unpredictability: Adversarial actions may be unpredictable, making it challenging to defend the network.
Cyber-Operation:

Control Actions: Actions taken by the network administrator to secure the network, including patching vulnerabilities, isolating compromised hosts, and monitoring network traffic.
Dynamic Response: The network's response to adversarial actions and evolving conditions.
Optimal Policy: Determine the best actions to minimize vulnerabilities and protect network integrity.
Minimal Maneuver Cost:

Cost Assignments: Assigning costs to control actions, such as patching, isolating hosts, or monitoring. The goal is to minimize the overall cost of maintaining network security.
Host Remediation:

Response to Attacks: When an attack is detected, take actions to remediate compromised hosts, remove malicious software, and restore normal operation.
Attack Prevention:

Preventive Measures: Implement measures to prevent attacks, including firewall rules, intrusion detection systems, and timely patch management.

## Features

- User Management: Register, log in, and manage user profiles.
- Scenario Selection: Choose from a list of available tabletop scenarios.
- Game Analysis: Perform analysis based on user inputs and view the results.
- Playbook Building: Generate playbooks tailored to your game analysis.

## Prerequisites

- Python 3.6 or higher
- [Poetry](https://python-poetry.org/) for dependency management
- A modern web browser

## Installation
 
1. Clone the repository:

   ```bash
   git clone git@github.com:green-dino/TableTopExcercise.git
   cd tabletop-tool
   ```

2. Initialize the virtual environment and install dependencies:

   ```bash
   poetry install
   ```

3. Activate the virtual environment:

   ```bash
   poetry shell
   ```

4. Start the Flask application:

   ```bash
   python run.py
   ```

The application will be accessible at `http://localhost:5000` in your web browser.

## Usage

- Visit `http://localhost:5000` to access the Tabletop Tool.
- Register a new user or log in with an existing account.
- Select a tabletop scenario and perform analysis.
- Build custom playbooks based on the analysis results.

## Linting

This project uses Flake8 for linting. To check your code for compliance, run:

```bash
poetry run lint
```

## Configuration

- Database configurations and other application settings can be found in the `config.py` file.
- You can customize the Flask application in `app/` and its subdirectories.

## Contributing

Contributions are welcome! If you'd like to improve this project, please open an issue or create a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Flask: [Flask Documentation](https://flask.palletsprojects.com/)
- Poetry: [Poetry Documentation](https://python-poetry.org/)
- Flake8: [Flake8 Documentation](https://flake8.pycqa.org/)


