import pytest


def create_input_result_get_attribute_value_from_text_draghul():
    input_result_pairs = [
        ("stärke", "3"),
        ("scharfsinn", "4"),
        ("gewandtheit", "15"),
        ("aufmerksamkeit", "10"),
        ("ausstrahlung", "5"),
        ("präzision", "9"),
        ("willenskraft", "13"),
        ("heimlichkeit", "10"),
    ]
    return input_result_pairs


@pytest.fixture(params=create_input_result_get_attribute_value_from_text_draghul())
def prep_input_result_get_attribute_value_from_text_draghul(request):
    target_attribute = request.param[0]
    expected_result = request.param[1]
    yield target_attribute, expected_result
    del target_attribute, expected_result


@pytest.fixture
def create_expected_result_extract_all_abilities_from_text_baiagorn():
    expected_result = {"Berserkerrausch": "Adept"}
    yield expected_result
    del expected_result


@pytest.fixture
def create_expected_result_extract_all_abilities_from_text_guard():
    expected_result = {"Abilities found in text": "Zero"}
    yield expected_result
    del expected_result


@pytest.fixture
def create_expected_result_extract_all_abilities_from_text_aeber():
    expected_result = {"Eisenfaust": "Adept"}
    yield expected_result
    del expected_result


def create_input_result_get_attribute_value_from_text_baiagorn():
    input_result_pairs = [
        ("stärke", "15"),
        ("scharfsinn", "10"),
        ("gewandtheit", "7"),
        ("aufmerksamkeit", "11"),
        ("ausstrahlung", "5"),
        ("präzision", "10"),
        ("willenskraft", "13"),
        ("heimlichkeit", "9"),
    ]
    return input_result_pairs


@pytest.fixture(params=create_input_result_get_attribute_value_from_text_baiagorn())
def prep_input_result_get_attribute_value_from_text_baiagorn(request):
    target_attribute = request.param[0]
    expected_result = request.param[1]
    yield target_attribute, expected_result
    del target_attribute, expected_result


def create_input_result_get_attribute_value_from_text_guard():
    input_result_pairs = [
        ("stärke", "15"),
        ("scharfsinn", "7"),
        ("gewandtheit", "10"),
        ("aufmerksamkeit", "11"),
        ("ausstrahlung", "9"),
        ("präzision", "13"),
        ("willenskraft", "10"),
        ("heimlichkeit", "5"),
    ]
    return input_result_pairs


@pytest.fixture(params=create_input_result_get_attribute_value_from_text_guard())
def prep_input_result_get_attribute_value_from_text_guard(request):
    target_attribute = request.param[0]
    expected_result = request.param[1]
    yield target_attribute, expected_result
    del target_attribute, expected_result


def create_input_result_get_attribute_value_from_text_aeber():
    input_result_pairs = [
        ("stärke", "15"),
        ("scharfsinn", "10"),
        ("gewandtheit", "13"),
        ("aufmerksamkeit", "9"),
        ("ausstrahlung", "5"),
        ("präzision", "10"),
        ("willenskraft", "11"),
        ("heimlichkeit", "7"),
    ]
    return input_result_pairs


@pytest.fixture(params=create_input_result_get_attribute_value_from_text_aeber())
def prep_input_result_get_attribute_value_from_text_aeber(request):
    target_attribute = request.param[0]
    expected_result = request.param[1]
    yield target_attribute, expected_result
    del target_attribute, expected_result


@pytest.fixture
def create_expected_result_extract_equipment_from_text_ger_draghul():
    expected_result = "1w10 orteg"
    yield expected_result
    del expected_result


@pytest.fixture
def create_expected_result_extract_equipment_from_text_ger_baiagorn():
    expected_result = "keine"
    yield expected_result
    del expected_result


@pytest.fixture
def create_expected_result_extract_equipment_from_text_ger_guard():
    expected_result = "1w10 schillinge, kautabak"
    yield expected_result
    del expected_result


@pytest.fixture
def create_expected_result_extract_equipment_from_text_ger_aeber():
    expected_result = "keine"
    yield expected_result
    del expected_result


@pytest.fixture
def create_expected_result_extract_armor_from_text_ger_draghul():
    expected_result = "2"
    yield expected_result
    del expected_result


@pytest.fixture
def create_expected_result_extract_armor_from_text_ger_baiagorn():
    expected_result = "4"
    yield expected_result
    del expected_result


@pytest.fixture
def create_expected_result_extract_armor_from_text_ger_guard():
    expected_result = "3"
    yield expected_result
    del expected_result


@pytest.fixture
def create_expected_result_extract_armor_from_text_ger_aeber():
    expected_result = "7"
    yield expected_result
    del expected_result


@pytest.fixture
def create_expected_result_extract_traits_from_text_ger_draghul():
    expected_result = "untot (I, siehe seite 231), robust (II, siehe seite 312)"
    yield expected_result
    del expected_result


@pytest.fixture
def create_expected_result_extract_traits_from_text_ger_baiagorn():
    expected_result = "natürliche waffen (I), robust (I), test1 (III), test2 (III), test3 (II)"
    yield expected_result
    del expected_result


@pytest.fixture
def create_expected_result_extract_traits_from_text_ger_guard():
    expected_result = "kontakte (karawanerwächter)"
    yield expected_result
    del expected_result


@pytest.fixture
def create_expected_result_extract_traits_from_text_ger_aeber():
    expected_result = "natürlicher panzer (II), natürliche waffen (II), robust (III, siehe seite 13)"
    yield expected_result
    del expected_result


@pytest.fixture
def create_expected_result_extract_tactics_from_text_draghul():
    expected_result = (
        "Der Untote verhält sich gemäß dem Willen seines "
        "Erschaffers oder nach seinem eigenen Willen. "
        "Er ist mmer auf der Suche nach warmen Fleisch und "
        "frischem Blut."
    )
    yield expected_result.lower()
    del expected_result


@pytest.fixture
def create_expected_result_extract_tactics_from_text_baiagorn():
    expected_result = (
        "Normalerweise sind Baiagornen vor"
        "sichtige Kreaturen, doch wenn sie verletzt oder "
        "verärgert werden, verwandeln sie sich brüllende "
        "Bestien, die wie wild mit ihren Krallen um sich "
        "schlagen und den nächsten Feind oder ihre "
        "Beute unerbittlich angreifen."
    )
    yield expected_result.lower()
    del expected_result


@pytest.fixture
def create_expected_result_extract_tactics_from_text_guard():
    expected_result = (
        "Der Spielercharakter, der am größten "
        "\"oder stärksten wirkt, wird zuerst vonzwei Wäch"
        "tern angegriffen. Jeder andere Spielercharakter "
        "\'wird von einem Wachter angegriffen."
    )
    yield expected_result.lower()
    del expected_result


@pytest.fixture
def create_expected_result_extract_tactics_from_text_aeber():
    expected_result = (
        "Der ber setzt fingierte Angriffe ein und "
        "versucht damit. seine Feinde zu verscheuchen. "
        "Sollte das scheitern. verlässt er sich darauf, "
        "dass seine Reflexe, seine widerstandsfähige "
        "Haut und seine brutalen Hauer ausreichen, um "
        "jeden Gegner niederzumetzeln."
    )
    yield expected_result.lower()
    del expected_result
