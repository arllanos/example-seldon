from flask import Flask, request, Response
import json
import logging

logging.basicConfig(level=logging.DEBUG)

app = Flask(__name__)

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

features_per_id = {'1': ['1', '2'],
                   '2': ['3', '4'],
                   '3': ['5', '6']}
def build_elem(struct_elem):
    features_to_add = features_per_id[struct_elem['id']]
    struct_elem['values'] += features_to_add
    return struct_elem

@app.route('/api/features', methods=['GET'])
def get():
    data = json.loads(request.data)
    logger.info("Received data: " + str(data))
    data.ndarray = [build_elem(struct_elem) for struct_elem in data.ndarray]
    data.names = ['a', 'b', 'c']
    return Response(json.dumps(data), mimetype=u'application/json')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5500)