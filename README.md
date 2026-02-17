# Home Assistant Configuration

This repository contains the Home Assistant configuration for a residential smart home system focused on climate control and automation.

## Overview

This configuration implements a comprehensive home automation system with emphasis on:

- **Multi-zone heating system** with individual room temperature control
- **Weather-compensated heating curve** for automatic boiler temperature optimization
- **Heat recovery ventilation (HRV)** integration with full monitoring and control
- **Automated scheduling** for temperature management across all zones
- **Safety monitoring** with leak detection and critical alerting

## Main Components

### Climate Control
- Multiple heating zones using `generic_thermostat` platform
- Both radiator and underfloor heating systems
- Temperature sensors (Zigbee-based and placeholder sensors for zones pending installation)
- Automated circulation pump control for underfloor heating
- Weather-based heating curve calculation with configurable parameters

### Ventilation System
- Full MQTT integration with HRV unit
- Real-time monitoring of temperatures, airflow, CO2, and humidity
- Manual and automatic operation modes
- Bypass valve control
- Filter maintenance tracking

### Automation & Scheduling
- Time-based temperature scheduling using [scheduler-component](https://github.com/nielsfaber/scheduler-component)
- Visual schedule management via [scheduler-card](https://github.com/nielsfaber/scheduler-card)
- Automatic pump control based on zone valve states
- Boiler setpoint deviation monitoring and alerts
- Water leak detection with multi-stage notifications

### Hardware Integration
- **Zigbee (ZHA)**: Temperature/humidity sensors, smart switches
- **MQTT**: HRV unit communication
- **Weather integration**: Outdoor temperature for heating calculations

## File Structure

```
config/
├── configuration.yaml          # Main configuration file
├── scripts.yaml                # Custom scripts
├── scenes.yaml                 # Scene definitions
├── dashboards/
│   └── heating.yaml            # Heating control dashboard
├── themes/                     # Custom themes
└── custom_zha_quirks/          # Custom Zigbee device quirks
```

## Key Features

### Heating Curve
Dynamic boiler temperature calculation based on outdoor conditions, eliminating the need for manual seasonal adjustments. Configurable slope and shift parameters allow fine-tuning for specific building characteristics.

### Smart Pump Control
Underfloor heating circulation pump activates automatically when any zone valve opens, with a delay to ensure valves are fully open before pump engagement.

### Comprehensive Dashboard
Single-page heating dashboard with:
- Boiler control and monitoring
- Individual thermostat controls for each room
- Historical temperature graphs
- Underfloor heating zone management
- Visual schedule editor for all zones

## Usage

This configuration is designed to be placed in the Home Assistant `config/` directory. All changes should be validated using Home Assistant's built-in configuration check before reloading or restarting.

### Dependencies
- [scheduler-component](https://github.com/nielsfaber/scheduler-component) (HACS)
- [scheduler-card](https://github.com/nielsfaber/scheduler-card) (HACS)
- MQTT broker (for HRV integration)
- Weather integration configured

## Version Control

This repository serves as both a backup and change tracking system for the entire home automation setup, enabling easy rollback and configuration history review.
