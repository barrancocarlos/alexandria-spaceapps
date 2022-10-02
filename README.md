# Alexandria. Space Apps Challenge 2022

![Alt Text](https://github.com/barrancocarlos/nebula-spaceapps/blob/main/static/assets/img/theme/python.jpg)

Alexandria is an artificial intelligence app that will improve the accessibility and discoverability of records in the public NASA Technical Report Server. Alexandria can read and summarize documents, generate text analytic data, and produce a list of topic keywords to help researchers find the information they need. 

_App screen capture_

![Alt Text](https://github.com/barrancocarlos/alexandria-spaceapps/blob/main/static/assets/images/theme/home.png)

_Youtube Presentation_

[![Alt Text](https://github.com/barrancocarlos/alexandria-spaceapps/blob/main/static/assets/images/theme/youtube.png)](https://www.youtube.com/watch?v=GwhijugkqIo&ab_channel=CarlosBarranco)

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

Make sure you have installed all of the following prerequisites on your development machine:

* Git - [Download & Install. Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
* Python - [Download & Install Python](https://www.python.org/downloads/) and the pip package manager.

### Installing

```bash
# Clone this repository
$ git clone https://github.com/barrancocarlos/alexandria-spaceapps.git

# Go into the repository
$ cd alexandria-spaceapps

# Install dependencies on virtual enviroment
$ pip install pipenv
$ pipenv shell
$ pipenv install

# Run the app
$ python manage.py runserver