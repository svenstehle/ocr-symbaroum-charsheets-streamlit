import pytest


@pytest.fixture
def create_input_get_roll20_chat_input_str_draghul(
    create_expected_result_transform_attribute_keys_to_english_longhand_draghul,
    create_expected_result_extract_all_abilities_from_text_draghul,
):
    equipment = "1w10 orteg"
    armor = "2"
    abilities = create_expected_result_extract_all_abilities_from_text_draghul
    traits = "untot (I, siehe seite 231), robust (II, siehe seite 312)"
    yield (
        create_expected_result_transform_attribute_keys_to_english_longhand_draghul,
        equipment,
        armor,
        abilities,
        traits,
    )


@pytest.fixture
def create_input_get_attack_value_draghul(create_expected_result_transform_attribute_keys_to_english_longhand_draghul):
    yield create_expected_result_transform_attribute_keys_to_english_longhand_draghul


@pytest.fixture
def create_input_get_defense_value_draghul(create_expected_result_transform_attribute_keys_to_english_longhand_draghul):
    yield create_expected_result_transform_attribute_keys_to_english_longhand_draghul


@pytest.fixture
def create_input_transform_attribute_keys_to_english_longhand_draghul(
    create_expected_result_extract_all_attributes_from_text_draghul
):
    yield create_expected_result_extract_all_attributes_from_text_draghul


@pytest.fixture
def create_expected_result_transform_attribute_keys_to_english_longhand_draghul():
    yield {
        "strong": "3",
        "quick": "15",
        "vigilant": "10",
        "resolute": "13",
        "persuasive": "5",
        "cunning": "4",
        "discreet": "10",
        "accurate": "9",
    }


@pytest.fixture
def create_input_create_setattr_str_draghul(
    create_expected_result_transform_attribute_keys_to_english_longhand_draghul
):
    yield create_expected_result_transform_attribute_keys_to_english_longhand_draghul


@pytest.fixture
def create_expected_result_setattr_name_str_draghul():
    expected_result = "!setattr --name Gandalf --strong|3 --quick|15" +\
                        " --vigilant|10 --resolute|13 --persuasive|5" +\
                        " --cunning|4 --discreet|10 --accurate|9" +\
                        " --toughness|10|10"
    yield expected_result
    del expected_result


@pytest.fixture
def create_expected_result_setattr_sel_str_draghul():
    expected_result = "!setattr --sel --strong|3 --quick|15" +\
                        " --vigilant|10 --resolute|13 --persuasive|5" +\
                        " --cunning|4 --discreet|10 --accurate|9" +\
                        " --toughness|10|10"
    yield expected_result
    del expected_result


@pytest.fixture
def create_expected_result_create_token_mod_str_draghul():
    expected_result = "!token-mod {{\n" +\
                    "--set\n" +\
                        "\tlayer|gmlayer\n" +\
                        "\tbar1_link|quick\n" +\
                        "\tbar2_link|toughness\n" +\
                        "\tbar3_link|accurate\n" +\
                        "\ttooltip|Att: 9/Def: 15/Armor: 2" +\
                        "\tABILITIES: Eisenfaust:Adept, Schildkampf:Novize, Testskill:Meister" +\
                        "\tTRAITS: untot (I, siehe seite 231), robust (II, siehe seite 312)" +\
                        "\tEQUIPMENT: 1w10 orteg\n" +\
                        "\tshow_tooltip|yes\n" +\
                        "\tdefaulttoken\n" +\
                        "}}"

    yield expected_result
    del expected_result


@pytest.fixture
def prep_create_token_mod_str_draghul(
    create_expected_result_transform_attribute_keys_to_english_longhand_draghul,
    create_expected_result_create_token_mod_str_draghul,
    create_expected_result_extract_all_abilities_from_text_draghul,
):
    equipment = "1w10 orteg"
    armor = "2"
    abilities = create_expected_result_extract_all_abilities_from_text_draghul
    traits = "untot (I, siehe seite 231), robust (II, siehe seite 312)"
    yield (
        create_expected_result_transform_attribute_keys_to_english_longhand_draghul,
        equipment,
        armor,
        abilities,
        traits,
        create_expected_result_create_token_mod_str_draghul,
    )


@pytest.fixture
def create_input_get_roll20_chat_input_str_baiagorn(
    create_expected_result_transform_attribute_keys_to_english_longhand_baiagorn
):
    equipment = "keine"
    armor = "4"
    abilities = {"Berserkerrausch": "Adept"}
    traits = "natürliche waffen (I), robust (I), test1 (III), test2 (III), test3 (II)"
    yield (
        create_expected_result_transform_attribute_keys_to_english_longhand_baiagorn,
        equipment,
        armor,
        abilities,
        traits,
    )


