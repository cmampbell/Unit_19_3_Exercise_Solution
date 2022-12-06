from flask import Flask, request, render_template, redirect, flash, jsonify
from flask_debugtoolbar import DebugToolbarExtension
from surveys import satisfaction_survey

app = Flask(__name__)

app.config['SECRET_KEY'] = 'poopybutthole'
debug = DebugToolbarExtension(app)

responses = []

@app.route('/')
def show_home_page():
    return render_template('survey_start.html', satisfaction_survey=satisfaction_survey)


@app.route('/questions/<int:q_num>')
def show_question(q_num):
    if len(satisfaction_survey.questions) == len(responses):
        return redirect('/thank-you')

    elif q_num >= len(satisfaction_survey.questions):
        flash('You are trying to access and invalid question')
        return redirect(f'/questions/{len(responses)}')
        
    else:
        question = satisfaction_survey.questions[q_num]
        return render_template('question.html', question=question, q_num=q_num)

@app.route('/answer', methods=['POST'])
def handle_answer():
    responses.append(request.form['answer'])
    if len(satisfaction_survey.questions) == len(responses):
        return redirect('/thank-you')
    else:
        return redirect(f'/questions/{len(responses)}')

@app.route('/thank-you')
def show_thank_you():

    return render_template('thank_you.html')