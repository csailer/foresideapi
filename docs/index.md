# Install

These steps where only tested on MacOS. They were not tested on Windows. 

 - Unzip the provided project zip file.
 - CD into the directory where the project zip file was extracted.
 - Create a Virtual Environment for the API (see [mkvirtualenv](https://virtualenvwrapper.readthedocs.io/en/latest/command_ref.html) for details)
    - ```python
        mkvirtualenv foreside
       ```
 - Make sure you are running in the Virtual Environment:
    ```
    workon foreside
    ``` 
 - From the terminal, and while in the forside virtual environment, Execute:
  ``` 
    . install.sh
  ```
   Note: You may have to make this file executable before it will execute.
    
    
 