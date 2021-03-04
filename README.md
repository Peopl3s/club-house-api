# club_house_api

![PyPI](https://img.shields.io/pypi/v/clubhouse_api?color=orange) ![Python 3.6, 3.7, 3.8](https://img.shields.io/pypi/pyversions/clubhouse?color=blueviolet) ![GitHub Pull Requests](https://img.shields.io/github/issues-pr/peopl3s/club-house-api?color=blueviolet) ![License](https://img.shields.io/pypi/l/clubhouse-api?color=blueviolet) ![Forks](https://img.shields.io/github/forks/peopl3s/club-house-api?style=social)

**club_house_api** - this module is a Python client library for The ClubHouse project management platform API (ClubHouse API wrapper)


**Clubhouse** is collaborative project management that streamlines and refines your existing workflow. The intuitive and powerful project management platform loved by software teams of all sizes. [Clubhouse](https://clubhouse.io) is here.


**API documentation** [https://clubhouse.io/api/rest/v3/](https://clubhouse.io/api/rest/v3/)

## Installation

Install the current version with PyPI:

```python
pip install clubhouse_api
```

Or from Github:
```python
pip install https://github.com/Peopl3s/club-house-api/archive/main.zip
```

And then execute:

    $ bundle

Or install it yourself as:

    $ gem install clubhouse.io-ruby

## Usage

### Setting up a client

Before we start its best to setup a default client if you are just using it with only one token.

You can generate a token for clubhouse by going to the account section and generating a new token

```ruby
Clubhouse.default_client = Clubhouse::Client.new('YOUR_TOKEN_HERE')
```

Now we are ready to start creating stories. In its basic form this is how you create a story

This will create a new story in the first project that is returned from the API in the all projects request.

```ruby
story = Clubhouse::Story.new(name:'My Story', project_id: Clubhouse::Project.all.first.id)
story.save
```

You can check out all the other docs on other resources with examples [here](docs)

* [Epics](docs/epics.md)
* [Files](docs/files.md)
* [Labels](docs/labels.md)
* [Linked-Files](docs/linked_files.md)
* [Projects](docs/projects.md)
* [Story-Links](docs/story_links.md)
* [Stories](docs/stories.md)
  * [Comments](docs/comments.md)
  * [Tasks](docs/tasks.md)
* [Users](docs/users.md)
* [Workflows](docs/workflows.md)


## Contributing

Bug reports and/or pull requests are welcome


## License

The gem is available as open source under the terms of the [MIT License](http://opensource.org/licenses/MIT)


