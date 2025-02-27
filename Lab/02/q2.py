import random

class LoadBalancerAgent:
    def __init__(self):
        self.utility = {'Underloaded': -5, 'Balanced': 10, 'Overloaded': -10}
        self.overloaded_servers = []
        self.underloaded_servers = []

    def calculate_utility(self, status):
        return self.utility[status]

    def scan_servers(self, server_name, status):
        if status == 'Overloaded':
            self.overloaded_servers.append(server_name)
            return f"Warning: Server {server_name} is overloaded!"
        elif status == 'Underloaded':
            self.underloaded_servers.append(server_name)
            return f"Note: Server {server_name} is underloaded."
        else:
            return f"Server {server_name} is balanced."

    def balance_load(self, environment):
        while self.overloaded_servers and self.underloaded_servers:
            overloaded = self.overloaded_servers.pop(0)
            underloaded = self.underloaded_servers.pop(0)
            environment.redistribute_load(overloaded, underloaded)
            print(f"Balanced load: Moved tasks from {overloaded} to {underloaded}.")

class DataCenter:
    def __init__(self):
        self.servers = {f"Server{i+1}": random.choice(['Underloaded', 'Balanced', 'Overloaded']) for i in range(5)}

    def get_system_state(self):
        return self.servers

    def redistribute_load(self, overloaded, underloaded):
        self.servers[overloaded] = 'Balanced'
        self.servers[underloaded] = 'Balanced'


def run_load_balancer(agent, system):
    total_utility = 0
    print("Initial Server Load Status:")
    initial_state = system.get_system_state()
    for server, status in initial_state.items():
        print(f"{server}: {status}")
    print("\nScanning Servers...")
    for server, status in initial_state.items():
        log_message = agent.scan_servers(server, status)
        print(log_message)
        total_utility += agent.calculate_utility(status)

    print("\nBalancing Server Load...")
    agent.balance_load(system)

    print("\nFinal Server Load Status:")
    final_state = system.get_system_state()
    for server, status in final_state.items():
        print(f"{server}: {status}")

    print("\nTotal Utility:", total_utility)


load_balancer = LoadBalancerAgent()
data_center = DataCenter()
run_load_balancer(load_balancer, data_center)
