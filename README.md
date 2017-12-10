
# LEO Lookup to Flashcards

This is a web app which allows you to look up a word in the [LEO online dictionary](https://dict.leo.org/franz%C3%B6sisch-deutsch/) and save it to a Google Form, so you can review it later.


## Configuration

Leocards looks for configuration details in a number of environment variables:

| Environment variable | Example value | Description |
|----------------------|---------------|-------------|
| LEOCARDS_PORT        | 80            | Port on which Leocards listens for connections |
| LEO_LANG             | französisch-deutsch | LEO language pair                        |
| GF_URL               | https://docs.google.com/forms/.../formResponse | Google Form URL |
| GF_FROM_ID           | entry.12345                                    | Name of the `input` field for the French word |
| GF_TO_ID             | entry.23456                                    | Name of the `input` field for the German word |

You can modify the language pair for your LEO word lookup by changing the `LEO_LANG` variable. If you click on the little flag above the word search box on the LEO front page, your browser will go to a URL for that language pair; e.g. `https://dict.leo.org/französisch-deutsch/`. Copy and paste the part after "dict.leo.org" into your `LEO_LANG` variable.

The URL under `GF_URL` is the submission URL for your Google Form. You can find it as follows. Go to your Google Form and go to Send -> Send via Link. Copy & paste that URL to your browser. You will find that it ends in .../viewform. Replace `viewForm` with `formResponse`. This is the value you need to put into `GF_URL`.

Furthermore, you will need to identify the names of the HTML elements for the input fields of your form. Open the .../viewForm URL for your Google Form and look at the HTML source code for your page (e.g. in Chrome you do View -> Developer -> View Source). Search for `<input type="text"` to find the HTML elements for the words in the two languages. Each of these has a `name` attribute (ignore the `jsname` attributes). These are what you need to put into `GF_FROM_ID` and `GF_TO_ID`.



## Installation

The preferred way to run Leocards is as a Docker container. Use the Dockerfile in this repository to build an image, or simply use the [prebuilt image on Docker Hub](https://hub.docker.com/r/akoller/leocards).

If you have to run Leocards outside of Docker, make sure that you have installed Python 3 and the following modules:

```
pip install lxml flask flask_wtf urllib3 bs4 cherrypy
```

