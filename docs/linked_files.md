# LinkedFiles

Before that setup the default client, or will inject your own client.

## Creating

```python
new_linked_file = {'name': 'Linked File One',
                   'type': 'url',
                   'url': 'https://github.com/lutangar/cities.json/blob/master/cities.json'}
linked_file = await club_house.linked_files.create(**new_linked_file)
```

## Updating

```python
id_file = 118
updated_fields= {'description': 'foo'}
linked_file = await club_house.linked_files.update(id_file, **updated_fields)
```

## Get by id

```python
id_file = 118
linked_file = await club_house.linked_files.get(id_file)
```

## Deleting by id

When None is returned this means it was successfull

```python
id_file = 118 
await club_house.linked_files.delete(id_file)
```

## Listing

Returns a list of all labels

```python
all_linked_files = await club_house.linked_files()
```

