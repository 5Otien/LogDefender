import random
from datetime import datetime
import os
def generate_ssh_logs(filename):
    ips = ["192.168.1.1", "10.0.0.5", "172.16.0.2", "203.0.113.99"]
    users = ["root", "admin", "guest", "test"]
    events = [
        "Failed password for",
        "Accepted password for",
        "Invalid user",
        "Connection closed by"
    ]

    with open(filename, "w") as f:
        for _ in range(50):
            ip = random.choice(ips)
            user = random.choice(users)
            event = random.choice(events)
            log_line = f"{datetime.now()} sshd[1234]: {event} {user} from {ip} port {random.randint(1024,65535)} ssh2\n"
            f.write(log_line)

def generate_apache_logs(filename):
    ips = ["198.51.100.23", "203.0.113.77", "192.0.2.15"]
    endpoints = ["/admin", "/index.php", "/login", "/wp-login.php", "/"]
    methods = ["GET", "POST"]
    user_agents = ["Mozilla/5.0", "curl/7.68.0", "sqlmap", "Nmap"]

    with open(filename, "w") as f:
        for _ in range(50):
            ip = random.choice(ips)
            endpoint = random.choice(endpoints)
            method = random.choice(methods)
            agent = random.choice(user_agents)
            status = random.choice(["200", "404", "403"])
            log_line = f'{ip} - - [{datetime.now().strftime("%d/%b/%Y:%H:%M:%S")} +0000] "{method} {endpoint} HTTP/1.1" {status} - "{agent}"\n'
            f.write(log_line)

os.makedirs("logs", exist_ok=True)

generate_ssh_logs("logs/ssh.log")
generate_apache_logs("logs/apache.log")

