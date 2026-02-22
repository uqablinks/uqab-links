# uqab-links
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/contact', methods=['POST'])
def contact():
    data = request.get_json()
    name = data.get('name', '')
    email = data.get('email', '')
    message = data.get('message', '')
    # TODO: handle form submission (email/db)
    print(f"Contact: {name} | {email} | {message}")
    return jsonify({'status': 'success', 'message': 'Thank you! We will get back to you soon.'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
