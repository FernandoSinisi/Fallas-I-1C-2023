from experta import *

from constants.diagnostic_constants import (SECONDARY_HYPERTHROIDISM, SUBCLINIC_HYPERTHROIDISM,
                                            T3_HYPERTYHROIDISM, YATROGEN_HYPERTHYROIDISM,
                                            PRIMARY_HYPERTHYROIDISM, GRAVES, ADENOMA, GOITER,
                                            NEGATIVE_DIAGNOSIS)


class Diagnosis(Fact):
    pass


class HyperthyroidismKnowledgeEngine(KnowledgeEngine):
    def __init__(self, answers):
        super().__init__()

        self.reset()

        self.text = "Faltan preguntas"

        self.current_tag = "inflamation"

        self.diagnosis = self.declare(
            Diagnosis(symptoms="No",
                      checked="No",
                      inflamation=answers.get("inflamation", "N/A"),
                      tachycardia=answers.get("tachycardia", "N/A"),
                      weight_loss=answers.get("weight_loss", "N/A"),
                      sudoration_increase=answers.get("sudoration_increase", "N/A"),
                      free_tsh=answers.get("free_tsh", "N/A"),
                      free_t4=answers.get("free_t4", "N/A"),
                      free_t3=answers.get("free_t3", "N/A"),
                      tyroidic_capture=answers.get("tyroidic_capture", "N/A"),
                      triglobuline=answers.get("triglobuline", "N/A"),
                      nodular_area=answers.get("nodular_area", "N/A")
                      ))

        if (answers.get("inflamation", "N/A") == "Sí") \
                or (answers.get("tachycardia", "N/A") == "Sí"
                    and answers.get("weight_loss", "N/A") == "Sí"
                    and answers.get("sudoration_increase", "N/A") == "Sí"):
            self.current_tag = "free_tsh"

            self.text = "No tiene síntomas"

            self.modify(self.diagnosis,
                        symptoms="Sí",
                        checked="Sí")

        self.run()

    @Rule(AND(
            Diagnosis(inflamation="Sí"),
            Diagnosis(inflamation="N/A"),
            Diagnosis(tachycardia="N/A")
        )
    )
    def has_inflamation(self):
        self.current_tag = "free_tsh"

    @Rule(AND(
            Diagnosis(inflamation="No"),
            Diagnosis(tachycardia="Sí"),
            Diagnosis(weight_loss="N/A")
        )
    )
    def has_tachycardia(self):
        self.current_tag = "weight_loss"

    @Rule(AND(
            Diagnosis(inflamation="No"),
            Diagnosis(tachycardia="Sí"),
            Diagnosis(weight_loss="Sí"),
            Diagnosis(sudoration_increase="N/A")
        )
    )
    def has_wight_loss(self):
        self.current_tag = "sudoration_increase"

    @Rule(
        AND(
            Diagnosis(symptoms="No"),
            Diagnosis(inflamation="No"),
            OR(
                AND(
                    Diagnosis(tachycardia="No")
                ),
                AND(
                    Diagnosis(tachycardia="Sí"),
                    Diagnosis(weight_loss="No")
                ),
                AND(
                    Diagnosis(tachycardia="Sí"),
                    Diagnosis(weight_loss="Sí"),
                    Diagnosis(sudoration_increase="No")
                ),
            )
        )
    )
    def does_not_have_symptoms(self):
        self.current_tag = ""

        self.text = "No tiene síntomas"

    @Rule(AND(
            Diagnosis(symptoms="No"),
            Diagnosis(inflamation="No"),
            Diagnosis(tachycardia="N/A")
        )
    )
    def does_not_have_inflamation(self):
        self.current_tag = "tachycardia"

    @Rule(AND(
            NOT(
                Diagnosis(free_tsh="Normal"),
            ),
            NOT(
                Diagnosis(free_tsh="N/A"),
            ),
            Diagnosis(free_t4="N/A")
        )
    )
    def compatible_free_tsh(self):
        self.current_tag = "free_t4"

    @Rule(Diagnosis(free_tsh="Bajo"),
          Diagnosis(free_t4="Elevado"),
          Diagnosis(tyroidic_capture="N/A")
    )
    def compatible_t4(self):
        self.current_tag = "tyroidic_capture"

    @Rule(Diagnosis(free_tsh="Bajo"),
          Diagnosis(free_t4="Normal")
    )
    def compatible_t4_2(self):
        self.current_tag = "free_t3"

    @Rule(Diagnosis(free_tsh="Bajo"),
          Diagnosis(free_t4="Elevado"),
          Diagnosis(tyroidic_capture="Bajo")
    )
    def tyroidic_capture_compatible(self):
        self.current_tag = "triglobuline"

    @Rule(Diagnosis(free_tsh="Bajo"),
          Diagnosis(free_t4="Elevado"),
          Diagnosis(tyroidic_capture="Elevado y nodular")
    )
    def tyroidic_capture_compatible_2(self):
        self.current_tag = "nodular_area"

    @Rule(AND(
        Diagnosis(symptoms="Sí"),
        Diagnosis(free_tsh="Elevado"),
        Diagnosis(free_t4="Elevado")
    ))
    def secondary_hyperthyroidism(self):
        self.answer = SECONDARY_HYPERTHROIDISM

    @Rule(AND(
        Diagnosis(symptoms="Sí"),
        Diagnosis(free_tsh="Bajo"),
        Diagnosis(free_t4="Normal"),
        Diagnosis(free_t3="Normal")
    ))
    def subclinic_hyperthyroidism(self):
        self.answer = SUBCLINIC_HYPERTHROIDISM

    @Rule(AND(
        Diagnosis(symptoms="Sí"),
        Diagnosis(free_tsh="Bajo"),
        Diagnosis(free_t4="Normal"),
        Diagnosis(free_t3="Elevado")
    ))
    def t3_hyperthyroidism_hyperthyroidism(self):
        self.answer = T3_HYPERTYHROIDISM

    @Rule(AND(
        Diagnosis(symptoms="Sí"),
        Diagnosis(free_tsh="Bajo"),
        Diagnosis(free_t4="Elevado"),
        Diagnosis(tyroidic_capture="Bajo"),
        Diagnosis(triglobuline="Bajo")
    ))
    def exogen_hormones_hyperthyroidism(self):
        self.answer = YATROGEN_HYPERTHYROIDISM

    @Rule(AND(
        Diagnosis(symptoms="Sí"),
        Diagnosis(free_tsh="Bajo"),
        Diagnosis(free_t4="Elevado"),
        Diagnosis(tyroidic_capture="Bajo"),
        Diagnosis(triglobuline="Elevado")
    ))
    def primary_hyperthyroidism(self):
        self.answer = PRIMARY_HYPERTHYROIDISM

    @Rule(AND(
        Diagnosis(symptoms="Sí"),
        Diagnosis(free_tsh="Bajo"),
        Diagnosis(free_t4="Elevado"),
        Diagnosis(tyroidic_capture="Elevado y difuso")
    ))
    def graves(self):
        self.answer = GRAVES

    @Rule(AND(
        Diagnosis(symptoms="Sí"),
        Diagnosis(free_tsh="Bajo"),
        Diagnosis(free_t4="Elevado"),
        Diagnosis(tyroidic_capture="Elevado y nodular"),
        Diagnosis(nodular_area="Única")
    ))
    def adenoma(self):
        self.answer = ADENOMA

    @Rule(AND(
        Diagnosis(symptoms="Sí"),
        Diagnosis(free_tsh="Bajo"),
        Diagnosis(free_t4="Elevado"),
        Diagnosis(tyroidic_capture="Elevado y nodular"),
        Diagnosis(nodular_area="Múltiples")
    ))
    def goiter(self):
        self.answer = GOITER

    @Rule(OR(
        AND(
            Diagnosis(symptoms="No"),
            Diagnosis(checked="Sí")
        ),
        AND(
            Diagnosis(symptoms="Sí"),
            Diagnosis(free_tsh="Normal")
        ),
        AND(
            Diagnosis(symptoms="Sí"),
            Diagnosis(free_tsh="Elevado"),
            OR(
                Diagnosis(free_t4="Normal"),
                Diagnosis(free_t4="Bajo")
            )
        ),
        AND(
            Diagnosis(symptoms="Sí"),
            Diagnosis(free_tsh="Bajo"),
            OR(
                Diagnosis(free_t4="Bajo"),
                AND(
                    Diagnosis(free_t3="Bajo"),
                    Diagnosis(free_t4="Normal"),
                    Diagnosis(symptoms="Sí")
                )
            )
        ),
    ))
    def no_hyperthyroidism(self):
        self.answer = NEGATIVE_DIAGNOSIS

    def get_diagnosis(self):
        try:
            return self.answer, ""

        except:
            return self.text, self.current_tag
