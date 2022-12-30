from flask import request, abort
from app import app
from controller import *


@app.route('/<slug>')
def short_link_slug(slug):
    return get_single_short_link(slug)


@app.route('/shortlinks', methods=['GET', 'POST'])
def short_links():
    if request.method == 'GET':
        return get_all_short_links()
    else:
        return add_new_short_link(request.json)


@app.route('/shortlinks/<slug>', methods=['PUT'])
def update_slug(slug):
    return update_short_link_by_slug(slug, request.json)


@app.errorhandler(500)
def bad_request(e):
    return jsonify({}), 500


@app.errorhandler(400)
def bad_request(e):
    response = {
        "status": "failed",
        "message": "Bad Request"
    }
    return jsonify(response), 400


@app.errorhandler(404)
@app.errorhandler(405)
def page_not_found(e):
    response = {
        "status": "failed",
        "message": "not found"
    }
    return jsonify(response), 404
