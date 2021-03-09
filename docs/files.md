# Files

Before that setup the default client, or will inject your own client.

## Upload Files

Upload one or more Files, which can then be associated to a Story Description, Story Comment, or Epic Comment.

```python
new_file = {'file' : 'D:/112.py'}
file = await club_house.files.upload(**new_file)
```

## Updating

```python
id_file = 117
update_fields = {'name': 'New file name', 'description': 'new desc'}
file = await club_house.files.update(id_file, **update_fields)
```

## Get by id

```python
id_file = 117
file = await club_house.files.get(id_file)
```

## Deleting by id

When None is returned this means it was successfull

```python
id_file = 117
await club_house.files.delete(id_file)
```

## Listing

Returns a list of all files

```python
files = await club_house.files()
```

