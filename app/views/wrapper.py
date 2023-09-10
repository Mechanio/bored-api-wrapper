from flask import jsonify, request, Blueprint
import requests
import json


from app.models import ActivityModel


wrapper_bp = Blueprint('wrapper', __name__)


@wrapper_bp.route("/api/activity/", methods=["GET"])
def get_activity():
    """
    Get activity from bored_api
    :return: json with activity info
    """
    params_list = ["key", "type", "participants", "price", "minprice", "maxprice",
                "accessibility", "minaccessibility", "maxaccessibility"]
    params = request.args.to_dict()
    result_params = {key: value for key, value in params.items() if key in params_list and value is not None}
    data = requests.get("https://www.boredapi.com/api/activity/", params=result_params)
    data = json.loads(data.text)
    if "error" in data:
        return jsonify({"message": "No activity found with the specified parameters"}), 400
    activity = ActivityModel(key=data["key"], activity=data["activity"], type=data["type"], participants=data["participants"],
                             price=data["price"], link=data["link"], accessibility=data["accessibility"])
    activity.save_to_db()
    return jsonify(data)


@wrapper_bp.route("/api/get_activities/", methods=["GET"])
def get_saved_activities():
    """
    Get 5 last activities from database
    :return: json with activities info
    """
    activities = ActivityModel.return_latest_activities()

    return jsonify(activities)
