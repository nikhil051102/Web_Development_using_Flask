from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/about')
def nikhil_function():
    return render_template('about.html')

@app.route('/nikhil')
def nikhil_function2():
    name = "Nikhil Deore"
    return render_template('name.html', nikhil = name)


app.run(debug=True)  #This will automatically detect change and reload it.

if __name__ == '__main__':
    app.run()