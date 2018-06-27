Code Academy Summer 2018 - Code Labs
====================================

Downloading the Code Labs
-------------------------

Run the following command in your computer's Terminal to download the code repository:

```bash
git clone https://github.com/bwhite000/Code-Labs-Summer-2018.git
```

Then, navigate into the code folder:

```bash
cd Code-Labs-Summer-2018
```

> **Pro-tip:** Hit the `tab` key in your Terminal after typing the first few letters to auto-complete the directory name.

Running a Python Script
-----------------------

To run a script from this repository, navigate into the directory of the script, then run the `python` command on the file.

```bash
# Navigate into the directory.
cd dice_roller

# Run the script with Python 3.
python3 final.py
```

Updating your Raspberry Pi
--------------------------

### Software update

In the Terminal, fetch the latest package update details:

```bash
sudo apt-get update
```

Perform the update to the packages:

```bash
sudo apt-get dist-upgrade
```

Sometimes you may need to reboot, this doesn't happen everytime. If you need to reboot to apply the updates, type:

```bash
sudo reboot
```

### Firmware update

The Raspberry Pi also occasionally has updates to the firmware that allows the various hardware pieces to speak with the Operating System. To update the firmware, type the command:

```bash
rpi-update
```
