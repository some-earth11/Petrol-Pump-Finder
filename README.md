# Petrol Pump Finder

A python based Selenium application which helps users to find directions to the nearest Petrol Pump via a Tkinter GUI.  

User can Find the nearest Petrol Pump with a click of a button!

## Usage

```python
import time
from selenium import webdriver

# Setting up Web Driver
driver = webdriver.Chrome(r"path_to_driver")
```
```python
import tkinter as tk
from tkinter import *
from tkinter import messagebox, filedialog

def navigate():
    # Import Functions from main.py
    import main
```
## Screenshots
### Interface
![Petrol Pump Finder GUI](https://github.com/some-earth11/Petrol-Pump-Finder/blob/main/Screenshots/ss1.jpg)
### Successful Run
![Petrol Pump Finder GUI](https://github.com/some-earth11/Petrol-Pump-Finder/blob/main/Screenshots/ss2.jpg)  
Petrol Pump Emoji Icon by [Vincent Le Moign](https://iconscout.com/contributors/vincent-le-moign)
## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)