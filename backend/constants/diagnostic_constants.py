from constants.GOITER_TEXT import GOITER_TEXT

from constants.adenoma_text import ADENOMA_TEXT

from constants.exogen_hormones_hypertiroidism_text import YATROGEN_HYPERTHYROIDISM_TEXT

from constants.graves_illness_text import GRAVES_ILLNESS_TEXT

from constants.primary_hypertiroidism_text import PRIMARY_HYPERTHYROIDISM_TEXT

from constants.secondary_hyperthyroidism_text import SECONDARY_HYPERTHROIDISM_TEXT

from constants.subclinic_hypertyroidism_text import SUBCLINIC_HYPERTYROIDISM_TEXT

from constants.t3_hypertyroidism_text import T3_HYPERTYROIDISM_TEXT

NEGATIVE_DIAGNOSIS = "No tiene ningún tipo de hipertiroidismo."

SECONDARY_HYPERTHROIDISM = "Hipertiroidismo secundario"

SUBCLINIC_HYPERTHROIDISM = "Hipertiroidismo subclínico"

T3_HYPERTYHROIDISM = "Hipertiroidismo T3 (toxicosis)"

YATROGEN_HYPERTHYROIDISM = "Hipertiroidismo por hormonas exógenas"

PRIMARY_HYPERTHYROIDISM = "Hipertiroidismo primario"

GRAVES = "Hipertiroidismo por enfermedad de Graves"

ADENOMA = "Adenoma tóxico"

GOITER = "Bocio multinodular tóxico"

DIAGNOSTIC_TEXTS = {
    SUBCLINIC_HYPERTHROIDISM: SUBCLINIC_HYPERTYROIDISM_TEXT,
    SECONDARY_HYPERTHROIDISM: SECONDARY_HYPERTHROIDISM_TEXT,
    T3_HYPERTYHROIDISM: T3_HYPERTYROIDISM_TEXT,
    YATROGEN_HYPERTHYROIDISM: YATROGEN_HYPERTHYROIDISM_TEXT,
    PRIMARY_HYPERTHYROIDISM: PRIMARY_HYPERTHYROIDISM_TEXT,
    GRAVES: GRAVES_ILLNESS_TEXT,
    GOITER: GOITER_TEXT,
    ADENOMA: ADENOMA_TEXT
}
