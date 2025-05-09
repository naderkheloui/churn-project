# app/schemas.py

from pydantic import BaseModel
from typing import Optional

class ChurnInput(BaseModel):
    Geolocalisation__Latitude__s: float
    Geolocalisation__Longitude__s: float
    pop_k1500m: float
    pop_k700m: float
    pop_k350m: float
    urban_dens: float
    nb_voisin_moins_200m: int
    nb_voisin_moins_300m: int
    nb_voisin_moins_2000m: int
    dist_voisin_1: float
    dist_voisin_2: float
    dist_voisin_3: float
    mois_actuel: int
    PUDO_delivery_m_1: int
    PUDO_delivery_m_2: int
    PUDO_delivery_m_3: int
    Dropoff_m_1: int
    Dropoff_m_2: int
    Dropoff_m_3: int
    nb_fermeture_annuel_pocket_dropoff: int
    nb_fermeture_annuel_deferred_dropoff: int
    nb_fermeture_annuel_deferred_delivery: int
    nb_fermeture_annuel_pocket_delivery: int
    nb_fermeture_annuel_delivery: int
    nb_fermeture_annuel_stuart_re_delivry: int
    nb_fermeture_annuel_fresh_delivery: int
    nb_fermeture_annuel_mail_delivery: int
    nb_fermeture_3_last_months_pocket_dropoff: int
    nb_fermeture_3_last_months_deferred_dropoff: int
    nb_fermeture_3_last_months_deferred_delivery: int
    nb_fermeture_3_last_months_pocket_delivery: int
    nb_fermeture_3_last_months_delivery: int
    nb_fermeture_3_last_months_stuart_re_delivry: int
    nb_fermeture_3_last_months_fresh_delivery: int
    nb_fermeture_3_last_months_mail_delivery: int
    dropoff_1_3: int
    dropoff_ANNUEL: int
    PUDO_delivery_1_3: int
    PUDO_delivery_ANNUEL: int