from flask import Flask
from app.stringfy import stringfy
from app.to_uppercase import to_uppercase
import platform


def create_app():
    app = Flask(__name__)

    @app.route('/')
    def show():
        py_build = to_uppercase(platform.python_build())
        py_compiler = platform.python_compiler()
        processor = platform.processor()
        os_realease = platform.release()
        py_revision = platform.python_version()
        system = platform.system()
        machine_type = platform.machine()
        uname = stringfy(platform.uname(), '|*|')

        

        output = {
            "build_do_python": py_build,
            "compilador_do_python": py_compiler,
            "processador": processor,
            "release_do_sistema": os_realease,
            "revisao_do_python": py_revision,
            "sistema": system,
            "tipo_da_maquina": machine_type,
            "uname": uname,

        }

        return output

    return app
