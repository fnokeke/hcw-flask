from hcw_flask import app
from flask_sqlalchemy import SQLAlchemy

from datetime import datetime

import json

db = SQLAlchemy(app)


class Interactions(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    source = db.Column(db.String(15))
    type = db.Column(db.String(15))
    session_id = db.Column(db.String(30))

    def __init__(self, info):
        self.source = info['source']
        self.type = info['type']
        self.session_id = info['session_id']

    @staticmethod
    def create_interaction(info):
        new_interaction = Interactions(info)
        db.session.add(new_interaction)
        db.session.commit()


class Reports(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    entry = db.Column(db.String(30))

    def __init__(self, info):
        self.entry = json.dumps(info)

    @staticmethod
    def create_report(info):
        new_report = Reports(info)
        db.session.add(new_report)
        db.session.commit()
        return {
            'status': 200
        }

    @staticmethod
    def fetch_most_recent_report(report_id):
        row = Reports.query.filter_by(report_id=report_id).order_by('created_at desc').first()
        data = {str(row)}
        return {
            'status': 200,
            'data': data
        }

    @staticmethod
    def fetch_reports(report_id):
        rows = Reports.query.filter_by(report_id=report_id).order_by('created_at desc').all()
        data = [{str(row)} for row in rows]
        return {
            'status': 200,
            'data': data
        }

    @staticmethod
    def update_report(report_id):
        row = Reports.query.filter_by(report_id=report_id).order_by('created_at desc').first()
        if not row:
            return {
                'status': 200,
                'message': 'No existing entry with that report id'
            }
        return {
            'status': 200,
        }

