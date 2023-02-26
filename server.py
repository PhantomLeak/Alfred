from flask import Flask, request, render_template
from src import alfred as alfred
import os

template_dir = os.path.abspath('templates')

app = Flask(__name__, template_folder=template_dir)

@app.route('/', methods=["GET", "POST"])
def main():
    processed_text = ''

    if request.method == "POST":
        text = request.form['commandRequest']
        processed_text = alfred.alfred_main(text)
    
    return render_template('index.html', return_value=processed_text)
# Running app
if __name__ == '__main__':
    app.run(debug=True)