@pytest.fixture
def create_input_get_attack_value_baiagorn(
    create_expected_result_transform_attribute_keys_to_english_longhand_baiagorn
):
    yield create_expected_result_transform_attribute_keys_to_english_longhand_baiagorn


@pytest.fixture
def create_input_get_defense_value_baiagorn(
    create_expected_result_transform_attribute_keys_to_english_longhand_baiagorn
):
    yield create_expected_result_transform_attribute_keys_to_english_longhand_baiagorn


@pytest.fixture
def create_input_transform_attribute_keys_to_english_longhand_baiagorn(
    create_expected_result_extract_all_attributes_from_text_baiagorn
):
    yield create_expected_result_extract_all_attributes_from_text_baiagorn


@pytest.fixture
def create_expected_result_transform_attribute_keys_to_english_longhand_baiagorn():
    yield {
        "strong": "15",
        "quick": "7",
        "vigilant": "11",
        "resolute": "13",
        "persuasive": "5",
        "cunning": "10",
        "discreet": "9",
        "accurate": "10",
    }


@pytest.fixture
def create_input_create_setattr_str_baiagorn(
    create_expected_result_transform_attribute_keys_to_english_longhand_baiagorn
):
    yield create_expected_result_transform_attribute_keys_to_english_longhand_baiagorn


@pytest.fixture
def create_expected_result_setattr_name_str_baiagorn():
    expected_result = "!setattr --name Legolas --strong|15 --quick|7" +\
                        " --vigilant|11 --resolute|13 --persuasive|5" +\
                        " --cunning|10 --discreet|9 --accurate|10" +\
                        " --toughness|15|15"
    yield expected_result
    del expected_result


@pytest.fixture
def create_expected_result_setattr_sel_str_baiagorn():
    expected_result = "!setattr --sel --strong|15 --quick|7" +\
                        " --vigilant|11 --resolute|13 --persuasive|5" +\
                        " --cunning|10 --discreet|9 --accurate|10" +\
                        " --toughness|15|15"
    yield expected_result
    del expected_result


@pytest.fixture
def create_expected_result_create_token_mod_str_baiagorn():
    expected_result = "!token-mod {{\n" +\
                    "--set\n" +\
                        "\tlayer|gmlayer\n" +\
                        "\tbar1_link|quick\n" +\
                        "\tbar2_link|toughness\n" +\
                        "\tbar3_link|accurate\n" +\
                        "\ttooltip|Att: 10/Def: 7/Armor: 4" +\
                        "\tABILITIES: Berserkerrausch:Adept" +\
                        "\tTRAITS: natürliche waffen (I), robust (I), " +\
                        "test1 (III), test2 (III), test3 (II)" +\
                        "\tEQUIPMENT: keine\n" +\
                        "\tshow_tooltip|yes\n" +\
                        "\tdefaulttoken\n" +\
                        "}}"

    yield expected_result
    del expected_result


@pytest.fixture
def prep_create_token_mod_str_baiagorn(
    create_expected_result_transform_attribute_keys_to_english_longhand_baiagorn,
    create_expected_result_create_token_mod_str_baiagorn,
):
    equipment = "keine"
    armor = "4"
    abilities = {"Berserkerrausch": "Adept"}
    traits = "natürliche waffen (I), robust (I), test1 (III), test2 (III), test3 (II)"
    yield (
        create_expected_result_transform_attribute_keys_to_english_longhand_baiagorn,
        equipment,
        armor,
        abilities,
        traits,
        create_expected_result_create_token_mod_str_baiagorn,
    )


@pytest.fixture
def create_input_get_roll20_chat_input_str_brand(
    create_expected_result_transform_attribute_keys_to_english_longhand_brand
):
    equipment = "glowing, oozing full plate"
    armor = "UNKNOWN"
    abilities = {"Bodyguard": "master", "Iron Fist": "master", "Two-handed Force": "adept"}
    traits = "-"
    yield create_expected_result_transform_attribute_keys_to_english_longhand_brand, equipment, armor, abilities, traits


@pytest.fixture
def create_input_get_attack_value_brand(create_expected_result_transform_attribute_keys_to_english_longhand_brand):
    yield create_expected_result_transform_attribute_keys_to_english_longhand_brand


