from flask import Flask, render_template, send_from_directory

app = Flask(__name__, 
    static_url_path='/static',
    static_folder='static')

@app.route('/static/site.webmanifest')
def manifest():
    return send_from_directory('static', 'site.webmanifest', mimetype='application/manifest+json')

@app.route('/')
def index():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)