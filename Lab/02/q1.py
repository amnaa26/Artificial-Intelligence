import random

class SecurityAgent:
    def __init__(self):
        self.utility = {'Vulnerable': -10, 'Safe': 10}
        self.vulnerable_components = []

    def calculate_utility(self, status):
        return self.utility[status]

    def scan_component(self, component, status):
        if status == 'Vulnerable':
            self.vulnerable_components.append(component)
            return f"Warning: Component {component} is vulnerable!"
        else:
            return f"Component {component} is secure."

    def patch_vulnerabilities(self, environment):
        for component in self.vulnerable_components:
            environment.patch_component(component)
            print(f"Patched Component {component}.")
        self.vulnerable_components.clear()

class SecuritySystem:
    def __init__(self):
        self.components = {chr(65 + i): random.choice(['Safe', 'Vulnerable']) for i in range(9)}

    def get_system_state(self):
        return self.components

    def patch_component(self, component):
        self.components[component] = 'Safe'

def run_security_check(agent, system):
    total_utility = 0

    # Initial System Check
    print("Initial System State:")
    initial_state = system.get_system_state()
    for component, status in initial_state.items():
        print(f"{component}: {status}")

    # System Scan
    print("\nScanning System...")
    for component, status in initial_state.items():
        log_message = agent.scan_component(component, status)
        print(log_message)
        total_utility += agent.calculate_utility(status)

    # Patching Vulnerabilities
    print("\nPatching Vulnerabilities...")
    agent.patch_vulnerabilities(system)

    # Final System Check
    print("\nFinal System State:")
    final_state = system.get_system_state()
    for component, status in final_state.items():
        print(f"{component}: {status}")

    print("\nTotal Utility:", total_utility)

# Creating object of agent and system
security_agent = SecurityAgent()
security_system = SecuritySystem()

# Run the security check
run_security_check(security_agent, security_system)
