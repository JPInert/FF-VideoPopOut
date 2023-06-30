 <h1>VideoPopOut</h1>

  <p>The VideoPopOut script allows you to map the middle mouse button to the keyboard keys Ctrl+Shift+] to automatically pop a video in Firefox out of the tab, creating a borderless, moveable, and scalable video window that always stays on top regardless of the active tab.</p>

  <h2>VideoPopOut.py</h2>
  <p>The `VideoPopOut.py` script can be run directly using Python. It provides the functionality to pop out videos in Firefox by mapping the middle mouse button to Ctrl+Shift+].</p>

  <h3>Requirements</h3>
  <ul>
    <li>Python 3.x</li>
    <li>Firefox browser</li>
    <li>pip package: pynput</li>
  </ul>

  <h3>Usage</h3>
  <ol>
    <li>Install Python from the official website: <a href="https://www.python.org">https://www.python.org</a></li>
    <li>Install the required package using pip: <code>pip install pynput</code></li>
    <li>Run the script: <code>python VideoPopOut.py</code></li>
  </ol>

  <h2>VideoPopOut_win.py</h2>
  <p>The `VideoPopOut_win.py` script is designed to be converted into an executable using a tool like PyInstaller. It provides the same functionality as `VideoPopOut.py`, but also creates an icon in the system tray with right-click exit functionality.</p>

  <h3>Requirements</h3>
  <ul>
    <li>Python 3.x</li>
    <li>Firefox browser</li>
    <li>pip package: pynput</li>
    <li>PyInstaller (to compile into an executable)</li>
  </ul>

  <h3>Usage</h3>
  <ol>
    <li>Install Python from the official website: <a href="https://www.python.org">https://www.python.org</a></li>
    <li>Install the required packages using pip: <code>pip install pynput</code></li>
    <li>Install PyInstaller: <code>pip install pyinstaller</code></li>
    <li>Compile the script into an executable: <code>pyinstaller --noconsole --icon=icon.ico --onefile VideoPopOut_win.py</code></li>
    <li>Run the compiled executable: <code>./dist/VideoPopOut_win.exe</code></li>
  </ol>

  <h2>Notes</h2>
  <p>Refer to the included `notes.txt` file for additional information and troubleshooting tips.</p>