"""Constants for teleinformation."""
# Base component constants
from homeassistant.const import (
    DEVICE_CLASS_CURRENT,
    DEVICE_CLASS_ENERGY,
    DEVICE_CLASS_POWER,
    ELECTRICAL_CURRENT_AMPERE,
    ENERGY_WATT_HOUR,
    POWER_WATT,
)
import logging

NAME = "TeleInformation"
DOMAIN = "teleinformation"
VERSION = "0.0.1"

LOGGER = logging.getLogger(__package__)


# Platforms
SENSOR = "sensor"
PLATFORMS = [SENSOR]


# Configuration and options
CONF_DEVICE = "device"
CONF_MONITORED_VARIABLES = "monitoredvars"
CONF_TIMEOUT = "readtimeout"
DEFAULT_CONF_TIMEOUT = 5

ERROR_INVALID_DONGLE_PATH = "invaliddongle"
MANUAL_PATH_VALUE = "Custom path"

SIGNAL_RECEIVE_MESSAGE = "teleinformation.receive_message"
DATA_SERIAL_NUMBER = "teleinformation.sn"
DATA_DONGLE = "teleinformation.dongle"


SENSOR_TYPES = {
    "ADCO": [
        "Contrat",
        None,
        None,
    ],  # N° d’identification du compteur : ADCO(12 caractères)
    "OPTARIF": [
        "Option tarifaire",
        None,
        None,
    ],  # Option tarifaire(type d’abonnement) : OPTARIF(4 car.)
    "ISOUSC": [
        "Intensité souscrite",
        ELECTRICAL_CURRENT_AMPERE,
        DEVICE_CLASS_CURRENT,
    ],  # Intensité souscrite : ISOUSC( 2 car.unité = ampères)
    "HCHC": [
        "Heures creuses",
        ENERGY_WATT_HOUR,
        DEVICE_CLASS_ENERGY,
    ],  # Index heures creuses si option = heures creuses : HCHC( 9 car.unité = Wh)
    "HCHP": [
        "Heures pleines",
        ENERGY_WATT_HOUR,
        DEVICE_CLASS_ENERGY,
    ],  # Index heures pleines si option = heures creuses : HCHP( 9 car.unité = Wh)
    "PTEC": [
        "Période Tarifaire",
        None,
        None,
    ],  # Période tarifaire en cours : PTEC( 4 car.)
    "IINST": [
        "Intensite instantanee",
        ELECTRICAL_CURRENT_AMPERE,
        DEVICE_CLASS_CURRENT,
    ],  # Intensité instantanée : IINST( 3 car.unité = ampères)
    "IINST1": [
        "Intensite instantanee phase 1",
        ELECTRICAL_CURRENT_AMPERE,
        DEVICE_CLASS_CURRENT,
    ],  # Intensité instantanée : IINST( 3 car.unité = ampères)
    "IINST2": [
        "Intensite instantanee phase 2",
        ELECTRICAL_CURRENT_AMPERE,
        DEVICE_CLASS_CURRENT,
    ],  # Intensité instantanée : IINST( 3 car.unité = ampères)
    "IINST3": [
        "Intensite instantanee phase 3",
        ELECTRICAL_CURRENT_AMPERE,
        DEVICE_CLASS_CURRENT,
    ],  # Intensité instantanée : IINST( 3 car.unité = ampères)
    "IMAX": [
        "Intensite max",
        ELECTRICAL_CURRENT_AMPERE,
        DEVICE_CLASS_CURRENT,
    ],  # Intensité maximale : IMAX( 3 car.unité = ampères)
    "IMAX1": [
        "Intensite max phase 1",
        ELECTRICAL_CURRENT_AMPERE,
        DEVICE_CLASS_CURRENT,
    ],  # Intensité maximale : IMAX( 3 car.unité = ampères)
    "IMAX2": [
        "Intensite max phase 2",
        ELECTRICAL_CURRENT_AMPERE,
        DEVICE_CLASS_CURRENT,
    ],  # Intensité maximale : IMAX( 3 car.unité = ampères)
    "IMAX3": [
        "Intensite max phase 3",
        ELECTRICAL_CURRENT_AMPERE,
        DEVICE_CLASS_CURRENT,
    ],  # Intensité maximale : IMAX( 3 car.unité = ampères)
    "PMAX": [
        "Puissance maximale triphasée atteinte",
        POWER_WATT,
        DEVICE_CLASS_POWER,
    ],  # Puissance apparente : PAPP( 5 car.unité = Volt.ampères)
    "PAPP": [
        "Puissance apparente",
        "VA",
        DEVICE_CLASS_POWER,
    ],  # Puissance apparente : PAPP( 5 car.unité = Volt.ampères)
    "HHPHC": [
        "Groupe horaire",
        None,
        None,
    ],  # Groupe horaire si option = heures creuses ou tempo : HHPHC(1 car.)
    "MOTDETAT": [
        "Mot d etat",
        None,
        None,
    ],  # Mot d’état(autocontrôle) : MOTDETAT(6 car.)
    "BASE": [
        "Base",
        ENERGY_WATT_HOUR,
        DEVICE_CLASS_ENERGY,
    ],  # Index si option = base : BASE( 9 car.unité = Wh)
    "EJPHN": [
        "EJP Heures normales",
        ENERGY_WATT_HOUR,
        DEVICE_CLASS_ENERGY,
    ],  # Index heures normales si option = EJP : EJP HN( 9 car.unité = Wh)</para>
    "EJPHPM": [
        "EJP Heures de pointe",
        ENERGY_WATT_HOUR,
        DEVICE_CLASS_ENERGY,
    ],  # Index heures de pointe mobile si option = EJP : EJP HPM( 9 car.unité = Wh)</para>
    "PEJP": [
        "EJP Préavis",
        ENERGY_WATT_HOUR,
        DEVICE_CLASS_ENERGY,
    ],  # Préavis EJP si option = EJP : PEJP( 2 car.) 30mn avant période EJP</para>
    "BBRHCJB": [
        "Tempo heures bleues creuses",
        ENERGY_WATT_HOUR,
        DEVICE_CLASS_ENERGY,
    ],  # Index heures creuses jours bleus si option = tempo : BBR HC JB( 9 car.unité = Wh)</para>
    "BBRHPJB": [
        "Tempo heures bleues pleines",
        ENERGY_WATT_HOUR,
        DEVICE_CLASS_ENERGY,
    ],  # Index heures pleines jours bleus si option = tempo : BBR HP JB( 9 car.unité = Wh)</para>
    "BBRHCJW": [
        "Tempo heures blanches creuses",
        ENERGY_WATT_HOUR,
        DEVICE_CLASS_ENERGY,
    ],  # Index heures creuses jours blancs si option = tempo : BBR HC JW( 9 car.unité = Wh)</para>
    "BBRHPJW": [
        "Tempo heures blanches pleines",
        ENERGY_WATT_HOUR,
        DEVICE_CLASS_ENERGY,
    ],  # Index heures pleines jours blancs si option = tempo : BBR HP JW( 9 car.unité = Wh)</para>
    "BBRHCJR": [
        "Tempo heures rouges creuses",
        ENERGY_WATT_HOUR,
        DEVICE_CLASS_ENERGY,
    ],  # Index heures creuses jours rouges si option = tempo : BBR HC JR( 9 car.unité = Wh)</para>
    "BBRHPJR": [
        "Tempo heures rouges pleines",
        ENERGY_WATT_HOUR,
        DEVICE_CLASS_ENERGY,
    ],  # Index heures pleines jours rouges si option = tempo : BBR HP JR( 9 car.unité = Wh)</para>
    "DEMAIN": [
        "Tempo couleur demain",
        None,
        None,
    ],  # Couleur du lendemain si option = tempo : DEMAIN</para>
    "ADPS": [
        "Dépassement Puissance",
        None,
        None,
    ],  # Avertissement de dépassement de puissance souscrite : ADPS( 3 car.unité = ampères) (message émis uniquement en cas de dépassement effectif, dans ce cas il est immédiat)</para>
    "PPOT": [
        "Présence des potentiels ",
        None,
        None,
    ],  # Présence des potentiels : PPOT ( 2 car.) </para>
}

SENSOR_TYPES_DEFAULT = [sensor_id for sensor_id, _ in SENSOR_TYPES.items()]
