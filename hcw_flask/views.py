import json
import utility

from hcw_flask import app
from hcw_flask.models import Reports, Interactions

from flask import request


@app.route('/')
def index():
    return utility.test_response()


@app.route('/reports', methods=['POST'])
def create_new_report():
    data = json.loads(request.data) if request.data else request.form.to_dict()
    result = Reports.create_report(data)
    return utility.to_response(result)


@app.route('/report/<report_id>/most-recent', methods=['GET'])
def get_most_recent(report_id):
    result = Reports.fetch_most_recent_report(report_id)
    return utility.to_response(result)


@app.route('/report/<report_id>', methods=['GET'])
def get_all_reports_for_id(report_id):
    result = Reports.fetch_reports(report_id)
    return utility.to_response(result)


@app.route('/report/<report_id>', methods=['PUT'])
def update_existing_report(report_id):
    result = Reports.update_report(report_id)
    return utility.to_response(result)


@app.route('/interactions', methods=['POST'])
def interactions():
    data = json.loads(request.data) if request.data else request.form.to_dict()
    result = Interactions.create_interaction(data)
    return utility.to_response(result)
