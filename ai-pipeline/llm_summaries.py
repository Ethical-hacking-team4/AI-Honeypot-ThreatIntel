def generate_summary(df):
    summary = f'Total attacks: {len(df)}\n'
    summary += f'Unique attack types: {df["attack_type"].nunique()}\n'
    summary += f'Unique source IPs: {df["src_ip"].nunique()}\n'
    return summary

if __name__ == '__main__':
    import pandas as pd
    df = pd.read_csv('clustered_logs.csv')
    report = generate_summary(df)
    print(report)
