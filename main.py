from flask import Flask, request, render_template
import werkzeug


app = Flask(__name__)


@app.route('/')
def home():
    return render_template(r'index.html')

@app.route('/destinations')
def destinations():
    return render_template(r'destinations.html')


if __name__ == "__main__":
    app.run(debug=True)
