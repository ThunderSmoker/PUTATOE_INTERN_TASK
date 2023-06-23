from flask import Flask, jsonify, request, render_template
from db import get_word, update_word

app = Flask(__name__, template_folder='templates')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/word', methods=['GET'])
def get_api_word():
    word = get_word()
    return jsonify({'word': word})

@app.route('/admin', methods=['GET', 'POST'])
def admin():
    if request.method == 'POST':
        new_word = request.form.get('word')
        update_word(new_word)
        return jsonify({'message': 'Word updated successfully'})
    current_word = get_word()
    return render_template('admin.html', current_word=current_word)

if __name__ == '__main__':
    app.run(debug=True)
