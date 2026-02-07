# Home Assistant Configuration

This repository contains the Home Assistant configuration for a residential smart home. It is version-controlled to track changes, enable rollbacks, and serve as a backup for the entire home automation setup.

## Purpose

The primary goal of this configuration is to centralize and automate climate control across the house. It manages two independent but coordinated systems:

- **Multi-zone heating** -- per-room thermostats (both radiator and underfloor) with schedule-driven comfort and eco temperature profiles, an automatic mode that follows defined schedules, and a weather-compensated heating curve for boiler flow temperature calculation.
- **Heat recovery ventilation (HRV)** -- full integration with the ventilation unit over MQTT, exposing sensors (temperatures, airflow, CO2, humidity, filter status), operating mode selection, bypass control, and manual/automatic fan speed management.

Additional infrastructure includes Zigbee device support via ZHA with custom quirks, and various helper entities and automations that tie the systems together.

## Key Concepts

- **Heating curve** -- the boiler target flow temperature is calculated dynamically based on outdoor temperature, a configurable slope, and a shift parameter. This replaces a fixed setpoint and adapts to weather conditions automatically.
- **Schedule-based automation** -- each room has a comfort schedule. When automatic heating mode is enabled, thermostats follow these schedules without manual intervention. The mode can be toggled off for full manual control.
- **Underfloor heating pump logic** -- the circulation pump activates only when at least one underfloor zone valve is open, with a startup delay to allow valves to open fully before the pump engages.

## Usage

This configuration is meant to be placed in the Home Assistant `config/` directory. Changes should be validated using the built-in configuration check before reloading or restarting Home Assistant.
