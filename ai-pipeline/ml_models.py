import pandas as pd
from sklearn.cluster import KMeans

def cluster_attacks(df, n_clusters=3):
    df_numeric = pd.get_dummies(df[['attack_type']])
    kmeans = KMeans(n_clusters=n_clusters, random_state=42)
    df['cluster'] = kmeans.fit_predict(df_numeric)
    return df

if __name__ == '__main__':
    df = pd.read_csv('preprocessed_logs.csv')
    df_clustered = cluster_attacks(df)
    print(df_clustered.head())
