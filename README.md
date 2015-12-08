# tagbar
Instagram scraper and photo analyzer.

tagbar is a Flask-based webapp where anyone can search for colors representative of any item that has ever been uploaded to Instagram. tagbar will download and analyze recent photos and return a set of colors representative of the provided hashtag, according to Google's material design principles.

##### To run the program
 - Ensure all packages are installed
 - Project needs 2 files not tracked in git.
  - in the root directory, `config.py` needs
  ```
  WTF_CSRF_ENABLED = True
  SECRET_KEY = <add your secret key>
  ```
  - in the app directory, create `settings.ini` and add instagram api info
  ```
  [Instagram]
  client_id= <your client id>
  client_secret= <your secret key>
  ```

###### Without Heroku:
  From the project root folder, `./run.py`

###### With Heroku:
  `heroku local`

```
$ pip install -r requirements.txt
```


Project structure is based on Miguel Grinberg's [Flask Tutorial](http://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world)

## v0.3 (in progress)
Major project restructure. Need to include a local settings file to read IG keys, as Heroku has problems with environment variables.

#### v0.2
Status:
 - Program can download, combine, and analyze multiple photos, but colors turn out better for single photo
 - Render top 5 colors on screen

Next:
 - site UI enhancements

#### v0.1
Status: Program downloads photos from Instagram according to provided hashtag.

Next: Create photo analyzer file
