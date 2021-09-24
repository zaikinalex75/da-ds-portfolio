### Алексей Заикин

# toxic-comments
**Цели проекта:** выявление токсичных комментариев и описаний о товарах интернет-магазина.

**Исходные данные:** файл csv с комментариями, помеченными как токсичные или нет.

**Решение:** [тетрадь Jupyter Notebook](https://github.com/zaikinalex75/da-ds-portfolio/blob/main/toxic-comments/toxic-comments.ipynb), где сделано следующее: *загрузка* данных из файла csv, *предобработка* (очистка от ненужных симоволов), *лемматизация*, *векторизация* (методом TF-IDF), *обучение* моделей вида Logistic Regression (scikit-learn), Desision Tree (scikit-learn), Random Forest (scikit-learn), LightGBM, CatBoost, XGBoost с подбором гиперпараметров и оценкой по метрикам F1, Recall и Precision-Reacall AUC. 

**Темы:** ML на текстовых данных, лемматизация, TF-IDF, бинарная классификация. 

**Стек:** python, pandas, nltk, scikit-learn, LightGBM, CatBoost, XGBoost. 
