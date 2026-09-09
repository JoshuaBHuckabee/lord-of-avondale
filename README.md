
# Lord of Avondale

A modular, text-based role-playing game inspired by classic MUDs.

**Lord of Avondale** is a long-term Python development project focused on building a playable text RPG while practicing professional software-development principles such as modular architecture, automated testing, documentation, version control, and eventual client/server networking.

## Project Overview

The goal of **Lord of Avondale** is to create a persistent text-based RPG that can eventually be hosted on a remote server and accessed by multiple players.

The game will begin as a simple local command-line application and progressively evolve toward a multiplayer MUD-style server.

The project is being developed incrementally so that each subsystem can be understood, tested, documented, and extended independently.

## Current Status

**Version:** `0.1.0 — Initial Development`

The current prototype includes:

-   A player character model
-   Character attributes
-   Health and damage handling
-   Character status display
-   ANSI terminal colors
-   A room/location system
-   Connected rooms
-   A small navigable dungeon
-   Basic directional movement
-   Basic command handling

The current implementation is intentionally small. The architecture will be expanded as new gameplay systems are introduced.

## Project Goals

The long-term goal is to develop a complete text-based RPG with:

-   Character creation
-   Character progression
-   Classes and statistics
-   Exploration
-   NPCs
-   Enemies
-   Combat
-   Weapons and armor
-   Inventory
-   Items and loot
-   Quests
-   Shops and economy
-   Saving and loading
-   ANSI terminal color
-   Player communication
-   Multiplayer networking
-   Persistent world state
-   Server administration
-   Remote hosting

The project will prioritize maintainability and extensibility over rapid feature development.

## Design Principles

### Modularity

Game systems should be separated into logical modules with clearly defined responsibilities.

A new feature should require as little modification as possible to unrelated systems.

### Separation of Responsibilities

Individual classes and modules should have a focused purpose.

For example:

-   A `Character` represents a character.
-   A `Room` represents a location.
-   A dungeon builder constructs the game world.
-   A command system interprets player input.
-   A combat system handles combat mechanics.

Systems should not become responsible for unrelated functionality.

### Testability

Important game mechanics will be covered by automated tests.

Tests will be developed alongside the features they verify rather than being postponed until the end of development.

### Readability

The codebase will favor clear, understandable Python over unnecessarily clever implementations.

Type hints, meaningful names, and documentation will be used throughout the project.

### Documentation

Important architectural decisions, game mechanics, development procedures, and design decisions will be documented as the project evolves.

## Project Structure

The project uses a `src` layout.

```text
lord-of-avondale/
│
├── README.md
├── LICENSE
├── .gitignore
├── pyproject.toml
│
├── docs/
│   ├── architecture.md
│   ├── development.md
│   └── game-design.md
│
├── src/
│   └── lord_of_avondale/
│       ├── __init__.py
│       │
│       ├── characters/
│       │   ├── __init__.py
│       │   └── character.py
│       │
│       ├── utils/
│       │   ├── __init__.py
│       │   └── colors.py
│       │
│       └── world/
│           ├── __init__.py
│           ├── room.py
│           └── dungeon.py
│
└── tests/

```

As development progresses, additional packages will be added for systems such as commands, combat, items, NPCs, persistence, and networking.

## Development Roadmap

### Phase 1 — Foundation

-   Create Git repository
-   Establish project structure
-   Create Python package
-   Create initial README
-   Character model
-   Character tests
-   ANSI color system
-   Room model
-   Room tests
-   Initial dungeon
-   Dungeon tests
-   Basic movement

### Phase 2 — Command System

-   Command parser
-   Command registry
-   Movement commands
-   Look command
-   Status command
-   Help command
-   Quit command
-   Unknown command handling
-   Command tests

### Phase 3 — World System

-   Expanded dungeon
-   NPC system
-   Enemies
-   Doors
-   Locked areas
-   Containers
-   Room objects
-   Dynamic room descriptions

### Phase 4 — Character Development

-   Character creation
-   Character classes
-   Attributes
-   Experience
-   Levels
-   Skills
-   Character progression

### Phase 5 — Combat

-   Combat system
-   Attack mechanics
-   Damage calculation
-   Defense
-   Critical hits
-   Death
-   Experience rewards
-   Combat tests

### Phase 6 — Items and Equipment

-   Item system
-   Inventory
-   Weapons
-   Armor
-   Equipment
-   Consumables
-   Loot
-   Item persistence

### Phase 7 — Game Systems

-   Quests
-   Shops
-   Currency
-   NPC dialogue
-   Factions
-   Reputation
-   World events

### Phase 8 — Persistence

-   Save/load system
-   Character persistence
-   World persistence
-   Data validation
-   Backup strategy

### Phase 9 — Multiplayer

-   Client/server architecture
-   Network protocol
-   Player sessions
-   Multiple simultaneous players
-   Player communication
-   Server commands
-   Connection management
-   Error handling

### Phase 10 — Deployment

-   Server configuration
-   Environment configuration
-   Logging
-   Server startup
-   Remote deployment
-   Database/storage strategy
-   Backup procedures
-   Administration documentation

## Development Environment

The project is being developed with **Python 3.12 or newer**.

A Python virtual environment should be used for local development.

### Create the Virtual Environment

```bash
python -m venv .venv

```

### Activate on Windows PowerShell

```powershell
.venv\Scripts\Activate.ps1

```

### Activate on Windows Command Prompt

```cmd
.venv\Scripts\activate

```

Once the project packaging is established, development dependencies can be installed with:

```bash
pip install -e ".[dev]"

```

## Running the Game

The game is currently under active development.

The exact startup command will be documented here as the application packaging and entry point are finalized.

## Running Tests

Automated tests will be run using `pytest`.

```bash
pytest

```

The test suite will expand as new systems are introduced.

## Version Control

Git is used for source control.

Development will be organized around logical commits representing meaningful changes to the project.

Examples:

```text
Initial project structure
Add Character model
Add Character tests
Implement Room model
Add dungeon builder
Implement command parser
Add combat system

```

The Git history is intended to document the evolution of the project as well as provide version control.

## Documentation

Additional project documentation will be maintained in the `docs/` directory.

Planned documentation includes:

### Architecture

**File:** `docs/architecture.md`

Describes the technical architecture of the game, including relationships between major systems and the reasoning behind architectural decisions.

### Development

**File:** `docs/development.md`

Describes how to set up the development environment, run the game, execute tests, and contribute changes.

### Game Design

**File:** `docs/game-design.md`

Documents game mechanics, character systems, combat rules, world design, progression, and other gameplay decisions.

## Educational Objectives

This project is also intended as a practical study in Python software development.

Topics explored during development include:

-   Python classes and objects
-   Dataclasses
-   Type hints
-   Modules and packages
-   Object-oriented design
-   Composition
-   Design patterns
-   Error handling
-   Testing
-   Git and version control
-   Software architecture
-   Command parsing
-   State management
-   Networking
-   Client/server architecture
-   Deployment

Each major subsystem will be introduced incrementally and documented as part of the development process.

## Project Philosophy

**Lord of Avondale** is intended to be more than a collection of game features.

The project is an exercise in building software that can continue to grow without becoming increasingly difficult to understand or maintain.

When choosing between adding a feature quickly and building a foundation that supports future development, the project will generally favor the latter.

## License

License information will be added as the project reaches its initial public release.