@pytest.fixture
def create_input_get_defense_value_brand(create_expected_result_transform_attribute_keys_to_english_longhand_brand):
    yield create_expected_result_transform_attribute_keys_to_english_longhand_brand


@pytest.fixture
def create_input_transform_attribute_keys_to_english_longhand_brand(
    create_expected_result_extract_all_attributes_from_text_eng_brand
):
    yield create_expected_result_extract_all_attributes_from_text_eng_brand


@pytest.fixture
def create_expected_result_transform_attribute_keys_to_english_longhand_brand():
    yield {
        "strong": "15",
        "quick": "11",
        "vigilant": "10",
        "resolute": "10",
        "persuasive": "5",
        "cunning": "7",
        "discreet": "9",
        "accurate": "13",
    }


@pytest.fixture
def create_input_create_setattr_str_brand(create_expected_result_transform_attribute_keys_to_english_longhand_brand):
    yield create_expected_result_transform_attribute_keys_to_english_longhand_brand


@pytest.fixture
def create_expected_result_setattr_name_str_brand():
    expected_result = "!setattr --name Hulk --strong|15 --quick|11" +\
                        " --vigilant|10 --resolute|10 --persuasive|5" +\
                        " --cunning|7 --discreet|9 --accurate|13" +\
                        " --toughness|15|15"
    yield expected_result
    del expected_result


@pytest.fixture
def create_expected_result_setattr_sel_str_brand():
    expected_result = "!setattr --sel --strong|15 --quick|11" +\
                        " --vigilant|10 --resolute|10 --persuasive|5" +\
                        " --cunning|7 --discreet|9 --accurate|13" +\
                        " --toughness|15|15"
    yield expected_result
    del expected_result


@pytest.fixture
def create_expected_result_create_token_mod_str_brand():
    expected_result = "!token-mod {{\n" +\
                    "--set\n" +\
                        "\tlayer|gmlayer\n" +\
                        "\tbar1_link|quick\n" +\
                        "\tbar2_link|toughness\n" +\
                        "\tbar3_link|accurate\n" +\
                        "\ttooltip|Att: 13/Def: 11/Armor: UNKNOWN" +\
                        "\tABILITIES: Bodyguard:master, Iron Fist:master, Two-handed Force:adept" +\
                        "\tTRAITS: -" +\
                        "\tEQUIPMENT: glowing, oozing full plate\n" +\
                        "\tshow_tooltip|yes\n" +\
                        "\tdefaulttoken\n" +\
                        "}}"

    yield expected_result
    del expected_result


@pytest.fixture
def prep_create_token_mod_str_brand(
    create_expected_result_transform_attribute_keys_to_english_longhand_brand,
    create_expected_result_create_token_mod_str_brand,
):
    equipment = "glowing, oozing full plate"
    armor = "UNKNOWN"
    abilities = {"Bodyguard": "master", "Iron Fist": "master", "Two-handed Force": "adept"}
    traits = "-"
    yield (
        create_expected_result_transform_attribute_keys_to_english_longhand_brand,
        equipment,
        armor,
        abilities,
        traits,
        create_expected_result_create_token_mod_str_brand,
    )


@pytest.fixture
def create_input_get_roll20_chat_input_str_fairy(
    create_expected_result_transform_attribute_keys_to_english_longhand_fairy
):
    equipment = "none"
    armor = "UNKNOWN"
    abilities = {"Abilities found in text": "Zero"}
    traits = "-"
    yield create_expected_result_transform_attribute_keys_to_english_longhand_fairy, equipment, armor, abilities, traits


@pytest.fixture
def create_input_get_attack_value_fairy(create_expected_result_transform_attribute_keys_to_english_longhand_fairy):
    yield create_expected_result_transform_attribute_keys_to_english_longhand_fairy


@pytest.fixture
def create_input_get_defense_value_fairy(create_expected_result_transform_attribute_keys_to_english_longhand_fairy):
    yield create_expected_result_transform_attribute_keys_to_english_longhand_fairy


@pytest.fixture
def create_input_transform_attribute_keys_to_english_longhand_fairy(
    create_expected_result_extract_all_attributes_from_text_eng_fairy
):
    yield create_expected_result_extract_all_attributes_from_text_eng_fairy


@pytest.fixture
def create_expected_result_attributes_fairy(create_expected_result_transform_attribute_keys_to_english_longhand_fairy):
    yield create_expected_result_transform_attribute_keys_to_english_longhand_fairy


