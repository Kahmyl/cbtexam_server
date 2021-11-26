from main import app

@app.route("/")
@app.route("/home")
def home():
    return "Welcome Home"