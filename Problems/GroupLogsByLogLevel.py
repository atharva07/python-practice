from collections import defaultdict

logs = [
    "INFO: Service started",
    "ERROR: DB failed",
    "WARNING: Disk low",
    "ERROR: Timeout",
    "INFO: Request received"
]

groupedLogs = defaultdict(list)

for log in logs:
    level = log.split(":")[0]
    groupedLogs[level].append(log)

print(dict(groupedLogs))
