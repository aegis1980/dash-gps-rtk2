from dash_app.index import app
from subprocess import Popen
import os

cwd = os.getcwd()


# ref to Dash app underlying flask server. 
server = app.server 

if __name__ == "__main__": 

    # batch command to (re)start MQTT broker
    p = Popen("start_broker.bat", cwd=cwd)
    stdout, stderr = p.communicate()



    # Runs dash app (non production)
    app.run_server(debug=True, host='0.0.0.0', port=8050)