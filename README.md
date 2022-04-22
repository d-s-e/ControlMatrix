# ControlMatrix

## About:

This is an application to control various outputs from different inputs.
The goal is to create a matrix, where one can connect arbitrary control inputs
with arbitrary sinks in a modular way.

### Currently supported:

- Twitch Chat (Input)
- MIDI (Input), tested with a Korg nanoPad2 controller
- DMX (Output), tested with an Enttec DMX USB Pro interface

### Ideas for additional channels:

- Streamdeck
- OBS Studio
- Matrix
- ...

The features are tailored primarily on my equipment and usage, but it should be easy
to adapt them to your own needs. More features like better modularization and
extensions are a work in progress ... 

## How to run:

1. Install the requirements (in some kind of virtual environment).

        pip install -r requirements.txt

    To use the StreamDeck, a LibUSB HIDAPI Backend is also needed.

2. Add your settings to the file _config.py_ in the folder _control_matrix_. 
   You can use the _config.example.py_ as a template.
3. Start the application with:

        python ./main.py


