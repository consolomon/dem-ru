sandbox.py — flask веб-сервер, идёт в YouTubeAPI. хост http://localhost:7070
Запрашивает ключи, переходит на страницу получения ключей и затем переходит на страницу выдачи ключей
yt_channels_stats_etl.py — youtube_auth() идёт на фласк веб-сервер из Airflow в контейнере. хост снаружи докера localhost:8080, внутри докера у него другой
По ссылке авторизации в ютубе yt_channels_stats_etl.py свободно идёт, а на мой flask сервер идти не хочет, пишет вот это:

requests.exceptions.ConnectionError: HTTPConnectionPool(host='localhost', port=7070): Max retries exceeded with url: /get_credentials (Caused by NewConnectionError('<urllib3.connection.HTTPConnection object at 0x7f06de62db90>: Failed to establish a new connection: [Errno 111] Connection refused'))
