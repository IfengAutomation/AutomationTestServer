import testserver

if __name__ == '__main__':
    app = testserver.get_from_cfg('config.py')
    app.run('0.0.0.0', 8080, use_reloader=False, threaded=True)
