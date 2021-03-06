### Алексей Заикин
# abc-telecom 
**Цели проекта:** анализ тарифов и услуг оператора связи, поиск оптимальных тарифов и оценка эффекта от их внедрения.

**Исходные данные:** файлы csv о пользоватлелях (колл-центрах), звонках и тарифах.

**Решение:** [тетрадь Jupyter Notebook](https://github.com/zaikinalex75/da-ds-portfolio/blob/main/abc-telecom/abc-telecom.ipynb), где сделано следующее: *загрузка* данных из файлов csv, *предобработка* (дубли, пропуски, выборсы), *биллинг* (расчёт стоимости потреблённых услуг для каждого пользователя помесячно), *исследование* пользователей и тарифов (распределение, доходность) за всё время и помесячно, *подбор* пользователям самых выгодных тарифов, *оценка* выручки после перехода всех пользователей на самые выгодные тарифы, *создание мат.модели* тарифов и расчёт вариантов их модификации для компенсации упущенной прибыли, *сравнение* пользователей разных тарифов (проверка стат.гипотез). 

**Итоги исследования по проекту:**
1. Клиенты оператора связи очень разнородны и обладают характеристиками в широком диапазоне: доход на клиента в месяц от 1 до 30 тыс.руб., количество соединений - от 1 до 30 тыс. в мес., длительность разговоров от 1 мин. до 10 тыс.мин. в месяц.
2. Средний клиент представляет собой очень небольшой call-центр: приносит доход - 2100 руб. в мес., операторов - 2 чел., звонков в  мес. - 33, длительность разговоров в мес. - 50 мин. в мес.
3. Тарифы приносят примерно одинаковый доход (примерно 200 тыс.руб. в мес.), но число пользователей тарифов и их характеристики существенно разные:  тариф А - 12% пользователей, тариф В - 35%, тариф С - 53%. Соответственно пользователи тарифа А приносят доход (и потребляют услуг) в несколько раз больше, чем пользователи тарифов В и С. Пользователи тарифа В опережают пользователей тарифа С в полтора-два раза. Проверка показывает, что эти различия статистически значимы и не являются следствием случайных влияний текущих факторов.
4. Пользователи тарифов переплачивают. Алгоритм выбора наиболее выгодного тарифа показывает, что подавляющему большинству пользователей тарифов А и В (более 90%) следует сменить свой тариф на тариф С. Это значит, что пользователи переоценили свои потребности в услугах связи и переплачивают.
5. Преход на оптимальные тарифы приведёт к снижению дохода. Переход пользователей на более выгодные тарифы сократит суммарный доход на 29%.

Рекомендации бизнесу:

- Привлечение новых клиентов и стимулирование имеющихся. Следует привлекать крупных клиентов, схожих по профилю с текущими пользователями тарифа А. Они дают в несколько раз больший доход, их потребности в связи растут. Имеющихся клиентов следует стимулировать. Способы стимулирования выходят за рамки данного проекта и требуют отдельного изучения.
- Риск перехода пользователей на более дешёвые тарифы может быть снижен, если предлагать сменить тариф не всем пользователям, которые могли бы это сделать, а только пользователям тарифа В. Если на более выгодные тарифы перейдут только они, то при максимальном числе довольных возможностью съэкономить пользователей общий доход упадёт не на 29%, а лишь на 15%.
- Компенсировать снижение дохода можно изменением тарифов. Калькулятор изменения тарифов позволяет расчтитать разные комбинации изменения параметров текущих тарифов для компенсации упущенного дохода. Например, расчёты показывают, что увеличение абонентской платы (на всех тарифах) на 70% полностью компенсирует переход всех пользователей на более экономные тарифы. Другой вариант: абонентская плата остаётся неизменной, но плату за оператора и минуту разговоров придётся увеличить на 100%. Возможны и другие варианты.

**Темы:** предобработка данных, исследовательский анализ, математическое моделирование, проверка гипотез. 

**Стек:** python, pandas, matplotlib, scipy.
