import random

class SecurityAgent:
    def __init__(self):
        self.utility = {'Safe': 10, 'Low Risk Vulnerable': -5, 'High Risk Vulnerable': -10}
        self.low_risk_vulnerabilities = []
        self.high_risk_vulnerabilities = []

    def calculate_utility(self, status):
        return self.utility[status]

    def scan_component(self, component, status):
        if status == 'Low Risk Vulnerable':
            self.low_risk_vulnerabilities.append(component)
            return f"Warning: Component {component} has a Low Risk Vulnerability!"
        elif status == 'High Risk Vulnerable':
            self.high_risk_vulnerabilities.append(component)
            return f"ALERT: Component {component} has a High Risk Vulnerability! Premium service required."
        else:
            return f"Component {component} is secure."

    def patch_low_risk_vulnerabilities(self, environment):
        for component in self.low_risk_vulnerabilities:
            environment.patch_component(component)
            print(f"Patched Low Risk Vulnerability in Component {component}.")
        self.low_risk_vulnerabilities.clear()

class SecuritySystem:
    def __init__(self):
        self.components = {chr(65 + i): random.choice(['Safe', 'Low Risk Vulnerable', 'High Risk Vulnerable']) for i in range(9)}

    def get_system_state(self):
        return self.components

    def patch_component(self, component):
        self.components[component] = 'Safe'

def run_security_check(agent, system):
    total_utility = 0
    print("Initial System State:")
    initial_state = system.get_system_state()
    for component, status in initial_state.items():
        print(f"{component}: {status}")

    print("\nScanning System...")
    for component, status in initial_state.items():
        log_message = agent.scan_component(component, status)
        print(log_message)
        total_utility += agent.calculate_utility(status)

    print("\nPatching Low Risk Vulnerabilities...")
    agent.patch_low_risk_vulnerabilities(system)
    print("\nFinal System State:")
    final_state = system.get_system_state()
    for component, status in final_state.items():
        print(f"{component}: {status}")

    # High Risk Vulnerability Report
    if agent.high_risk_vulnerabilities:
        print("\nUnresolved High Risk Vulnerabilities (Premium Service Required):")
        for component in agent.high_risk_vulnerabilities:
            print(f"- Component {component}")

    print("\nTotal Utility:", total_utility)


security_agent = SecurityAgent()
security_system = SecuritySystem()
run_security_check(security_agent, security_system)
