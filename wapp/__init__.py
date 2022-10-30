import os
import json
from dotenv import load_dotenv
from flask import Flask

load_dotenv('env_template')

app = Flask(__name__)

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def reveal_all(path):
    output = {}
    output['path'] = path
    output['env'] = dict(os.environ.items())
    return json.dumps(output, indent=2)
# end def

if __name__ == '__main__':
    app.run('0.0.0.0', 8080, debug=True)
# end if
