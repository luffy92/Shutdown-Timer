# Auto Sleep/Shutdown Timer

This is a simple Python application that allows you to schedule an automatic sleep or shutdown of your Windows computer. You can set the timer in hours and minutes, choose the action (sleep or shutdown), and see a countdown. The countdown will turn red and play a sound when there are 10 seconds or less remaining.

## Features

- Set a timer in hours and minutes.
- Choose between shutdown and sleep actions.
- Display a countdown timer.
- Change countdown color to red when less than or equal to 10 seconds.
- Play a sound when less than or equal to 10 seconds.
- Button label changes from "Start" to "Stop" when the timer is running.

## Requirements

- Python 3.x
- Tkinter (comes pre-installed with Python)
- `playsound` package

## Installation

1. Clone the repository:

    ```sh
    git clone https://github.com/yourusername/auto-sleep-shutdown.git
    cd auto-sleep-shutdown
    ```

2. Install the required Python package:

    ```sh
    pip install playsound
    ```

3. Place a sound file named `sound.mp3` in the project directory. This will be the sound played when there are 10 seconds or less left.

4. Convert the script into an executable using PyInstaller:

    ```sh
    pip install pyinstaller
    pyinstaller --onefile --windowed shutdown_timer.py
    ```

    - The `--onefile` flag tells PyInstaller to bundle everything into a single executable file.
    - The `--windowed` flag prevents a console window from appearing when you run the GUI application.

5. Move the `sound.mp3` file into the same directory as the generated executable (found in the `dist` directory). This ensures that the sound file is accessible when the application runs.

## Usage

Run the script using Python:

```sh
python shutdown_timer.py



### Explanation

- **Installation**: Provides instructions on how to clone the repository and install the required Python package.
- **Usage**: Shows how to run the script.
- **Converting to Executable**: Provides specific commands to install PyInstaller and convert the script into an executable, including moving the sound file to the same directory as the executable.
- **Notes**: Mentions the platform specificity and permissions.
- **License**: Specifies the licensing (you can change this according to your project’s license).

This version of the `README.md` includes all necessary commands and instructions to use and package the script into an executable.