import pandas as pd
from sklearn.model_selection import train_test_split


# fonction qui charge un dataset et le split en 4

def load_and_prepare_data(path_csv = '../Data/base.csv'):
    df = pd.read_csv(path_csv, sep=';')

    df.drop(columns=['InternationalReference'], inplace = True)

    # separation cible et variable explicative
    y = df['is_churn']
    X = df.drop(columns=['is_churn'])

    # Separation des data app et test
    X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.2, random_state=42, stratify=y)

    return X_train, X_test, y_train, y_test

