# StoryLinks

Before that setup the default client, or will inject your own client.

## Creating

```python
id_story = 125
new_story_link = { 'subject_id': 3, 'object_id': 2, 'verb': 'blocks'}
story_link = await club_house.story_links.create(id_story, **new_story_link)
```

## Updating

```python
id_story_link = 126
new_story_link = { 'subject_id': 3, 'object_id': 2, 'verb': 'blocks'}
story_link = await club_house.story_links.update(id_story_link, **new_story_link)
```

## Get by id

```python
id_story_link = 126
story_link = await club_house.story_links.get(id_story_link)
```

## Deleting by id

When None is returned this means it was successfull

```python
id_story_link = 126
await club_house.story_links.delete(id_story_link)
```
