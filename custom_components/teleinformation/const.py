"""Constants for teleinformation."""
# Base component constants
import logging

from homeassistant.components.sensor import STATE_CLASS_MEASUREMENT
from homeassistant.components.sensor import STATE_CLASS_TOTAL_INCREASING
from homeassistant.const import DEVICE_CLASS_CURRENT
from homeassistant.const import DEVICE_CLASS_ENERGY
from homeassistant.const import DEVICE_CLASS_POWER
from homeassistant.const import DEVICE_CLASS_VOLTAGE
from homeassistant.const import ELECTRIC_CURRENT_AMPERE
from homeassistant.const import ELECTRIC_POTENTIAL_VOLT
from homeassistant.const import ENERGY_WATT_HOUR
from homeassistant.const import POWER_VOLT_AMPERE
from homeassistant.const import POWER_WATT

NAME = "TeleInformation"
DOMAIN = "teleinformation"
VERSION = "0.1.0"

LOGGER = logging.getLogger(__package__)


# Platforms
SENSOR = "sensor"
PLATFORMS = [SENSOR]


# Configuration and options
CONF_DEVICE = "device"
CONF_COUNTERTYPE = "countertype"
CONF_MONITORED_VARIABLES = "monitoredvars"
CONF_TIMEOUT = "readtimeout"
DEFAULT_CONF_TIMEOUT = 30

ERROR_INVALID_DONGLE_PATH = "invaliddongle"
MANUAL_PATH_VALUE = "Custom path"

SIGNAL_RECEIVE_MESSAGE = "teleinformation.receive_message"
DATA_SERIAL_NUMBER = "teleinformation.sn"
DATA_DONGLE = "teleinformation.dongle"
DATA_DETECTED_VALUE = "teleinformation.detectedvalue"
SENSOR_HISTORICAL = "histo"
SENSOR_STANDARD = "standard"


