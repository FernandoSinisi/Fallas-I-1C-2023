from flask import Flask, jsonify, request

from flask_cors import CORS

from constants.general_constants import QUESTIONS_ROUTE

from services.engine import HyperthyroidismKnowledgeEngine

from services.question_loader import load_questions

from constants.diagnostic_constants import (NEGATIVE_DIAGNOSIS, DIAGNOSTIC_TEXTS)

import datetime

app = Flask("")

CORS(app,  resources={r"/*": {"origins": "*"}})

questions = load_questions(QUESTIONS_ROUTE)


@app.route('/diagnostic',
           methods=['POST'])
def answer_unanswered():
    answers = request.get_json()

    diagnostic, current_tag = HyperthyroidismKnowledgeEngine(answers).get_diagnosis()

    print(f"{str(datetime.datetime.now())} - {diagnostic}")

    response = {
        "questions": questions,

        "next_tag": current_tag,

        "diagnostic": DIAGNOSTIC_TEXTS.get(diagnostic, NEGATIVE_DIAGNOSIS)
    }

    return jsonify(response)
