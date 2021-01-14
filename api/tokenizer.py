import json

from flask import Response

from config import *
from error.CommunicationError import CommunicationError
from service.RequestService import RequestService
from service.TokenizerService import TokenizeService


def create(input):
    service = TokenizeService()
    req = RequestService()

    # not quire good technic
    data = {"textData": input['text']}
    d = json.dumps(data)

    try:
        resp = req.postJSONRequest(API_URL + API_URL_SPLITTER, d)
    except CommunicationError as e:
        return Response(response=json.dumps({'error': e.message}), status=e.status_code,
                        mimetype="application/json")

    d = json.loads(resp)
    split_sentece = service.split(d['data'])
    j = json.dumps({"data": split_sentece})

    try:
        nerData = req.postJSONRequest(API_URL + API_URL_NER_PIPELINE, j)
    except CommunicationError as e:
        return Response(response=json.dumps({'error': e.message}), status=e.status_code,
                        mimetype="application/json")

    return json.loads(nerData)


def get():
    return Response(response=json.dumps({'message': "Hello there"}), status=200,
                    mimetype="application/json")
