from src.process_text import extract_all_skills_from_text


def test_extract_all_skills_from_text(prep_extract_all_skills_from_text):
    text, expected_result = prep_extract_all_skills_from_text
    result = extract_all_skills_from_text(text)
    assert expected_result == result
