# Dash app for ESP32-GPSRTK2 rover





## Dev get started (VScode)

### Local Dash app setup

1. right click on project root folder > select **open in terminal**
2. `python -m venv .venv` to setup python virtual environment for this project. TIP: copy from here and right click in terminal to paste-and-execute.
3. Dialog should come up asking you want this env as interpreter for project: answer yes.
4. If no to (3) on blue ribbon at bottom of VSCODE, on left click on interpreter, chose the **venv** one you just created.
5. Might get some bits and both e.g. 'install pylint' etc. click install for them.
6. `pip install -r requirements.txt` to install packages
7. `pip install -e .` to make editable
8. Run `./dash_app/index.py` to run with **dev server**. (Running `./production.py` runs using `gunicorn` in production environment)

#### Dependancies/ packages

Use `pip-chill` to freeze requirements file, rather than `pip freeze` and delete `dash_app` line that's created.

``` bash
pip-chill > requirements.txt
```

### Mosquitto MQTT broker server

MQTT messaging used to communicate between Dash app and the rover (on same wifi network). You need to install Mosquitto to act as a broker (separate process to Dash app server).
I have developed on Windows machine, so instructions need to be adjusted for Linux:

1. Could not Mosquitto v2 working with Websockets MQTT (which Dash app uses), so using v1.6.9 [(d/l here)](https://mosquitto.org/files/binary/win64/mosquitto-1.6.9-install-windows-x64.exe). Installed in standard location at `c:\program files\mosquitto` 
2. Running `start_broker.bat` from cmd line in VSCode will start broker, using `mosquitto.conf` config file included. Alternatively use `runme.py` to start broker and dash app.

``` bash
./start_broker.bat
```
3. You'll need to modify `config.toml`,`start_broker.bat` and/or  `mosquitto.conf` if anything changed, eg:
 - (Websockets) ports need to match. Default port set to 8083.
 - Install location for Mosquitto not as above default.
 - You may need to fiddle with Firewall/ Anti-virus software to permit connections.

### Configuration file ('config.toml')

Config file for Dash app (based on my WIP template). Self explanatory, mostly.
