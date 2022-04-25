import os
import webbrowser
import urllib.request
from bs4 import BeautifulSoup
from urllib.parse import quote


def game_s_link(team):
    """Return the link that contains the game which the user is looking for.
            
    Args:
        team (str): The team which the user wants to download its game

    Returns:
        str: the link which contains the video of the game
    """
    # sends request and reads the html
    html = urllib.request.urlopen(url)
    # parses the html
    soup = BeautifulSoup(html)
    # returns a list of all links in the html tagged with href
    for a in soup.find_all('a', href=True):
        # finds the link which is dedicated to the selected team's last game
        if team in a['href'] and "خلاصه" in a['href']:
            new_url = url+a['href']
            return new_url


def IRI_to_Ascii(link):
    """Convert a URL containing non-ascii characters(IRI) to a plain ASCII.
    
    Args:
        link (str): link to convert
        
    Returns:
        str: ASCII link
    """
    iri = quote(link.split("/")[-1])
    url_without_iri = link.split("/")[:-1]
    converted_url = "/".join(url_without_iri) + "/" + iri
    return converted_url


def download_link():
    """Extract and return the download's url from the game's url."""
    # sends request and reads the html
    html = urllib.request.urlopen(IRI_to_Ascii(game_s_link(team)))
    # parses the html
    soup = BeautifulSoup(html)
    # returns a list of all links in the html tagged with href
    for a in soup.find_all('a', href=True):
        # finds the video file's url
        if ".mp4" in a['href']:
            video_url = a['href']
    return video_url


def download_video():
    """Create a folder on user's desktop named "Varzesh3" 
    and save the video in the created folder.
    """
    desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
    newpath = os.path.join(desktop, "Varzesh3")
    if not os.path.exists(newpath):
        os.makedirs(newpath)
    filename_and_path = os.path.join(newpath, f"{team}.mp4")
    # urllib.request.urlretrieve(download_link(), filename_and_path)


url = "https://video.varzesh3.com"
team = "لیورپول"


download_video()
