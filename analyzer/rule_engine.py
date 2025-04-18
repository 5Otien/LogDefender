import re
import yaml

def load_rules(file_path):
    with open(file_path, 'r') as file:
        return yaml.safe_load(file)
def load_logs(file_path):
    with open(file_path, 'r') as file:
        return file.readlines()  
def apply_rules(logs, rules):
    alerts = []
    for log_line in logs:
        log_line = log_line.strip()  
        for rule in rules:
            if re.search(rule["pattern"], log_line):
                alerts.append({
                    "line": log_line,           
                    "rule": rule["name"],
                    "level": rule["level"]
                })
    return alerts


if __name__ == "__main__":
    rules_file = "rules.yaml"
    logs_file = "logs.txt"

    rules = load_rules(rules_file)
    logs = load_logs(logs_file)

    apply_rules(rules, logs)
