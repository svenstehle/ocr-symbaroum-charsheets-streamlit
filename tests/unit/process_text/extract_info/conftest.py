import pytest


@pytest.fixture
def create_expected_result_extract_tactics_from_text_fairy():
    expected_result = "Renn and his friends will not attack more " +\
                        "than one or two persons at a time. They wait for " +\
                        "the opportunity to arise before fearlessly assaul" +\
                        "ting the prey."
    yield expected_result.lower()
    del expected_result


@pytest.fixture
def create_expected_result_extract_tactics_from_text_draghul():
    expected_result = "Der Untote verhält sich gemäß dem Willen seines " +\
                        "Erschaffers oder nach seinem eigenen Willen. " +\
                        "Er ist mmer auf der Suche nach warmen Fleisch und " +\
                        "frischem Blut."
    yield expected_result.lower()
    del expected_result


@pytest.fixture
def create_expected_result_extract_tactics_from_text_baiagorn():
    expected_result = "Normalerweise sind Baiagornen vor" +\
                        "sichtige Kreaturen, doch wenn sie verletzt oder " +\
                        "verärgert werden, verwandeln sie sich brüllende " +\
                        "Bestien, die wie wild mit ihren Krallen um sich " +\
                        "schlagen und den nächsten Feind oder ihre " +\
                        "Beute unerbittlich angreifen."
    yield expected_result.lower()
    del expected_result


@pytest.fixture
def create_expected_result_extract_tactics_from_text_guard():
    expected_result = "Der Spielercharakter, der am größten " +\
                        "\"oder stärksten wirkt, wird zuerst vonzwei Wäch" +\
                        "tern angegriffen. Jeder andere Spielercharakter " +\
                        "\'wird von einem Wachter angegriffen."
    yield expected_result.lower()
    del expected_result


@pytest.fixture
def create_expected_result_extract_tactics_from_text_aeber():
    expected_result = "Der ber setzt fingierte Angriffe ein und " +\
                        "versucht damit. seine Feinde zu verscheuchen. " +\
                        "Sollte das scheitern. verlässt er sich darauf, " +\
                        "dass seine Reflexe, seine widerstandsfähige " +\
                        "Haut und seine brutalen Hauer ausreichen, um " +\
                        "jeden Gegner niederzumetzeln."
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
def create_input_get_roll20_chat_input_str_draghul(
    create_expected_result_transform_attribute_keys_to_english_longhand_draghul,
    create_expected_result_extract_all_abilities_from_text_draghul,
):
    equipment = "1w10 orteg"
    armor = "2"
    abilities = create_expected_result_extract_all_abilities_from_text_draghul
    yield create_expected_result_transform_attribute_keys_to_english_longhand_draghul, equipment, armor, abilities


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
                        "\tTRAITS: blablabla" +\
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
    yield (
        create_expected_result_transform_attribute_keys_to_english_longhand_draghul,
        equipment,
        armor,
        abilities,
        create_expected_result_create_token_mod_str_draghul,
    )


@pytest.fixture
def create_input_get_roll20_chat_input_str_baiagorn(
    create_expected_result_transform_attribute_keys_to_english_longhand_baiagorn
):
    equipment = "keine"
    armor = "4"
    abilities = {"Berserkerrausch": "Adept"}
    yield create_expected_result_transform_attribute_keys_to_english_longhand_baiagorn, equipment, armor, abilities


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
                        "\tTRAITS: blablabla" +\
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
    yield (
        create_expected_result_transform_attribute_keys_to_english_longhand_baiagorn,
        equipment,
        armor,
        abilities,
        create_expected_result_create_token_mod_str_baiagorn,
    )


@pytest.fixture
def create_input_get_roll20_chat_input_str_brand(
    create_expected_result_transform_attribute_keys_to_english_longhand_brand
):
    equipment = "glowing, oozing full plate"
    armor = "UNKNOWN"
    abilities = {"Bodyguard": "master", "Iron Fist": "master", "Two-handed Force": "adept"}
    yield create_expected_result_transform_attribute_keys_to_english_longhand_brand, equipment, armor, abilities


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
                        "\tTRAITS: blablabla" +\
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
    yield (
        create_expected_result_transform_attribute_keys_to_english_longhand_brand,
        equipment,
        armor,
        abilities,
        create_expected_result_create_token_mod_str_brand,
    )


@pytest.fixture
def create_input_get_roll20_chat_input_str_fairy(
    create_expected_result_transform_attribute_keys_to_english_longhand_fairy
):
    equipment = "none"
    armor = "UNKNOWN"
    abilities = {"Abilities found in text": "Zero"}
    yield create_expected_result_transform_attribute_keys_to_english_longhand_fairy, equipment, armor, abilities


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
                        "\tTRAITS: blablabla" +\
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
    yield (
        create_expected_result_transform_attribute_keys_to_english_longhand_fairy,
        equipment,
        armor,
        abilities,
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
