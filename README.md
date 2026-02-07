# Home Assistant Configuration

This repository contains the Home Assistant configuration for a residential smart home. It is version-controlled to track changes, enable rollbacks, and serve as a backup for the entire home automation setup.

## Purpose

The primary goal of this configuration is to centralize and automate climate control across the house. It manages two independent but coordinated systems:

- **Multi-zone heating** -- per-room thermostats (both radiator and underfloor) with a weather-compensated heating curve for boiler flow temperature calculation. Scheduling and temperature setpoints are managed by [scheduler-component](https://github.com/nielsfaber/scheduler-component) with the [scheduler-card](https://github.com/nielsfaber/scheduler-card) frontend, which directly calls `climate.set_temperature` on each thermostat according to defined time schemes.
- **Heat recovery ventilation (HRV)** -- full integration with the ventilation unit over MQTT, exposing sensors (temperatures, airflow, CO2, humidity, filter status), operating mode selection, bypass control, and manual/automatic fan speed management.

Additional infrastructure includes Zigbee device support via ZHA with custom quirks, helper entities (heating curve parameters, boiler setpoint tracking), and an automation for underfloor heating pump control.

## Key Concepts

- **Heating curve** -- the boiler target flow temperature is calculated dynamically based on outdoor temperature, a configurable slope, and a shift parameter. This replaces a fixed setpoint and adapts to weather conditions automatically. A deviation alert fires when the calculated flow temperature diverges significantly from the last manually recorded boiler setpoint.
- **Scheduler integration** -- temperature scheduling is handled by [scheduler-component](https://github.com/nielsfaber/scheduler-component) (HACS custom component). Schedules are created and managed via the [scheduler-card](https://github.com/nielsfaber/scheduler-card) Lovelace card, which provides a visual time-scheme editor for each thermostat. This replaces the previous built-in schedule helpers, target temperature sensors, and the central sync automation.
- **Underfloor heating pump logic** -- the circulation pump activates only when at least one underfloor zone valve is open, with a startup delay to allow valves to open fully before the pump engages.
- **Fake temperature sensors** -- rooms without a physical temperature sensor (Office, Kitchen, Vestibule, Bathroom Ground Floor, Bathroom First Floor) use hardcoded placeholder values so that their `generic_thermostat` entities can function until real sensors are installed.

## Usage

This configuration is meant to be placed in the Home Assistant `config/` directory. Changes should be validated using the built-in configuration check before reloading or restarting Home Assistant.
