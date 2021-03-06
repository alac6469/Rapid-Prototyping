from flask import Flask
from flask import render_template
app = Flask(__name__)
app.debug = True

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('ResumeLanding.html', name=name)

if __name__ == '__main__':
    app.run()
