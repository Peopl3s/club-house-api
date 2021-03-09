# Tasks

Before that setup the default client, or will inject your own client.

## Creating

```python
id_story = 125
new_task= {'description': 'My Task', 'complete': 'false'}
task = await club_house.stories.create(id_story, 'tasks', **new_task)
```

## Updating

```python
id_story = 125
    id_task = 128
    update_task= {'description': 'My Task Change'}
    task = await club_house.stories.update(id_story, 'tasks', 
                                           id_task, **update_task)
```

## Get by id

```python
id_story = 125
id_task = 128
task = await club_house.stories.get(id_story, 'tasks', id_task)
```

## Deleting by id

When None is returned this means it was successfull

```python
id_story = 125
id_task = 128
task = await club_house.stories.delete(id_story, 'tasks', id_task)
```
