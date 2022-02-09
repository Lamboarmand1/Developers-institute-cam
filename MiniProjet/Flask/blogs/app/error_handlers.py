from app import app as appli
from flask import render_template

@appli.errorhandler(404)
def error_404(error):
    return render_template('errors/404_error.html'), 404