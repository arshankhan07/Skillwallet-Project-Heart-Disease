from flask import Flask, render_template

app = Flask(__name__)

# ──────────────────────────────────────────────
#  TABLEAU EMBED CONFIG
#  Use the base URL only — no query params needed
# ──────────────────────────────────────────────
TABLEAU = {
    "dashboard1": {
        "name": "Heart Disease Dashboard 1",
        "url": "https://public.tableau.com/views/HeartDisease_Dashboard1/Dashboard1",
        "description": "Interactive analysis of heart disease indicators and risk factors.",
        "icon": "❤️"
    },
    "dashboard2": {
        "name": "Heart Disease Dashboard 2",
        "url": "https://public.tableau.com/views/HeartDisease_Dashboard1/Dashboard2",   # ← replace
        "description": "Deep-dive metrics and comparative analysis across patient groups.",
        "icon": "🫀"
    },
    "story": {
        "name": "Heart Disease Story",
        "url": "https://public.tableau.com/views/HeartDisease_Story/Story1",        # ← replace
        "description": "A guided narrative walkthrough of key heart disease insights.",
        "icon": "📖"
    }
}

@app.route("/")
def home():
    return render_template("home.html", tableau=TABLEAU)

@app.route("/dashboards")
def dashboards():
    return render_template("dashboards.html",
                           d1=TABLEAU["dashboard1"],
                           d2=TABLEAU["dashboard2"])

@app.route("/story")
def story():
    return render_template("story.html", story=TABLEAU["story"])

if __name__ == "__main__":
    app.run(debug=True, port=5000)
