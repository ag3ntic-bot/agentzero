# agentzero

AI agent powered by **Claude Opus 4.6** — the best model for coding and agentic workflows as of February 2026.

## Setup

```bash
# Install dependencies
pip install -e .

# Configure API key
cp .env.example .env
# Edit .env and add your ANTHROPIC_API_KEY
```

Get an API key at https://console.anthropic.com/

## Usage

```bash
# Run the agent
agentzero

# Or directly
python -m agentzero.main
```

## Project Structure

```
src/agentzero/
  __init__.py    # Package init
  config.py      # Model configuration and metadata
  agent.py       # Core agent with Claude Opus 4.6
  main.py        # CLI entry point
```