@pytest.fixture
def create_expected_result_transform_attribute_keys_to_english_longhand_fairy():
    yield {
        "strong": "5",
        "quick": "13",
        "vigilant": "11",
        "resolute": "7",
        "persuasive": "9",
        "cunning": "10",
        "discreet": "15",
        "accurate": "10",
    }


@pytest.fixture
def create_input_create_setattr_str_fairy(create_expected_result_transform_attribute_keys_to_english_longhand_fairy):
    yield create_expected_result_transform_attribute_keys_to_english_longhand_fairy


@pytest.fixture
def create_expected_result_setattr_name_str_fairy():
    expected_result = "!setattr --name Captain Marvel --strong|5 --quick|13" +\
                        " --vigilant|11 --resolute|7 --persuasive|9" +\
                        " --cunning|10 --discreet|15 --accurate|10" +\
                        " --toughness|10|10"
    yield expected_result
    del expected_result


@pytest.fixture
def create_expected_result_setattr_sel_str_fairy():
    expected_result = "!setattr --sel --strong|5 --quick|13" +\
                        " --vigilant|11 --resolute|7 --persuasive|9" +\
                        " --cunning|10 --discreet|15 --accurate|10" +\
                        " --toughness|10|10"
    yield expected_result
    del expected_result


@pytest.fixture
def create_expected_result_create_token_mod_str_fairy():
    expected_result = "!token-mod {{\n" +\
                    "--set\n" +\
                        "\tlayer|gmlayer\n" +\
                        "\tbar1_link|quick\n" +\
                        "\tbar2_link|toughness\n" +\
                        "\tbar3_link|accurate\n" +\
                        "\ttooltip|Att: 10/Def: 13/Armor: UNKNOWN" +\
                        "\tABILITIES: Abilities found in text:Zero" +\
                        "\tTRAITS: -" +\
                        "\tEQUIPMENT: none\n" +\
                        "\tshow_tooltip|yes\n" +\
                        "\tdefaulttoken\n" +\
                        "}}"

    yield expected_result
    del expected_result


@pytest.fixture
def prep_create_token_mod_str_fairy(
    create_expected_result_transform_attribute_keys_to_english_longhand_fairy,
    create_expected_result_create_token_mod_str_fairy,
):
    equipment = "none"
    armor = "UNKNOWN"
    abilities = {"Abilities found in text": "Zero"}
    traits = "-"
    yield (
        create_expected_result_transform_attribute_keys_to_english_longhand_fairy,
        equipment,
        armor,
        abilities,
        traits,
        create_expected_result_create_token_mod_str_fairy,
    )


@pytest.fixture
def prep_transform_attribute_keys_to_english_longhand_not_supported_language(
    prep_ocr_text_unknown_language, create_expected_result_transform_attribute_keys_to_english_longhand_fairy
):
    attributes = create_expected_result_transform_attribute_keys_to_english_longhand_fairy
    text = prep_ocr_text_unknown_language
    yield text, attributes
    del text, attributes


def create_input_result_pairs_get_toughness():
    input_result_pairs = [
        (
            {
                "strong": "15"
            },
            15,
        ),
        (
            {
                "strong": "11"
            },
            11,
        ),
        (
            {
                "strong": "10"
            },
            10,
        ),
        (
            {
                "strong": "9"
            },
            10,
        ),
        (
            {
                "strong": "3"
            },
            10,
        ),
    ]
    return input_result_pairs


@pytest.fixture(params=create_input_result_pairs_get_toughness())
def prep_get_toughness(request):
    attributes = request.param[0]
    expected_result = request.param[1]
    yield attributes, expected_result
    del attributes, expected_result


@pytest.fixture
def create_expected_result_get_attribute_mapping_for_language_ger():
    # pylint: disable=duplicate-code
    mapping = {
        "strong": "stärke",
        "quick": "gewandtheit",
        "vigilant": "aufmerksamkeit",
        "resolute": "willenskraft",
        "persuasive": "ausstrahlung",
        "cunning": "scharfsinn",
        "discreet": "heimlichkeit",
        "accurate": "präzision"
    }
    yield mapping
    del mapping


@pytest.fixture
def create_expected_result_get_attribute_mapping_for_language_eng():
    # pylint: disable=duplicate-code
    mapping = {
        "strong": "str",
        "quick": "qui",
        "vigilant": "vig",
        "resolute": "res",
        "persuasive": "per",
        "cunning": "cun",
        "discreet": "dis",
        "accurate": "acc"
    }
    yield mapping
    del mapping
