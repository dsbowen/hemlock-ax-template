"""Create the application.
"""
from hemlock import create_app
from hemlock.app import socketio
from hemlock_ax import init_app

import src

app = create_app()
init_app(app)

if app.config["ENV"] == "production":
    # Don't allow users to restart and block duplicate IP addresses in production
    app.config.update(ALLOW_USERS_TO_RESTART=False, BLOCK_DUPLICATE_KEYS=["ipv4"])

if __name__ == "__main__":
    socketio.run(app, debug=True)
