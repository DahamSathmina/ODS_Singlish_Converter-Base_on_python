from flask import Flask, render_template
import { SpeedInsights } from "@vercel/speed-insights/next"

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

# No app.run() needed for Vercel serverless functions
