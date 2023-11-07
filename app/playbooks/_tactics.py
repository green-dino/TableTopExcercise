class Tactic:
    def __init__(self, name):
        self.name = name

    def perform(self):
        raise NotImplementedError("Subclasses must implement the 'perform' method.")

class Reconnaissance(Tactic):
    def perform(self):
        print(f"Performing Reconnaissance: {self.name}")

class ResourceDevelopment(Tactic):
    def perform(self):
        print(f"Performing Resource Development: {self.name}")

class InitialAccess(Tactic):
    def perform(self):
        print(f"Performing Initial Access: {self.name}")

class Execution(Tactic):
    def perform(self):
        print(f"Performing Execution: {self.name}")

class Persistence(Tactic):
    def perform(self):
        print(f"Performing Persistence: {self.name}")

class PrivilegeEscalation(Tactic):
    def perform(self):
        print(f"Performing Privilege Escalation: {self.name}")

class DefenseEvasion(Tactic):
    def perform(self):
        print(f"Performing Defense Evasion: {self.name}")

class CredentialAccess(Tactic):
    def perform(self):
        print(f"Performing Credential Access: {self.name}")

class Discovery(Tactic):
    def perform(self):
        print(f"Performing Discovery: {self.name}")

class LateralMovement(Tactic):
    def perform(self):
        print(f"Performing Lateral Movement: {self.name}")

class Collection(Tactic):
    def perform(self):
        print(f"Performing Collection: {self.name}")

class CommandAndControl(Tactic):
    def perform(self):
        print(f"Performing Command and Control: {self.name}")

class Exfiltration(Tactic):
    def perform(self):
        print(f"Performing Exfiltration: {self.name}")

class Impact(Tactic):
    def perform(self):
        print(f"Performing Impact: {self.name}")

# Create instances of tactics
tactics = [
    Reconnaissance("Tactic1"),
    ResourceDevelopment("Tactic2"),
    InitialAccess("Tactic3"),
    Execution("Tactic4"),
    Persistence("Tactic5"),
    PrivilegeEscalation("Tactic6"),
    DefenseEvasion("Tactic7"),
    CredentialAccess("Tactic8"),
    Discovery("Tactic9"),
    LateralMovement("Tactic10"),
    Collection("Tactic11"),
    CommandAndControl("Tactic12"),
    Exfiltration("Tactic13"),
    Impact("Tactic14")
]

# Perform actions for each tactic
for tactic in tactics:
    tactic.perform()
