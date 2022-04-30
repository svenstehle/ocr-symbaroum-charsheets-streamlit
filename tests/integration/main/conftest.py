import pytest
from hydra import compose, initialize


@pytest.fixture
def prep_test_main():
    with initialize(config_path="../../../src/conf", job_name="test_app"):
        cfg = compose(config_name="config", overrides=["testing=enabled"])
        expected_result = "ORIGINAL\n========\nDas ist ein Test\n\n"
        yield cfg, expected_result
        del cfg, expected_result
