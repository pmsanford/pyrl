# pyrl
Python Roguelike-in-progress. Currently based on TDL, but with an eye to supporting modular engines.

# Default Keybindings
Vi keys or arrow keys for movement. `a` will prompt you for a direction to attack in, or you can move into a monster. `q` quits. See the [keybindings.json](gamedata/keybindings.json) file for more.

# Running
First, run
```
git clone https://github.com/pmsanford/pyrl.git
```
Then move into the newly created pyrl directory and create a virtualenv with:
```
virtualenv --python=python3 venv
```
then, if you are on OSX/Linux: `source venv/bin/activate`

or Windows: `venv\Scripts\activate`

Finally, run
```
pip install -r requirements.txt
```
to install prerequisites. Then you can `python run.py`
