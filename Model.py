from flask import Flask
from marshmallow import Schema, fields, pre_load, validate
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy


ma = Marshmallow()
db = SQLAlchemy()


class Diagnosis(db.Model):
    """
    Creates the diagnosis model
    """
    __tablename__ = 'diagnosis'
    id = db.Column(db.Integer, primary_key=True)
    category_code = db.Column(db.String(50), nullable=False)
    diagnosis_code = db.Column(db.String(50), nullable=False)
    # the full code is empty
    full_code = db.Column(db.String(50), unique=True, nullable=False)
    abbreviated_description = db.Column(db.String(250), nullable=False)
    full_description = db.Column(db.String(500), nullable=False)
    category_title = db.Column(db.String(500), nullable=False)
    # the date this record was created
    creation_date = db.Column(
        db.TIMESTAMP, server_default=db.func.current_timestamp(), nullable=False)

    def __init__(self, category_code, diagnosis_code, full_code, abbreviated_description, full_description, category_title):
        self.category_code = category_code
        self.diagnosis_code = diagnosis_code
        self.full_code = full_code
        self.abbreviated_description = abbreviated_description
        self.full_description = full_description
        self.category_title = category_title


class DiagnosisSchema(ma.Schema):
    """
    Creates the diagnosis schema
    """
    id = fields.Integer()
    category_code = fields.String(required=True, validate=validate.Length(1))
    diagnosis_code = fields.String(required=True, validate=validate.Length(1))
    full_code = fields.String(required=True, validate=validate.Length(1))
    abbreviated_description = fields.String(
        required=True, validate=validate.Length(1))
    full_description = fields.String(
        required=True, validate=validate.Length(1))
    category_title = fields.String(required=True, validate=validate.Length(1))
    creation_date = fields.DateTime()
