import os
import yaml
from analyzer.log_reader import read_logs
from analyzer.rule_engine import apply_rules
from analyzer.reporter import generate_report
from  DATAFARM import generate_visualizations

with open("config.yaml", "r") as f:
    config = yaml.safe_load(f)
print(config)

log_folder = config["log_folder"]
rule_folder = config["rule_folder"]
output_folder = config["output_folder"]
alert_level = config["alert_level"]

all_logs = []
for filename in os.listdir(log_folder):
    path = os.path.join(log_folder, filename)
    print(f"📄 Total logs loaded: {len(all_logs)}")
    for line in all_logs:
        print("📝", line)

    all_logs += read_logs(path)


with open(os.path.join(rule_folder, "rules.yaml"), "r") as f:
    data = yaml.safe_load(f)
    print("🔎 YAML content:", data)
    rules = data["rules"]

alerts = apply_rules(all_logs, rules)

generate_report(alerts, output_folder)

generate_visualizations()