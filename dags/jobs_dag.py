from datetime import datetime
from airflow import DAG

configs = {
    'dag_test_1': {'schedule_interval': "0 0 * * *", "start_date": datetime(2019, 02, 25)},
    'dag_test_2': {'schedule_interval': "0 0 * * *", "start_date": datetime(2019, 02, 25)},
    'dag_test_3': {'schedule_interval': "0 0 * * *", "start_date": datetime(2019, 02, 25)}
}

scheduleInterval = 'schedule_interval'
startDate = 'start_date'

for key, value in configs.iteritems():
    # Without context manager because you don't need the automatically assign new operators
    globals()[key] = DAG(key, default_args=value)
