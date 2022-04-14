import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, precision_score, recall_score, f1_score
from sklearn.preprocessing import LabelEncoder
from sklearn.base import clone
from xgboost import XGBRegressor, XGBClassifier
from catboost import CatBoostRegressor, CatBoostClassifier
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor, DecisionTreeClassifier
from sklearn.ensemble import RandomForestRegressor, RandomForestClassifier
from sklearn.model_selection import KFold


REGRESSION = 'regression'
CLASSIFICATION = 'classification'


def main():
    # dataset original url: https://www.kaggle.com/datasets/uciml/student-alcohol-consumption
    dataset = pd.read_csv('student-mat.csv')
    print(dataset.head())

    categorical_columns = [
        'school', 'sex', 'address', 'famsize', 'Pstatus',
        'Mjob', 'Fjob', 'reason', 'guardian', 'schoolsup',
        'famsup', 'paid', 'activities', 'nursery', 'higher',
        'internet', 'romantic'
    ]

    for column in categorical_columns:
        dataset[column] = dataset[column].astype('category').cat.codes

    labels = {
        CLASSIFICATION: ['health', 'Dalc', 'Walc'],
        REGRESSION: ['G1', 'G2', 'G3'],
    }

    models = {
        REGRESSION: [
            {'name': 'lin reg', 'model': LinearRegression()},
            {'name': 'tree', 'model': DecisionTreeRegressor()},
            {'name': 'rand forest', 'model': RandomForestRegressor()},
            {'name': 'xgboost', 'model': XGBRegressor()},
            {'name': 'catboost', 'model': CatBoostRegressor(verbose=False)}
        ],

        CLASSIFICATION: [
            {'name': 'tree', 'model': DecisionTreeClassifier()},
            {'name': 'rand forest', 'model': RandomForestClassifier()},
            {'name': 'xgboost', 'model': XGBClassifier()},
            {'name': 'catboost', 'model': CatBoostClassifier(verbose=False)}
        ]
    }

    for task in labels:
        print(f'Task: {task}')

        for model_info in models[task]:
            print(f"    {model_info['name']}")

            for label_column in labels[task]:
                feature_columns = [name for name in dataset.columns if name != label_column]
                data_x = dataset[feature_columns]
                data_y = dataset[label_column]
                data_y = LabelEncoder().fit_transform(data_y)

                kfold = KFold(n_splits=10)

                metrics = {
                    'train': {
                        'score': [],
                        'mse': [],
                        'precision': [],
                        'recall': [],
                        'f1': []
                    },

                    'test': {
                        'score': [],
                        'mse': [],
                        'precision': [],
                        'recall': [],
                        'f1': []
                    }
                }

                for fold, (train_index, test_index) in enumerate(kfold.split(data_x)):
                    train_x, test_x = data_x.iloc[train_index], data_x.iloc[test_index]
                    train_y, test_y = data_y[train_index], data_y[test_index]

                    model = clone(model_info['model'])
                    model.fit(train_x, train_y)

                    train_pred = model.predict(train_x)
                    test_pred = model.predict(test_x)

                    metrics['train']['score'].append(model.score(train_x, train_y))
                    metrics['test']['score'].append(model.score(test_x, test_y))

                    if task == REGRESSION:
                        metrics['train']['mse'].append(mean_squared_error(train_pred, train_y))
                        metrics['test']['mse'].append(mean_squared_error(test_pred, test_y))
                    else:
                        metrics['train']['precision'].append(precision_score(train_pred, train_y, average='macro'))
                        metrics['test']['precision'].append(precision_score(test_pred, test_y, average='macro'))
                        metrics['train']['recall'].append(recall_score(train_pred, train_y, average='macro'))
                        metrics['test']['recall'].append(recall_score(test_pred, test_y, average='macro'))
                        metrics['train']['f1'].append(f1_score(train_pred, train_y, average='macro'))
                        metrics['test']['f1'].append(f1_score(test_pred, test_y, average='macro'))

                print(f'        Label: {label_column}')
                print(f"        - Train score: {np.mean(metrics['train']['score']):.4}")

                if task == REGRESSION:
                    print(f"        - Train MSE: {np.mean(metrics['train']['mse']):.4}")
                else:
                    print(f"        - Train precision: {np.mean(metrics['train']['precision']):.4}")
                    print(f"        - Train recall: {np.mean(metrics['train']['recall']):.4}")
                    print(f"        - Train f1: {np.mean(metrics['train']['f1']):.4}")

                print(f"        - Test score: {np.mean(metrics['test']['score']):.4}")

                if task == REGRESSION:
                    print(f"        - Test MSE: {np.mean(metrics['test']['mse']):.4}\n")
                else:
                    print(f"        - Test precision: {np.mean(metrics['test']['precision']):.4}")
                    print(f"        - Test recall: {np.mean(metrics['test']['recall']):.4}")
                    print(f"        - Test f1: {np.mean(metrics['test']['f1']):.4}")

                print('')


if __name__ == '__main__':
    main()
