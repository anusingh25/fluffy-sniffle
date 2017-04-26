# fluffy-sniffle
A web interface for changing the power state of a TPLink HS105 smart plug

## Background and inpiration
This project is inspired by people who have made their christmas lights controllable via web interfaces, and viewable via webcam. Connecting a web interface to the API for the smart plug is effectively the same. Since this all just reinvents the wheel, this is meant to be more of a learning project than anything else. Learning/experience goals are as follows:
- More react experience (use [component state](https://facebook.github.io/react/docs/state-and-lifecycle.html))
- Build experience with [declarative programming](https://www.youtube.com/watch?v=yGh0bjzj4IQ)
- Better unit test development (properly mock objects!)

## Getting started
It's all pretty simple at the moment:

```
virtualenv venv
source venv/bin/activate
pip install Flask pyHS100
python app.py
```