SENSOR_TYPES = {
    "ADCO": [
        "Contrat",
        None,
        None,
        None,
        SENSOR_HISTORICAL,
    ],  # N° d’identification du compteur : ADCO(12 caractères)
    "OPTARIF": [
        "Option tarifaire",
        None,
        None,
        None,
        SENSOR_HISTORICAL,
    ],  # Option tarifaire(type d’abonnement) : OPTARIF(4 car.)
    "ISOUSC": [
        "Intensité souscrite",
        ELECTRIC_CURRENT_AMPERE,
        DEVICE_CLASS_CURRENT,
        None,
        SENSOR_HISTORICAL,
    ],  # Intensité souscrite : ISOUSC( 2 car.unité = ampères)
    "HCHC": [
        "Heures creuses",
        ENERGY_WATT_HOUR,
        DEVICE_CLASS_ENERGY,
        STATE_CLASS_TOTAL_INCREASING,
        SENSOR_HISTORICAL,
    ],  # Index heures creuses si option = heures creuses : HCHC( 9 car.unité = Wh)
    "HCHP": [
        "Heures pleines",
        ENERGY_WATT_HOUR,
        DEVICE_CLASS_ENERGY,
        STATE_CLASS_TOTAL_INCREASING,
        SENSOR_HISTORICAL,
    ],  # Index heures pleines si option = heures creuses : HCHP( 9 car.unité = Wh)
    "PTEC": [
        "Période Tarifaire",
        None,
        None,
        None,
        SENSOR_HISTORICAL,
    ],  # Période tarifaire en cours : PTEC( 4 car.)
    "IINST": [
        "Intensite instantanee",
        ELECTRIC_CURRENT_AMPERE,
        DEVICE_CLASS_CURRENT,
        STATE_CLASS_MEASUREMENT,
        SENSOR_HISTORICAL,
    ],  # Intensité instantanée : IINST( 3 car.unité = ampères)
    "IINST1": [
        "Intensite instantanee phase 1",
        ELECTRIC_CURRENT_AMPERE,
        DEVICE_CLASS_CURRENT,
        STATE_CLASS_MEASUREMENT,
        SENSOR_HISTORICAL,
    ],  # Intensité instantanée : IINST( 3 car.unité = ampères)
    "IINST2": [
        "Intensite instantanee phase 2",
        ELECTRIC_CURRENT_AMPERE,
        DEVICE_CLASS_CURRENT,
        STATE_CLASS_MEASUREMENT,
        SENSOR_HISTORICAL,
    ],  # Intensité instantanée : IINST( 3 car.unité = ampères)
    "IINST3": [
        "Intensite instantanee phase 3",
        ELECTRIC_CURRENT_AMPERE,
        DEVICE_CLASS_CURRENT,
        STATE_CLASS_MEASUREMENT,
        SENSOR_HISTORICAL,
    ],  # Intensité instantanée : IINST( 3 car.unité = ampères)
    "IMAX": [
        "Intensite max",
        ELECTRIC_CURRENT_AMPERE,
        DEVICE_CLASS_CURRENT,
        None,
        SENSOR_HISTORICAL,
    ],  # Intensité maximale : IMAX( 3 car.unité = ampères)
    "IMAX1": [
        "Intensite max phase 1",
        ELECTRIC_CURRENT_AMPERE,
        DEVICE_CLASS_CURRENT,
        None,
        SENSOR_HISTORICAL,
    ],  # Intensité maximale : IMAX( 3 car.unité = ampères)
    "IMAX2": [
        "Intensite max phase 2",
        ELECTRIC_CURRENT_AMPERE,
        DEVICE_CLASS_CURRENT,
        None,
        SENSOR_HISTORICAL,
    ],  # Intensité maximale : IMAX( 3 car.unité = ampères)
    "IMAX3": [
        "Intensite max phase 3",
        ELECTRIC_CURRENT_AMPERE,
        DEVICE_CLASS_CURRENT,
        None,
        SENSOR_HISTORICAL,
    ],  # Intensité maximale : IMAX( 3 car.unité = ampères)
    "PMAX": [
        "Puissance maximale triphasée atteinte",
        POWER_WATT,
        DEVICE_CLASS_POWER,
        None,
        SENSOR_HISTORICAL,
    ],  # Puissance apparente : PAPP( 5 car.unité = Volt.ampères)
    "PAPP": [
        "Puissance apparente",
        POWER_VOLT_AMPERE,
        DEVICE_CLASS_POWER,
        STATE_CLASS_MEASUREMENT,
        SENSOR_HISTORICAL,
    ],  # Puissance apparente : PAPP( 5 car.unité = Volt.ampères)
    "HHPHC": [
        "Groupe horaire",
        None,
        None,
        None,
        SENSOR_HISTORICAL,
    ],  # Groupe horaire si option = heures creuses ou tempo : HHPHC(1 car.)
    "MOTDETAT": [
        "Mot d etat",
        None,
        None,
        None,
        SENSOR_HISTORICAL,
    ],  # Mot d’état(autocontrôle) : MOTDETAT(6 car.)
    "BASE": [
        "Base",
        ENERGY_WATT_HOUR,
        DEVICE_CLASS_ENERGY,
        STATE_CLASS_TOTAL_INCREASING,
        SENSOR_HISTORICAL,
    ],  # Index si option = base : BASE( 9 car.unité = Wh)
    "EJPHN": [
        "EJP Heures normales",
        ENERGY_WATT_HOUR,
        DEVICE_CLASS_ENERGY,
        None,
        SENSOR_HISTORICAL,
    ],  # Index heures normales si option = EJP : EJP HN( 9 car.unité = Wh)</para>
    "EJPHPM": [
        "EJP Heures de pointe",
        ENERGY_WATT_HOUR,
        DEVICE_CLASS_ENERGY,
        None,
        SENSOR_HISTORICAL,
    ],  # Index heures de pointe mobile si option = EJP : EJP HPM( 9 car.unité = Wh)</para>
    "PEJP": [
        "EJP Préavis",
        ENERGY_WATT_HOUR,
        DEVICE_CLASS_ENERGY,
        None,
        SENSOR_HISTORICAL,
    ],  # Préavis EJP si option = EJP : PEJP( 2 car.) 30mn avant période EJP</para>
    "BBRHCJB": [
        "Tempo heures bleues creuses",
        ENERGY_WATT_HOUR,
        DEVICE_CLASS_ENERGY,
        None,
        SENSOR_HISTORICAL,
    ],  # Index heures creuses jours bleus si option = tempo : BBR HC JB( 9 car.unité = Wh)</para>
    "BBRHPJB": [
        "Tempo heures bleues pleines",
        ENERGY_WATT_HOUR,
        DEVICE_CLASS_ENERGY,
        None,
        SENSOR_HISTORICAL,
    ],  # Index heures pleines jours bleus si option = tempo : BBR HP JB( 9 car.unité = Wh)</para>
    "BBRHCJW": [
        "Tempo heures blanches creuses",
        ENERGY_WATT_HOUR,
        DEVICE_CLASS_ENERGY,
        None,
        SENSOR_HISTORICAL,
    ],  # Index heures creuses jours blancs si option = tempo : BBR HC JW( 9 car.unité = Wh)</para>
    "BBRHPJW": [
        "Tempo heures blanches pleines",
        ENERGY_WATT_HOUR,
        DEVICE_CLASS_ENERGY,
        None,
        SENSOR_HISTORICAL,
    ],  # Index heures pleines jours blancs si option = tempo : BBR HP JW( 9 car.unité = Wh)</para>
    "BBRHCJR": [
        "Tempo heures rouges creuses",
        ENERGY_WATT_HOUR,
        DEVICE_CLASS_ENERGY,
        None,
        SENSOR_HISTORICAL,
    ],  # Index heures creuses jours rouges si option = tempo : BBR HC JR( 9 car.unité = Wh)</para>
    "BBRHPJR": [
        "Tempo heures rouges pleines",
        ENERGY_WATT_HOUR,
        DEVICE_CLASS_ENERGY,
        None,
        SENSOR_HISTORICAL,
    ],  # Index heures pleines jours rouges si option = tempo : BBR HP JR( 9 car.unité = Wh)</para>
    "DEMAIN": [
        "Tempo couleur demain",
        None,
        None,
        None,
        SENSOR_HISTORICAL,
    ],  # Couleur du lendemain si option = tempo : DEMAIN</para>
    "ADPS": [
        "Dépassement Puissance",
        None,
        None,
        None,
        SENSOR_HISTORICAL,
    ],  # Avertissement de dépassement de puissance souscrite : ADPS( 3 car.unité = ampères) (message émis uniquement en cas de dépassement effectif, dans ce cas il est immédiat)</para>
    "PPOT": [
        "Présence des potentiels ",
        None,
        None,
        None,
        SENSOR_HISTORICAL,
    ],  # Présence des potentiels : PPOT ( 2 car.) </para>
    "ADSC": [
        "Contrat",
        None,
        None,
        None,
        SENSOR_STANDARD,
    ],  # N° d’identification du compteur : ADCO(12 caractères)
    "NGTF": [
        "Nom du calendrier tarifaire fournisseur",
        None,
        None,
        None,
        SENSOR_STANDARD,
    ],  # BASE, HPHC, etc équivalent OPTARIF
    "LTARF": [
        "Libellé tarif fournisseur en cours",
        None,
        None,
        None,
        SENSOR_STANDARD,
    ],  # BASE, HPHC, etc équivalent PTEC
    "EAST": [
        "Energie active soutirée totale",
        ENERGY_WATT_HOUR,
        DEVICE_CLASS_ENERGY,
        STATE_CLASS_TOTAL_INCREASING,
        SENSOR_STANDARD,
    ],  # Total de tous les compteurs soutirage
    "EASF01": [
        "Energie active soutirée Fournisseur, index 01",
        ENERGY_WATT_HOUR,
        DEVICE_CLASS_ENERGY,
        STATE_CLASS_TOTAL_INCREASING,
        SENSOR_STANDARD,
    ],  # Equivalent BASE ou CREUSE
    "EASF02": [
        "Energie active soutirée Fournisseur, index 02",
        ENERGY_WATT_HOUR,
        DEVICE_CLASS_ENERGY,
        STATE_CLASS_TOTAL_INCREASING,
        SENSOR_STANDARD,
    ],  # Equivalent BASE ou CREUSE
    "EAIT": [
        "Energie active injectée totale",
        ENERGY_WATT_HOUR,
        DEVICE_CLASS_ENERGY,
        STATE_CLASS_TOTAL_INCREASING,
        SENSOR_STANDARD,
    ],  # Total de tous les compteurs injection
    "IRMS1": [
        "Courant efficace, phase 1",
        ELECTRIC_CURRENT_AMPERE,
        DEVICE_CLASS_CURRENT,
        STATE_CLASS_MEASUREMENT,
        SENSOR_STANDARD,
    ],
    "IRMS2": [
        "Courant efficace, phase 2",
        ELECTRIC_CURRENT_AMPERE,
        DEVICE_CLASS_CURRENT,
        STATE_CLASS_MEASUREMENT,
        SENSOR_STANDARD,
    ],
    "IRMS3": [
        "Courant efficace, phase 3",
        ELECTRIC_CURRENT_AMPERE,
        DEVICE_CLASS_CURRENT,
        STATE_CLASS_MEASUREMENT,
        SENSOR_STANDARD,
    ],
    "URMS1": [
        "Tension efficace, phase 1",
        ELECTRIC_POTENTIAL_VOLT,
        DEVICE_CLASS_VOLTAGE,
        STATE_CLASS_MEASUREMENT,
        SENSOR_STANDARD,
    ],
    "URMS2": [
        "Tension efficace, phase 2",
        ELECTRIC_POTENTIAL_VOLT,
        DEVICE_CLASS_VOLTAGE,
        STATE_CLASS_MEASUREMENT,
        SENSOR_STANDARD,
    ],
    "URMS3": [
        "Tension efficace, phase 3",
        ELECTRIC_POTENTIAL_VOLT,
        DEVICE_CLASS_VOLTAGE,
        STATE_CLASS_MEASUREMENT,
        SENSOR_STANDARD,
    ],
    "PREF": [
        "Puissance app. de référence",
        "kVA",
        DEVICE_CLASS_POWER,
        STATE_CLASS_MEASUREMENT,
        SENSOR_STANDARD,
    ],
    "PCOUP": [
        "Puissance app. de coupure",
        "kVA",
        DEVICE_CLASS_POWER,
        STATE_CLASS_MEASUREMENT,
        SENSOR_STANDARD,
    ],
    "SINSTS": [
        "Puissance app. Instantanée soutirée",
        POWER_VOLT_AMPERE,
        DEVICE_CLASS_POWER,
        STATE_CLASS_MEASUREMENT,
        SENSOR_STANDARD,
    ],
    "SINSTS1": [
        "Puissance app. Instantanée soutirée phase 1",
        POWER_VOLT_AMPERE,
        DEVICE_CLASS_POWER,
        STATE_CLASS_MEASUREMENT,
        SENSOR_STANDARD,
    ],
    "SINSTS2": [
        "Puissance app. Instantanée soutirée phase 2",
        POWER_VOLT_AMPERE,
        DEVICE_CLASS_POWER,
        STATE_CLASS_MEASUREMENT,
        SENSOR_STANDARD,
    ],
    "SINSTS3": [
        "Puissance app. Instantanée soutirée phase 3",
        POWER_VOLT_AMPERE,
        DEVICE_CLASS_POWER,
        STATE_CLASS_MEASUREMENT,
        SENSOR_STANDARD,
    ],
    "SINSTI": [
        "Puissance app. Instantanée injectée",
        POWER_VOLT_AMPERE,
        DEVICE_CLASS_POWER,
        STATE_CLASS_MEASUREMENT,
        SENSOR_STANDARD,
    ],
    "SMAXSN": [
        "Puissance app. max. soutirée n",
        POWER_VOLT_AMPERE,
        DEVICE_CLASS_POWER,
        None,
        SENSOR_STANDARD,
    ],
    "SMAXSN1": [
        "Puissance app. max. soutirée n phase 1",
        POWER_VOLT_AMPERE,
        DEVICE_CLASS_POWER,
        None,
        SENSOR_STANDARD,
    ],
    "SMAXSN2": [
        "Puissance app. max. soutirée n phase 2",
        POWER_VOLT_AMPERE,
        DEVICE_CLASS_POWER,
        None,
        SENSOR_STANDARD,
    ],
    "SMAXSN3": [
        "Puissance app. max. soutirée n phase 3",
        POWER_VOLT_AMPERE,
        DEVICE_CLASS_POWER,
        None,
        SENSOR_STANDARD,
    ],
    "MSG1": ["Message court", None, None, None, SENSOR_STANDARD],
    "MSG2": ["Message Ultra court", None, None, None, SENSOR_STANDARD],
}


SENSOR_TYPES_ALL = [sensor_id for sensor_id, _ in SENSOR_TYPES.items()]

SENSOR_TYPES_HISTO = {
    sensor_id
    for sensor_id, val in SENSOR_TYPES.items()
    if (val[4] == SENSOR_HISTORICAL)
}
SENSOR_TYPES_STANDARD = {
    sensor_id: val
    for sensor_id, val in SENSOR_TYPES.items()
    if (val[4] == SENSOR_STANDARD)
}

SENSOR_RECOMMENDED_DEFAULT = [
    "ADCO",
    "ISOUSC",
    "HPHP",
    "HPHC",
    "BASE",
    "PTEC",
    "IINST",
    "IINST1",
    "IINST2",
    "IINST",
    "PAPP",
    "ADSC",
    "LTARF",
    "EASF01",
    "EASF02",
    "EAIT",
    "IRMS1",
    "IRMS2",
    "IRMS3",
    "URMS1",
    "URMS2",
    "URMS3",
    "PCOUP",
    "SINSTS",
    "SINSTS1",
    "SINSTS2",
    "SINSTS3",
    "SINSTI",
    "MSG1",
    "MSG2",
]
