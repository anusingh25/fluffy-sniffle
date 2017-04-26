import sys
import json
from flask import Flask
from flask import request
from flask import current_app
from flask import render_template
from flask import send_from_directory
import pyHS100

class WebLight(Flask):
    def __init__(self, *args, **kwargs):
        # Call the superclass
        super(WebLight, self).__init__(*args, **kwargs)

        # Following two lines are used for debugging
        self.config.update(TEMPLATES_AUTO_RELOAD=True)
        self.debug = True

        # Register our routes
        self.route("/")(self.page_index)
        self.route("/static/<path:path>")(self.serve_static)
        self.route("/api/state", methods=['POST','GET'])(self.api_state)

    def serve_static(self, path):
        """
        Serves static files from the 'static' folder within the python package
        """
        return send_from_directory('static', path)

    def page_index(self):
        """
        Gets the index page
        """
        return self.serve_static('index.html')

    def api_state(self):
        plug = pyHS100.SmartPlug("192.168.0.109")
        if request.method == 'POST':
            # POST requests are for setting the light state
            light_state_actions = {True: plug.turn_on, False: plug.turn_off}
            light_state = request.form.get('light_state', 'false') == "true"
            light_state_actions[light_state]()
            #set_state_on = 'light_state' in request.form.keys() and request.form.get('light_state', 'false') == "true"
            #if set_state_on:
            #    plug.turn_on()
            #else:
            #    plug.turn_off()
            return ('', 204)
        elif request.method == 'GET':
            # GET requests are for reading the light state
            return_dict = {"light_state": plug.state == "ON"}
            return json.dumps(return_dict)

def main(arg_list):
    try:
        host = arg_list[0]
    except IndexError:
        host = '0.0.0.0'

    try:
        port = arg_list[1]
    except IndexError:
        port = 8000

    app = WebLight("weblight")
    app.run(host=host, port=port)

if __name__ == "__main__":
    main(sys.argv[1:])
