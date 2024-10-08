from flask import Flask, render_template
import business as bus
 

app = Flask(__name__)


@app.route("/")
def home():
    
    data = "hello world"
    
    render_template('index.html',data=data)
    return data


if __name__=='__main__':
    app.run(
        debug=True
    )