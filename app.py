from flask import Flask, render_template, request
import model

app = Flask(__name__)

@app.route('/')
def home():
    titles = model.game_titles()
    return render_template('home.html', titles=titles)

@app.route('/output', methods=["POST", "GET"])
def output():
    game = request.args.get('game')

    print(game)

    recommendation = model.recommend(game)

    return render_template('output.html', result=recommendation)

if __name__ == '__main__':
    app.run()