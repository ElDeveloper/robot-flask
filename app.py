from flask import Flask, render_template

app = Flask(__name__)



@app.route('/go/<feet>')
def home(feet):
    return render_template('minimal_template.html',
                           repetitions=range(int(feet)))

@app.route('/square/<feet>')
def square(feet):
    return render_template('square.html', repetitions=range(int(feet)))

if __name__ == "__main__":
    app.run(debug=True)
