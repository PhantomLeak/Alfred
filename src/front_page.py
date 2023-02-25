from flask import Flask, request, render_template
import alfred as alfred
import os

template_dir = os.path.abspath('../templates')
app = Flask(__name__, template_folder=template_dir)

@app.route("/")

def hello_world():
    return render_template('index.html')

# This will return what has been written inside of the text block
@app.route('/', methods=['POST'])
def my_form_post():
    text = request.form['text']
    processed_text = alfred.alfred_main(text)
    return processed_text