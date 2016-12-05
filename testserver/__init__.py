from flask import Flask
from testserver import blueprints

app = Flask('Automation')


def init():
    for bp_module in blueprints.__all__:
        app.register_blueprint(bp_module.bp)


def get_from_env(var_name):
    init()
    app.config.from_envvar(var_name)
    return app


def get_from_cfg(cfg_file):
    init()
    app.config.from_pyfile(cfg_file)
    return app

