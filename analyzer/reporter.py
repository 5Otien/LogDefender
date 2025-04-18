import os
from datetime import datetime

def generate_report(alerts, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    now = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = os.path.join(output_folder, f"alerts_{now}.txt")

    with open(filename, "w", encoding="utf-8") as f:
        for alert in alerts:
            f.write(f"[{alert['level'].upper()}] {alert['rule']} -> {alert['line']}\n")

    print(f"Report saved to {filename}")
