from flask import Blueprint, send_from_directory

static_bp = Blueprint('static', __name__)

@static_bp.route('/<path:path>')
def api_root(path):
    return send_from_directory('static', path)
