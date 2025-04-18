import re

logs = [
    "2025-04-16 17:22:19.601724 sshd[1234]: Failed password for guest from 192.168.1.1 port 62695 ssh2",
    "2025-04-16 17:22:19.601724 sshd[1234]: Invalid user guest from 10.0.0.5 port 43167 ssh2",
    "2025-04-16 17:22:19.601724 sshd[1234]: Connection closed by guest from 192.168.1.1 port 28399 ssh2"
]

patterns = [
    "Failed password",
    "Invalid user",
    "Connection closed by"
]

for line in logs:
    for pattern in patterns:
        if re.search(pattern, line, re.IGNORECASE):
            print(f"✅ MATCH: {pattern} IN → {line}")
