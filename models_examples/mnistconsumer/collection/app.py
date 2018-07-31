from flask import Flask, request, Response
import json
import logging
import sys

logging.basicConfig(level=logging.DEBUG)

app = Flask(__name__)

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


@app.route('/api/features', methods=['GET'])
def get():
    ids = json.loads(request.data)
    logger.info("Received IDs: " + str(ids))
    return Response(json.dumps([1,2,3]), mimetype=u'application/json')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5500)