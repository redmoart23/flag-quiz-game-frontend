from flask import Flask, jsonify
from modules.get_all_flags import get_all_flags

from random import choice, sample, shuffle

app = Flask(__name__)

countries, continents = get_all_flags()

@app.get('/api/v1/flags')
def get_all_flags_route():
    return jsonify({'continents': continents, 'countries': countries})


@app.get('/api/v1/flags/question')
def get_question_route():
    correct_answer = choice(countries[choice(continents)])
    response_choices = sample(countries[choice(continents)], 3) + [correct_answer]

    shuffle(response_choices)

    return jsonify({'question': correct_answer, 'response_choices': response_choices})



if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
