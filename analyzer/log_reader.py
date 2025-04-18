def read_logs(filepath):
    with open(filepath, "r", encoding="utf-8", errors="ignore") as file:
        return [line.strip() for line in file if line.strip()]
