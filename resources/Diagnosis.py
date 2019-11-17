from flask import jsonify, request
from flask_restful import Resource
from Model import db, Diagnosis, DiagnosisSchema

# create the schemas
diagnose_many_schema = DiagnosisSchema(many=True)
diagnosis_schema = DiagnosisSchema()


class DiagnosisResource(Resource):
    def get(self):
        """
        Handles get requests
        """
        # get all diagnosis from the db
        diagnosis = Diagnosis.query.all()
        diagnosis = diagnose_many_schema.dump(diagnosis).data

        return {"status": "success", "data": diagnosis}, 200

    def post(self):
        """
        Handles post requests
        """
        json_data = request.get_json(force=True)

        # if request body is empty
        if not json_data:
            return {'message': 'No input data provided'}, 400

        data, errors = diagnosis_schema.load(json_data)

        # if error loading the data
        if errors:
            return {"status": "error", "data": errors}, 422

        diagnosis = Diagnosis(
            category_code=data['category_code'],
            diagnosis_code=data['diagnosis_code'],
            full_code=data['full_code'],
            abbreviated_description=data['abbreviated_description'],
            full_description=data['full_description'],
            category_title=data['category_title']
        )

        db.session.add(diagnosis)
        db.session.commit()

        result = diagnosis_schema.dump(diagnosis).data

        return {'status': "success", 'data': result}, 201

    def put(self):
        """
        Handles put requests
        """
        json_data = request.get_json(force=True)

        # if request body is empty
        if not json_data:
            return {'message': 'No input data provided'}, 400

        data, errors = diagnosis_schema.load(json_data)

        # if error loading the data
        if errors:
            return errors, 422
        print("******", data)
        diagnosis = Diagnosis.query.filter_by(id=data['id']).first()

        if not diagnosis:
            return {'message': 'diagnosis does not exist'}, 400

        diagnosis.category_code = data['category_code'],
        diagnosis.diagnosis_code = data['diagnosis_code']
        diagnosis.full_code = data['full_code']
        diagnosis.abbreviated_description = data['abbreviated_description']
        diagnosis.full_description = data['full_description']
        diagnosis.category_title = data['category_title']

        db.session.commit()

        result = diagnosis_schema.dump(diagnosis).data

        return {"status": 'success', 'data': result}, 200

    def delete(self):
        """
        Handles delete requests
        """
        json_data = request.get_json(force=True)
        if not json_data:
            return {'message': 'No input data provided'}, 400

        data, errors = diagnosis_schema.load(json_data)

        if errors:
            return errors, 422

        diagnosis = Diagnosis.query.filter_by(id=data['id']).delete()
        db.session.commit()

        result = diagnosis_schema.dump(diagnosis).data

        return {"status": 'success', 'data': result}, 204
