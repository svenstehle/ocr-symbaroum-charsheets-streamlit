import pytest


@pytest.fixture
def create_expected_result_extract_all_attributes_from_text_draghul():
    expected_result = {
        "stärke": "3",
        "scharfsinn": "4",
        "gewandtheit": "15",
        "aufmerksamkeit": "10",
        "ausstrahlung": "5",
        "präzision": "9",
        "willenskraft": "13",
        "heimlichkeit": "10",
    }
    yield expected_result
    del expected_result


@pytest.fixture
def create_expected_result_extract_all_attributes_from_text_baiagorn():
    expected_result = {
        "stärke": "15",
        "scharfsinn": "10",
        "gewandtheit": "7",
        "aufmerksamkeit": "11",
        "ausstrahlung": "5",
        "präzision": "10",
        "willenskraft": "13",
        "heimlichkeit": "9",
    }
    yield expected_result
    del expected_result


@pytest.fixture
def create_expected_result_extract_all_attributes_from_text_guard():
    expected_result = {
        "stärke": "15",
        "scharfsinn": "7",
        "gewandtheit": "10",
        "aufmerksamkeit": "11",
        "ausstrahlung": "9",
        "präzision": "13",
        "willenskraft": "10",
        "heimlichkeit": "5",
    }
    yield expected_result
    del expected_result


@pytest.fixture
def create_expected_result_extract_all_attributes_from_text_aeber():
    expected_result = {
        "stärke": "15",
        "scharfsinn": "10",
        "gewandtheit": "13",
        "aufmerksamkeit": "9",
        "ausstrahlung": "5",
        "präzision": "10",
        "willenskraft": "11",
        "heimlichkeit": "7",
    }
    yield expected_result
    del expected_result


@pytest.fixture
def create_expected_result_extract_all_attributes_from_text_eng_fairy():
    expected_result = {
        "acc": "10",
        "cun": "10",
        "dis": "15",
        "per": "9",
        "qui": "13",
        "res": "7",
        "str": "5",
        "vig": "11",
    }
    yield expected_result
    del expected_result


@pytest.fixture
def create_expected_result_extract_all_attributes_from_text_eng_brand():
    expected_result = {
        "acc": "13",
        "cun": "7",
        "dis": "9",
        "per": "5",
        "qui": "11",
        "res": "10",
        "str": "15",
        "vig": "10",
    }
    yield expected_result
    del expected_result


@pytest.fixture
def create_expected_result_extract_all_attributes_from_text_eng_hunter():
    expected_result = {
        "acc": "5",
        "cun": "10",
        "dis": "10",
        "per": "7",
        "qui": "11",
        "res": "16",
        "str": "9",
        "vig": "18",
    }
    yield expected_result
    del expected_result


@pytest.fixture
def create_expected_result_extract_all_attributes_from_text_eng_sikander():
    expected_result = {
        "acc": "9",
        "cun": "11",
        "dis": "5",
        "per": "10",
        "qui": "13",
        "res": "15",
        "str": "7",
        "vig": "10",
    }
    yield expected_result
    del expected_result


@pytest.fixture
def create_expected_result_extract_all_abilities_from_text_draghul():
    expected_result = {
        "Eisenfaust": "Adept",
        "Schildkampf": "Novize",
        "Testskill": "Meister",
    }
    yield expected_result
    del expected_result


@pytest.fixture
def create_expected_result_extract_all_abilities_from_text_sikander():
    expected_result = {"Brimstone Cascade": "master", "Flame Wall": "master"}
    yield expected_result
    del expected_result


@pytest.fixture
def create_input_extract_all_attributes_from_text_ger_general():
    attribute_names = [
        "stärke",
        "scharfsinn",
        "gewandtheit",
        "aufmerksamkeit",
        "ausstrahlung",
        "präzision",
        "willenskraft",
        "heimlichkeit",
    ]
    yield attribute_names
    del attribute_names


@pytest.fixture
def create_input_extract_all_attributes_from_text_eng_general():
    attribute_names = ["acc", "cun", "dis", "per", "qui", "res", "str", "vig"]
    yield attribute_names
    del attribute_names


@pytest.fixture
def create_expected_result_extract_tactics_from_text_fairy():
    expected_result = (
        "Renn and his friends will not attack more "
        "than one or two persons at a time. They wait for "
        "the opportunity to arise before fearlessly assaul"
        "ting the prey."
    )
    yield expected_result.lower()
    del expected_result


@pytest.fixture
def create_expected_result_extract_tactics_from_text_brand():
    expected_result = (
        "Brand protects his master by attacking "
        "an enemy in full force. Also, Brand will defend "
        "his master from all attacks and make counte"
        "rattacks against any attacker within range of "
        "melee, damage 8 (see the ability Bodyguard at "
        "master level)."
    )
    yield expected_result.lower()
    del expected_result


@pytest.fixture
def create_expected_result_extract_tactics_from_text_hunter():
    expected_result = (
        "The Eternal Hunter moves among the "
        "death dancers, shooting single arrows for en"
        "couragement. When a worthy opponent emerges. "
        "the hunter begins his own, personal hunt. He alter"
        "nates between firing deadly arrows and trying to "
        "charm and drink warm. delightful blood from the "
        "victim, saturated with the sublime taste of despe"
        "ration and fear. As soon as Gylta's herd becomes "
        "occupied with fighting the death dancers he takes "
        "the opportunity to commence his fight against the "
        "forest goddess."
    )
    yield expected_result.lower()
    del expected_result


@pytest.fixture
def create_expected_result_extract_tactics_from_text_sikander():
    expected_result = (
        "Sikander raises a Flame Wall around "
        "himself and his flaming servant. Anyone ente"
        "ring through the wall of fire encounters Brand in "
        "melee while Sikander maneuvers so he can cast a "
        "chain of Brimstone Cascades at the enemy. He is "
        "prepared to die for his claim and during the fight "
        "he accuses the attackers of wanting to steal his "
        "precious treasure."
    )
    yield expected_result.lower()
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
