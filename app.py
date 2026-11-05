import os
import subprocess
from flask import Flask, render_template, request, jsonify
import target

app = Flask(__name__)

# Get current git commit SHA
def get_commit_sha():
    if os.getenv("RENDER_GIT_COMMIT"):
        return os.getenv("RENDER_GIT_COMMIT")
    try:
        sha = subprocess.check_output(["git", "rev-parse", "HEAD"]).decode("utf-8").strip()
        return sha
    except Exception:
        return "development-sha"

@app.route("/")
def index():
    commit_sha = get_commit_sha()
    return render_template("index.html", commit_sha=commit_sha)

@app.route("/health")
def health():
    return jsonify({
        "status": "healthy",
        "commit_sha": get_commit_sha()
    })

@app.route("/api/run", methods=["POST"])
def run_function():
    data = request.json or {}
    func_name = data.get("function")
    args = data.get("args", [])

    try:
        func = getattr(target, func_name)
        # Convert argument types as appropriate for python function testing
        result = func(*args)
        return jsonify({"success": True, "result": result})
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 400

if __name__ == "__main__":
    app.run(debug=True, port=5000)