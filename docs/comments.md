# Comments

Before that setup the default client, or will inject your own client.

## Creating

```python
id_story = 125
new_comment = {'text': 'foo'}
comment = await club_house.stories.create(id_story, 'comments', **new_comment)
```

## Updating

```python
id_story = 125
id_comment = 127
update_comment = {'text': 'foo'}
comment = await club_house.stories.update(id_story, 'comments', 
                                              id_comment, **update_comment)
```

## Get by id

```python
id_story = 125
id_comment = 127
comment = await club_house.stories.get(id_story, 'comments', id_comment)
```

## Deleting by id

When None is returned this means it was successfull

```python
id_story = 125
id_comment = 127
await club_house.stories.delete(id_story, 'comments', id_comment)
```
