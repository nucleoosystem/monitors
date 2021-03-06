from datetime import datetime
from random import randint

databases = connection.Query('''
    SELECT datname AS datname,
           round(pg_catalog.pg_database_size(datname)/1048576.0,2) AS size
    FROM pg_catalog.pg_database
    WHERE NOT datistemplate
    ORDER BY
        CASE WHEN pg_catalog.has_database_privilege(datname, 'CONNECT')
             THEN pg_catalog.pg_database_size(datname)
             ELSE NULL
        END DESC
''')

datasets = []
for db in databases.Rows:
    color = "rgb(" + str(randint(125, 225)) + "," + str(randint(125, 225)) + "," + str(randint(125, 225)) + ")"
    datasets.append({
            "label": db['datname'],
            "fill": False,
            "backgroundColor": color,
            "borderColor": color,
            "lineTension": 0,
            "pointRadius": 1,
            "borderWidth": 1,
            "data": [db["size"]]
        })

result = {
    "labels": [datetime.now().strftime('%H:%M:%S')],
    "datasets": datasets
}
