from services.engine import HyperthyroidismKnowledgeEngine, \
    SECONDARY_HYPERTHROIDISM, \
    SUBCLINIC_HYPERTHROIDISM, \
    NEGATIVE_DIAGNOSIS, \
    T3_HYPERTYHROIDISM, \
    YATROGEN_HYPERTHYROIDISM, \
    PRIMARY_HYPERTHYROIDISM, \
    GRAVES, \
    GOITER, \
    ADENOMA


def test_secondary_hyperthroidism():
    assert SECONDARY_HYPERTHROIDISM == \
           HyperthyroidismKnowledgeEngine({
            "tachycardia": "Sí",
            "weight_loss": "Sí",
            "sudoration_increase": "Sí",
            "inflamation": "No",
            "free_tsh": "Elevado",
            "free_t4": "Elevado",
            "free_t3": "Bajo",
            "tyroidic_capture": "N/A",
            "triglobuline": "N/A",
            "nodular_area": "N/A"
            }).get_diagnosis()[0]


def test_subclinic_hyperthroidism():
    assert SUBCLINIC_HYPERTHROIDISM == \
           HyperthyroidismKnowledgeEngine({
            "tachycardia": "Sí",
            "weight_loss": "Sí",
            "sudoration_increase": "Sí",
            "inflamation": "No",
            "free_tsh": "Bajo",
            "free_t4": "Normal",
            "free_t3": "Normal",
            "tyroidic_capture": "N/A",
            "triglobuline": "N/A",
            "nodular_area": "N/A"
            }).get_diagnosis()[0]


def test_t3_hyperthiroidism():
    assert T3_HYPERTYHROIDISM == \
           HyperthyroidismKnowledgeEngine({
            "tachycardia": "Sí",
            "weight_loss": "Sí",
            "sudoration_increase": "Sí",
            "inflamation": "No",
            "free_tsh": "Bajo",
            "free_t4": "Normal",
            "free_t3": "Elevado",
            "tyroidic_capture": "N/A",
            "triglobuline": "N/A",
            "nodular_area": "N/A"
            }).get_diagnosis()[0]


def test_exogen_hormones_hyperthroidism():
    assert YATROGEN_HYPERTHYROIDISM == \
           HyperthyroidismKnowledgeEngine({
            "tachycardia": "Sí",
            "weight_loss": "Sí",
            "sudoration_increase": "Sí",
            "inflamation": "No",
            "free_tsh": "Bajo",
            "free_t4": "Elevado",
            "free_t3": "N/A",
            "tyroidic_capture": "Bajo",
            "triglobuline": "Bajo",
            "nodular_area": "N/A"
            }).get_diagnosis()[0]


def test_primary_hyperthroidism():
    assert PRIMARY_HYPERTHYROIDISM == \
           HyperthyroidismKnowledgeEngine({
            "tachycardia": "Sí",
            "weight_loss": "Sí",
            "sudoration_increase": "Sí",
            "inflamation": "No",
            "free_tsh": "Bajo",
            "free_t4": "Elevado",
            "free_t3": "N/A",
            "tyroidic_capture": "Bajo",
            "triglobuline": "Elevado",
            "nodular_area": "N/A"
            }).get_diagnosis()[0]


def test_graves():
    assert GRAVES == \
           HyperthyroidismKnowledgeEngine({
            "tachycardia": "Sí",
            "weight_loss": "Sí",
            "sudoration_increase": "Sí",
            "inflamation": "No",
            "free_tsh": "Bajo",
            "free_t4": "Elevado",
            "free_t3": "N/A",
            "tyroidic_capture": "Elevado y difuso",
            "triglobuline": "N/A",
            "nodular_area": "N/A"
            }).get_diagnosis()[0]


def test_adenoma():
    assert ADENOMA == \
           HyperthyroidismKnowledgeEngine({
            "tachycardia": "Sí",
            "weight_loss": "Sí",
            "sudoration_increase": "Sí",
            "inflamation": "No",
            "free_tsh": "Bajo",
            "free_t4": "Elevado",
            "free_t3": "N/A",
            "tyroidic_capture": "Elevado y nodular",
            "triglobuline": "N/A",
            "nodular_area": "Única"
            }).get_diagnosis()[0]


def test_goiter():
    assert GOITER == \
           HyperthyroidismKnowledgeEngine({
            "tachycardia": "Sí",
            "weight_loss": "Sí",
            "sudoration_increase": "Sí",
            "inflamation": "No",
            "free_tsh": "Bajo",
            "free_t4": "Elevado",
            "free_t3": "N/A",
            "tyroidic_capture": "Elevado y nodular",
            "triglobuline": "N/A",
            "nodular_area": "Múltiples"
            }).get_diagnosis()[0]


def test_low_free_t4_no_hyperthyroidism():
    assert NEGATIVE_DIAGNOSIS == \
           HyperthyroidismKnowledgeEngine({
            "tachycardia": "Sí",
            "weight_loss": "Sí",
            "sudoration_increase": "Sí",
            "inflamation": "No",
            "free_tsh": "Bajo",
            "free_t4": "Normal",
            "free_t3": "Bajo",
            "tyroidic_capture": "N/A",
            "triglobuline": "N/A",
            "nodular_area": "N/A"
            }).get_diagnosis()[0]


def test_low_free_t3_no_hyperthyroidism():
    assert NEGATIVE_DIAGNOSIS == \
           HyperthyroidismKnowledgeEngine({
            "tachycardia": "Sí",
            "weight_loss": "Sí",
            "sudoration_increase": "Sí",
            "inflamation": "No",
            "free_tsh": "Bajo",
            "free_t4": "Normal",
            "free_t3": "Bajo",
            "tyroidic_capture": "N/A",
            "triglobuline": "N/A",
            "nodular_area": "N/A"
            }).get_diagnosis()[0]


def test_no_tachycardia_no_hyperthyroidism():
    assert NEGATIVE_DIAGNOSIS == \
           HyperthyroidismKnowledgeEngine({
            "tachycardia": "Sí",
            "weight_loss": "Sí",
            "sudoration_increase": "Sí",
            "inflamation": "No",
            "free_tsh": "Elevado",
            "free_t4": "Normal",
            "free_t3": "Normal",
            "tyroidic_capture": "N/A",
            "triglobuline": "N/A",
            "nodular_area": "N/A"
            }).get_diagnosis()[0]


def test_normal_free_tsh_no_hyperthyroidism():
    assert NEGATIVE_DIAGNOSIS == \
           HyperthyroidismKnowledgeEngine({
            "tachycardia": "Sí",
            "weight_loss": "Sí",
            "sudoration_increase": "Sí",
            "inflamation": "No",
            "free_tsh": "Normal",
            "free_t4": "Normal",
            "free_t3": "Normal",
            "tyroidic_capture": "N/A",
            "triglobuline": "N/A",
            "nodular_area": "N/A"
            }).get_diagnosis()[0]
