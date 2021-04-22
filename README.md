# teleinformation

[![GitHub Release][releases-shield]][releases]
[![GitHub Activity][commits-shield]][commits]
[![License][license-shield]](LICENSE)

[![pre-commit][pre-commit-shield]][pre-commit]
[![Black][black-shield]][black]

[![hacs][hacsbadge]][hacs]
[![Project Maintenance][maintenance-shield]][user_profile]


**This component will set up the following platforms.**

| Platform        | Description                                                               |
| --------------- | ------------------------------------------------------------------------- |
| `sensor`        | Show info from teleinformation serial.                                    |

![example][logo]

## Installation

1. Using the tool of choice open the directory (folder) for your HA configuration (where you find `configuration.yaml`).
2. If you do not have a `custom_components` directory (folder) there, you need to create it.
3. In the `custom_components` directory (folder) create a new folder called `teleinformation`.
4. Download _all_ the files from the `custom_components/teleinformation/` directory (folder) in this repository.
5. Place the files you downloaded in the new directory (folder) you created.
6. Restart Home Assistant
7. In the HA UI go to "Configuration" -> "Integrations" click "+" and search for "teleinformation"

Using your HA configuration directory (folder) as a starting point you should now also have this:

```text
custom_components/teleinformation/translations/en.json
custom_components/teleinformation/translations/fr.json
custom_components/teleinformation/__init__.py
custom_components/teleinformation/config_flow.py
custom_components/teleinformation/const.py
custom_components/teleinformation/dongle.py
custom_components/teleinformation/manifest.json
custom_components/teleinformation/sensor.py
```

## Configuration is done in the UI

<!---->

## Contributions are welcome!

If you want to contribute to this please read the [Contribution guidelines](CONTRIBUTING.md)

## Credits

This project was generated from [@oncleben31](https://github.com/oncleben31)'s [Home Assistant Custom Component Cookiecutter](https://github.com/oncleben31/cookiecutter-homeassistant-custom-component) template.

Code template was mainly taken from [@Ludeeus](https://github.com/ludeeus)'s [integration_blueprint][integration_blueprint] template

---

[integration_blueprint]: https://github.com/custom-components/integration_blueprint
[black]: https://github.com/psf/black
[black-shield]: https://img.shields.io/badge/
[commits-shield]: https://img.shields.io/github/commit-activity/y/poppypop/integration_teleinformation.svg?style=for-the-badge
[commits]: https://github.com/poppypop/integration_teleinformation/commits/main
[hacs]: https://hacs.xyz
[hacsbadge]: https://img.shields.io/badge/HACS-Custom-orange.svg?style=for-the-badge
[logo]: Logo-EDF-500x407.jpg
[forum-shield]: https://img.shields.io/badge/community-forum-brightgreen.svg?style=for-the-badge
[forum]: https://community.home-assistant.io/
[license]: https://github.com/poppypop/integration_teleinformation/blob/main/LICENSE
[license-shield]: https://img.shields.io/github/license/poppypop/integration_teleinformation.svg?style=for-the-badge
[maintenance-shield]: https://img.shields.io/badge/maintainer-%40poppypop-blue.svg?style=for-the-badge
[pre-commit]: https://github.com/pre-commit/pre-commit
[pre-commit-shield]: https://img.shields.io/badge/pre--commit-enabled-brightgreen?style=for-the-badge
[releases-shield]: https://img.shields.io/github/release/poppypop/integration_teleinformation.svg?style=for-the-badge
[releases]: https://github.com/poppypop/integration_teleinformation/releases
[user_profile]: https://github.com/poppypop
