# Template for a Bootstrap Dash app



## Get started (VScode) 

1. right click on project root folder > select **open in terminal**
2. `python -m venv .venv` to setup python virtual environment for this project. TIP: copy from here and right click in terminal to paste-and-execute.
3. Dialog should come up asking you want this env as interpreter for project: answer yes.
4. If no to (3) on blue ribbon at bottom of VSCODE, on left click on interpreter, chose the **venv** one you just created.
5. Might get some bits and both e.g. 'install pylint' etc. click install for them.
6. `pip install -r requirements.txt` to install packages
7. `pip install -e .` to make editable
8. Run `./dash_app/index.py` to run with **dev server**. (Running `./production.py` runs using `gunicorn` in production environment)

## Dependancies/ packages

Use `pip-chill` to freeze requirements file, rather than `pip freeze` and delete `dash_app` line that's created.

``` bash
pip-chill > requirements.txt
```

## Configuration



## Deployment


#### LFS

Uses this [Heroku buildpack](https://github.com/radian-software/heroku-buildpack-git-lfs) for LFS.

