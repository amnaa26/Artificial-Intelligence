import random

class BackupManagementAgent:
    def __init__(self):
        self.utility = {'Completed': 10, 'Failed': -10}
        self.failed_backups = []

    def calculate_utility(self, status):
        return self.utility[status]

    def scan_backups(self, task_id, status):
        if status == 'Failed':
            self.failed_backups.append(task_id)
            return f"Warning: Backup Task {task_id} has failed!"
        else:
            return f"Backup Task {task_id} completed successfully."

    def retry_failed_backups(self, environment):
        for task_id in self.failed_backups:
            environment.retry_backup(task_id)
            print(f"Retried and completed Backup Task {task_id}.")
        self.failed_backups.clear()

class BackupSystem:
    def __init__(self):
        self.backup_tasks = {f"Task{i+1}": random.choice(['Completed', 'Failed']) for i in range(5)}

    def get_backup_status(self):
        return self.backup_tasks

    def retry_backup(self, task_id):
        self.backup_tasks[task_id] = 'Completed'

def run_backup_agent(agent, system):
    total_utility = 0
    print("Initial Backup Task Status:")
    initial_status = system.get_backup_status()
    for task, status in initial_status.items():
        print(f"{task}: {status}")
    print("\nScanning Backup Tasks...")
    for task, status in initial_status.items():
        log_message = agent.scan_backups(task, status)
        print(log_message)
        total_utility += agent.calculate_utility(status)
    print("\nRetrying Failed Backups...")
    agent.retry_failed_backups(system)
    print("\nFinal Backup Task Status:")
    final_status = system.get_backup_status()
    for task, status in final_status.items():
        print(f"{task}: {status}")

    print("\nTotal Utility:", total_utility)


backup_agent = BackupManagementAgent()
backup_system = BackupSystem()
run_backup_agent(backup_agent, backup_system)
