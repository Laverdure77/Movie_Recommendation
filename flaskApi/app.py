
from flask import Flask
from flask import jsonify
from flask import request
from flask import json
from flask import make_response
from flask_cors import CORS
from function import get_recommendations
import uvicorn

app = Flask(__name__)
CORS(app)

@app.route("/")
def greeting():
    return {"greeting" : "Hello from Flask Recommandation API!"}

@app.route('/recommandation', methods=['POST'])
def recommandation():
    error = None
    if request.method == 'POST':
        content_type = request.headers.get('Content-Type')
        if (content_type == 'application/json'):
            datas = request.json
            overviews = ','.join([i for i in datas])
            # get the recommandation
            reco = get_recommendations(overviews)
            # format the answer
            films = reco.title.to_dict()
            # Build json response
            response = app.response_class(
                response=json.dumps(films),
                # response=films,
                status=200,
                mimetype='application/json'
            )
            print(response)
            return response
        else:
            error = "Content type is not supported."
            return make_response(jsonify(error, 200))
            

# App run
port = 5100
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=port, debug=True)