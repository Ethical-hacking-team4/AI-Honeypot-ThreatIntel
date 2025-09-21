import pandas as pd

def preprocess_logs(df):
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    df['src_ip'] = df['src_ip'].astype(str)
    df['attack_type'] = df.get('eventid', 'unknown')
    df = df[['timestamp', 'src_ip', 'attack_type']]
    return df

if __name__ == '__main__':
    df = pd.read_csv('sample_combined_logs.csv')
    df_clean = preprocess_logs(df)
    print(df_clean.head())
