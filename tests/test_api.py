import os
import sys
import pytest
import asyncio
from club_house_api.utils import with_mocked_api
from club_house_api import ClubHouse, ClubHouseApiMethod

REQ_WITH_ONE_ARG = {'role': 'owner'}
REQ_WITH_MANY_ARGS = {'app_url': 'https://app.clubhouse.io/pylounge/story/36','archived': False, 'started': False, 
                  'num_tasks_completed': 0, 'completed_at_override': None, 'started_at': None, 'completed_at': None, 'name': 'ghhghg', 
                  'completed': False, 'blocker': False, 'epic_id': 27, 'external_links': [], 
                  'previous_iteration_ids': [], 'requested_by_id': '6028be51-95af-4051-8652-eef622045976', 'id': 36,
                  'blocked': False, 'project_id': 4, 'linked_file_ids': [], 'deadline': None, 
                  'stats': {'num_related_documents': 0}, 'comment_ids': [], 'created_at': '2021-02-21T12:13:50Z', 'moved_at': '2021-02-21T12:13:50Z'}
REQ_WITH_NO_ARGS_NO_KWARGS = ["{'role': 'owner', 'entity_type': 'member', 'disabled': False, 'updated_at': '2021-02-14T06:08:17Z'}"]
REQ_WITH_KWARGS = { 'name' : "New story with some tasks",'project_id':4}
REQ_WITH_ARGS_KWARGS = {'description': 'Task description 3', 'entity_type': 'story-task', 'story_id': 39, 
                        'completed_at': None, 'updated_at': '2021-02-21T13:06:14Z', 
                        'id': 41, 'position': 2, 'complete': False, 'created_at': '2021-02-21T12:33:34Z'}

@pytest.mark.asyncio
@with_mocked_api(REQ_WITH_ONE_ARG)
async def test_api_response_with_one_args(ch_api:ClubHouseApiMethod):
    response = await ch_api.members.get('6028be51-95af-4051-8652-eef622045976')
    assert isinstance(response, dict)
    assert response['role'] == 'owner'

@pytest.mark.asyncio
@with_mocked_api(REQ_WITH_MANY_ARGS)
async def test_api_response_with_many_args(ch_api:ClubHouseApiMethod):
    response = await ch_api.projects(4, 'stories')
    assert isinstance(response, dict)
    assert response['id'] == 36

@pytest.mark.asyncio
@with_mocked_api(REQ_WITH_NO_ARGS_NO_KWARGS)
async def test_api_response_no_args_no_kwargs(ch_api:ClubHouseApiMethod):
    response = await ch_api.members()
    assert isinstance(response, list)
    assert len(response) == 1 
 
@pytest.mark.asyncio
@with_mocked_api(REQ_WITH_KWARGS)
async def test_api_response_with_kwargs(ch_api:ClubHouseApiMethod):
    new_story = { 'name' : "New story with some tasks",
                  'project_id':4
    }
    response = await ch_api.stories.create(**new_story)
    assert isinstance(response, dict)
    assert response['name'] == 'New story with some tasks'

@pytest.mark.asyncio
@with_mocked_api(REQ_WITH_ARGS_KWARGS)
async def test_api_response_with_args_kwargs(ch_api:ClubHouseApiMethod):
    story_id = 39
    task_id = 41
    response = await ch_api.stories.get(story_id, 'tasks', task_id)
    assert isinstance(response, dict)
    assert response['description'] == 'Task description 3'

TOKEN = os.getenv("TOKEN")

@pytest.fixture
def ch_api():
    club_house_session = ClubHouse(TOKEN, 'v3')
    return club_house_session.get_api()


@pytest.mark.asyncio
async def test_api_wrong_method(ch_api:ClubHouseApiMethod):
    with pytest.raises(Exception):
        await ch_api.ssdtories()

@pytest.mark.asyncio
async def test_api_wrong_method_args_kwargs(ch_api:ClubHouseApiMethod):
    with pytest.raises(Exception):
        await ch_api.stories.get(9999)

