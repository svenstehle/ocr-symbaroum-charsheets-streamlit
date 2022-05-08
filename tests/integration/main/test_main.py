from src.main import main
from tests.testing_utils import replace_ubuntu_specific_characters


def test_main(capsys, prep_test_main):
    cfg, expected_result = prep_test_main
    main(cfg)
    out, err = capsys.readouterr()
    # replace ubuntu specific characters
    out = replace_ubuntu_specific_characters(out)
    assert out == expected_result
    assert err == ""
