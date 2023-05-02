from flask import Flask, render_template, request
import json
from dbOperations import insertIntentsData

app = Flask(__name__)

@app.route('/aibot')
def home():
    return render_template('home.html')


@app.route('/aibot/train', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Get form data
        tag = request.form['tag']
        patterns = request.form['patterns'].split('\n')
        responses = request.form['responses'].split('\n')
        patterns = [p.strip() for p in patterns]
        responses = [r.strip() for r in responses]
        pat = ', '.join(patterns)
        res = ', '.join(responses)
        data = {
            'tag': tag,
            'patterns': patterns,
            'responses': responses
        }
        json_data = json.dumps(data)

        # Insert data into MySQL database
        insertIntentsData(tag, pat, res, json_data)

        return render_template('home.html')

    return render_template('index.html')

if __name__ == '__main__':
    app.run()



