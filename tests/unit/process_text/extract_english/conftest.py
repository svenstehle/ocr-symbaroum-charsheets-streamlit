import pytest


@pytest.fixture
def create_expected_result_extract_all_abilities_from_text_fairy():
    expected_result = {"Abilities found in text": "Zero"}
    yield expected_result
    del expected_result


@pytest.fixture
def create_expected_result_extract_all_abilities_from_text_brand():
    expected_result = {"Bodyguard": "master", "Iron Fist": "master", "Two-handed Force": "adept"}
    yield expected_result
    del expected_result


@pytest.fixture
def create_expected_result_extract_all_abilities_from_text_hunter():
    expected_result = {"Acrobatics": "master", "Marksman": "master", "Sixth Sense": "master", "Steadfast": "master"}
    yield expected_result
    del expected_result


@pytest.fixture
def create_expected_result_get_all_attribute_values_from_text_eng_fairy():
    expected_result = ["10", "10", "15", "9", "13", "7", "5", "11"]
    yield expected_result
    del expected_result


@pytest.fixture
def create_expected_result_get_all_attribute_values_from_text_eng_brand():
    expected_result = ["13", "7", "9", "5", "11", "10", "15", "10"]
    yield expected_result
    del expected_result


@pytest.fixture
def create_expected_result_get_all_attribute_values_from_text_eng_hunter():
    expected_result = ["5", "10", "10", "7", "11", "16", "9", "18"]
    yield expected_result
    del expected_result


@pytest.fixture
def create_expected_result_get_all_attribute_values_from_text_eng_sikander():
    expected_result = ["9", "11", "5", "10", "13", "15", "7", "10"]
    yield expected_result
    del expected_result


@pytest.fixture
def create_expected_result_extract_equipment_from_text_eng_fairy():
    expected_result = "none"
    yield expected_result
    del expected_result


@pytest.fixture
def create_expected_result_extract_equipment_from_text_eng_brand():
    expected_result = "glowing, oozing full plate"
    yield expected_result
    del expected_result


@pytest.fixture
def create_expected_result_extract_equipment_from_text_eng_hunter():
    expected_result = "none"
    yield expected_result
    del expected_result


@pytest.fixture
def create_expected_result_extract_equipment_from_text_eng_sikander():
    expected_result = "order cloak, 1d10 thaler"
    yield expected_result
    del expected_result


@pytest.fixture
def create_expected_result_extract_armor_from_text_eng_fairy():
    expected_result = "UNKNOWN"
    yield expected_result
    del expected_result


@pytest.fixture
def create_expected_result_extract_traits_from_text_eng_fairy():
    expected_result = "-"
    yield expected_result
    del expected_result


@pytest.fixture
def create_expected_result_extract_traits_from_text_eng_brand():
    expected_result = "-"
    yield expected_result
    del expected_result


@pytest.fixture
def create_expected_result_extract_traits_from_text_eng_hunter():
    expected_result = "bloodlust (III. see p. 54), manifestation (III), spirit form (III)"
    yield expected_result
    del expected_result


@pytest.fixture
def create_expected_result_extract_traits_from_text_eng_sikander():
    expected_result = "test1 (II), test2 (III), test3 (III), test4 (II), test5 (III)"
    yield expected_result
    del expected_result


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
