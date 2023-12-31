from os.path import join


class PATH:
    hdfs = '/hdfs'
    dfs  = '/dfs'
    app  = 'realtime_trend_pipeline'

    dags = join('/opt/airflow', 'dags')
    src  = join(dags, app)
    operators = join(src, 'operators')
    
    input  = join(dfs, app, 'input')
    output = join(dfs, app, 'output')
