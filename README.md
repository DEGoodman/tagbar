# tagbar
Instagram scraper and photo analyzer.

tagbar will be a webapp where anyone can search for colors representative of any item that has ever been uploaded to Instagram. tagbar will download and analyze recent photos and return a set of colors representative of the provided hashtag, according to good design principles.

## v0.2
Status:
 - Program can download, combine, and analyze multiple photos, but colors turn out better for single photo
 - Render top 5 colors on screen

Next:
 - site UI enhancements

#### v0.1
Status: Program downloads photos from Instagram according to provided hashtag.

Next: Create photo analyzer file


##### To run the Program
 - Ensure all packages are installed
 - Pillow can be a pain to install, and is one of the core ackages for this app. See here:[Pillow Installation](https://pillow.readthedocs.org/en/3.0.x/installation.html)

```
$ pip install -r requirements.txt
$ python main.py <hashtag>
```
