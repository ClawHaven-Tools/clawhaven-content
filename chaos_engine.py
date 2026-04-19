#!/usr/bin/env python3
import random
import time
import json
from datetime import datetime

def generate_chaos():
    projects = ["Neural Mesh", "Void Protocol", "Spectral Link", "Core Breach"]
    status = ["CRITICAL", "STABLE", "SYNCING", "NULL"]
    return {
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "project": random.choice(projects),
        "status": random.choice(status),
        "anomaly": random.randint(100, 999)
    }

while True:
    data = generate_chaos()
    with open('chaos_log.json', 'w') as f:
        json.dump(data, f)
    time.sleep(5)
