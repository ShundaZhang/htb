from flask import Flask, redirect

app = Flask(__name__)

index = 0

@app.route('/old')
def old_route():
    global index
    index += 1

    # Redirect to a different URL
    if index == 1:
        return redirect("http://www.google.com", code=302)
    else:
        return redirect("http://127.0.0.1:1337/secret", code=302)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)

