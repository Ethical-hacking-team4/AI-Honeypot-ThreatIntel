import json
import os
import pandas as pd

def load_cowrie_logs(log_dir='honeypots/cowrie-logs'):
    all_logs = []
    for file in os.listdir(log_dir):
        if file.endswith('.json'):
            with open(os.path.join(log_dir, file), 'r') as f:
                for line in f:
                    all_logs.append(json.loads(line))
    df = pd.DataFrame(all_logs)
    return df

if __name__ == '__main__':
    df_cowrie = load_cowrie_logs()
    print(df_cowrie.head())
