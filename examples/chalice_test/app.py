import os
from chalice import Chalice

app = Chalice(app_name='chalice_test')


@app.route('/hello/world')
def index():
    return {'hello': 'world'}


working_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
config_path = os.path.join(working_dir, 'conf/test.yaml')

from swagger_ui import api_doc
api_doc(app, config_path=config_path, url_prefix='/api/doc')
