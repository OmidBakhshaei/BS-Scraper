# Football Downloader


_Football Downloader_ is a web scraper built with Python which downloads a video file of the highlights of the latest game of a soccer team from an [Iranian website](https://varzesh3.com/).
It comes with a user interface where you can easily write the name of the team and download its last match's highlights.

If you do not have time for a 90 minutes football match but you would like to watch its highlights later in less than 10 minutes **without knowing the result**, You will love _Football Downloader_!

![User Interface](https://github.com/OmidBakhshaei/BS-Scraper/blob/master/img/UI.jpg?raw=true)

---
## Usage
1. make sure the following Python packages are installed:

    - Pyqt5
    ```
    pip install Pyqt5
    ```
    
    - urllib.request
    ```
    pip install urllib.request
    ```
    
    - bs4
    ```
    pip install bs4
    ```

2. Run the code in your editor.

3. Write the name of the team in the UI. 
4. push the **دانلود** button. 


by following the four steps a folder named **Varzesh3** would be created on your desktop and after a few moments you can find the downloaded video file(with the same name of the selected team) in the mentioned folder.

![Varzesh3](https://github.com/OmidBakhshaei/BS-Scraper/blob/master/img/DL.jpg?raw=true)

---
### About Football Downloader
Football downloader is an exercise in making an scraper using beautifulsoup. The UI was added to the original code which you can find in the same repository.

<p align="center">
  <img src="https://github.com/OmidBakhshaei/BS-Scraper/blob/master/img/Module_Football_downloader.jpg" alt="Original code" width="800">
</p>
