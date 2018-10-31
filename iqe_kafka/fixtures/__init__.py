import pytest

@pytest.fixture
def test_topic():
    SimpleClient(MQ.API.KAFKA).ensure_topic_exists('test-topic')