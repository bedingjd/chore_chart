# chore_chart
simple project to track the kids chores


# First Time Set-up
set up python virtual environment
https://python.land/virtual-environments/virtualenv
  mkdir venv
  python -m venv venv
  // virtualenv venv   (activated virtual environment)
  source venv/bin/activate

First time only:
Installed pre-reqs:
pip install flask
pip install pyyaml
pip install jinja2
pip install markdown

 Other pre-reqs:
- Install emoji fonts
sudo apt install fonts-noto-color-emoji

Others not yet installed:
- Install unclutter to hide mouse: sudo apt-get install unclutter -y

- To turn the screen orientation by 180° enter this on a new line in /boot/config.txt and the screen will turn upside-down after a reboot: lcd_rotate=2

# To Run Each Time (start)
- Open python virtual environment.  From outside `venv` folder:
  - python -m venv venv
  - source venv/bin/activate
- cd into `chore_chart` folder
- ./run_app.sh 
- http://192.168.1.234:5000

# Notes
- New font icons to include in the config.yaml file can be found here: `https://symbolsdb.com/`

# To-Do
- [ ] convert dict to yaml: `https://stackoverflow.com/questions/52762525/convert-python-dictionary-to-yaml`
- [ ] Align the chort chart into a grid with one person per row
- [ ] Adjust the header, or remove the header and add a Chore Chart title
- [ ] Update the `update` button, or allow the entire Card to be a link to update chore status
- [ ] Create a way to re-set the chores the next day (or get them ready for the next week). e.g. update status from 'DONE' to "TOTO'
- [ ] Update the chore status to a python `Enum` or enumeration
- [ ] Add capability to pay-out monies and adjust bank accounts
- [ ] Update this `README` to describe how to set-up the chore chart from scratch
