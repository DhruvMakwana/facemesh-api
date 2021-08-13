# importing libraries
from flask import Flask, request
from run import main

app = Flask(__name__)

@app.route("/upload/facemesh")
def facemesh():
    image = request.args.get('image')
    distance_dict, angle_dict = main(image)
    output = {}
    output["distance_dict"] = distance_dict
    output["angle_dict"] = angle_dict
    return {"data": output}

if __name__ == "__main__":
    app.run()