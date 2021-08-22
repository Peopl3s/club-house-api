# club_house_api

![PyPI](https://img.shields.io/pypi/v/clubhouse_api?color=orange) ![Python 3.6, 3.7, 3.8](https://img.shields.io/pypi/pyversions/clubhouse?color=blueviolet) ![GitHub Pull Requests](https://img.shields.io/github/issues-pr/peopl3s/club-house-api?color=blueviolet) ![License](https://img.shields.io/pypi/l/clubhouse-api?color=blueviolet) ![Forks](https://img.shields.io/github/forks/peopl3s/club-house-api?style=social)

**club_house_api** - this module is a Python client library for The ClubHouse project management platform API (ClubHouse API wrapper)


**Clubhouse** is collaborative project management that streamlines and refines your existing workflow. The intuitive and powerful project management platform loved by software teams of all sizes. [Clubhouse](https://clubhouse.io) is here.


**API documentation** [https://clubhouse.io/api/rest/v3/](https://clubhouse.io/api/rest/v3/)

## Installation

Install the current version with [PyPI](https://pypi.org/project/clubhouse-api/):

```bash
pip install clubhouse_api
```

Or from Github:
```bash
pip install https://github.com/Peopl3s/club-house-api/archive/main.zip
```

## Usage

You can generate a token for clubhouse by going to the account section and generating a new token

```python
TOKEN = os.getenv('TOKEN')

club_house_session = ClubHouse(TOKEN, 'v3')
club_house = club_house_session.get_api()
```

## Example

Create a new Story in the first Project that is returned from the API in the all projects list.

*If you installed a module from PyPi, you should to import it like this: ``` from clubhouse_api import ClubHouse ```*

*If from GitHub or source: ``` from club_house_api import ClubHouse ```*

```python
from club_house_api import ClubHouse
import asyncio
import os

TOKEN = os.getenv('API_TOKEN')

club_house_session = ClubHouse(TOKEN, 'v3')
club_house = club_house_session.get_api()

async def main():

    all_projects = await club_house.projects()
    first_project_id = all_projects[0]['id']

    new_story = {'name': 'My new story', 'project_id': first_project_id}
    story = await club_house.stories.create(**new_story)
    print(story)

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
```

You can check out all the docs with examples [here](docs)

* [Epics](docs/epics.md)
* [Files](docs/files.md)
* [Labels](docs/labels.md)
* [Linked-Files](docs/linked_files.md)
* [Projects](docs/projects.md)
* [Story-Links](docs/story_links.md)
* [Stories](docs/stories.md)
  * [Comments](docs/comments.md)
  * [Tasks](docs/tasks.md)
  * [Reactions](docs/reactions.md)
* [Members](docs/members.md)
* [Teams](docs/teams.md)
* [Workflows](docs/workflows.md)


## Contributing

Bug reports and/or pull requests are welcome


## License

The module is available as open source under the terms of the [Apache License, Version 2.0](https://opensource.org/licenses/Apache-2.0)


