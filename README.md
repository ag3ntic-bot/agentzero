# agentzero

AI agent powered by **Claude Opus 4.6** — the best model for coding and agentic workflows as of February 2026.

## Why Claude Opus 4.6?

Selected based on current benchmark rankings:

| Benchmark | Score | Notes |
|-----------|-------|-------|
| Terminal-Bench 2.0 | 65.4% | Industry-leading coding performance |
| OSWorld | 72.7% | Best computer-use model |
| Context Window | 1M tokens | Beta (200K default) |
| Max Output | 128K tokens | |

**Pricing:** $5/M input, $25/M output tokens.

Key advantages over alternatives:
- **vs GPT-5.2** ($1.75/$14): Claude leads on coding/agent benchmarks; GPT-5.2 is stronger on math (100% AIME 2025)
- **vs Gemini 3 Pro**: Claude leads on coding; Gemini leads overall LM Arena
- **Adaptive thinking**: Dynamically adjusts reasoning depth per request (no manual budget tuning)

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
