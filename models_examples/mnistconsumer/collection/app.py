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
    # data.ndarray is a 2 dimensional array. This means
    # an array containing arrays as elements.
    # Every element array contains then 2 sub-elements where, by convention, the first one corresponds to an ID
    # and the second one to an value which can be an scalar or even another array contains as first element (this is by convention) the id that identifies the rest of items in the array
    # (which not necessarily are scalars, they may be also arrays (think of a multi label classification for example
    data.ndarray = [struct_elem for struct_elem in data.ndarray]
    data.names = ['a', 'b', 'c']
    logger.info("Received IDs: " + str(ids))
    return Response(json.dumps([{sample_id: [1,2,3]} for sample_id in ids]), mimetype=u'application/json')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5500)