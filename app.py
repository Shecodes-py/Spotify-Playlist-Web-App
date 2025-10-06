from flask import Flask, render_template
import json
import os

app = Flask(__name__)

@app.route('/')
def home():
    name = "Zainab Adebayo Temidun"
    playlist_url = "https://open.spotify.com/playlist/0sNfSkRkYaVQCwRYkAZZjG?si=e59954fc17dc4136"
    with open('data.json', 'r') as f:
        songs = json.load(f)

    return render_template('index.html', name=name, playlist_url=playlist_url, songs=songs)

@app.route("/letter")
def letter():
    return render_template('letter.html')

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
