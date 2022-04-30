from src.main import main


def test_main(capsys, prep_test_main):
    cfg, expected_result = prep_test_main
    main(cfg)
    out, err = capsys.readouterr()
    # replace ubuntu specific characters
    out = out.replace("\x0c", "")    # pylint: disable=anomalous-backslash-in-string
    assert out == expected_result
    assert err == ""
