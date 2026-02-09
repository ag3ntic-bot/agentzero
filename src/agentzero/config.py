"""Model configuration for AgentZero.

Claude Opus 4.6 is selected as the primary model based on February 2026 benchmarks:
- Best-in-class coding performance (65.4% Terminal-Bench 2.0, 72.7% OSWorld)
- 1M token context window (beta), 128K max output
- Adaptive thinking for dynamic reasoning
- $5/$25 per million input/output tokens
"""

import os

from dotenv import load_dotenv

load_dotenv()

# Primary model: Claude Opus 4.6 (released Feb 5, 2026)
MODEL_ID = "claude-opus-4-6"

# Model parameters
MAX_TOKENS = 16384
CONTEXT_WINDOW = 200_000  # default; up to 1M in beta
TEMPERATURE = 1.0  # Anthropic recommended default

# API configuration
API_KEY = os.environ.get("ANTHROPIC_API_KEY", "")


def get_model_info() -> dict:
    """Return metadata about the configured model."""
    return {
        "model_id": MODEL_ID,
        "provider": "Anthropic",
        "model_name": "Claude Opus 4.6",
        "release_date": "2026-02-05",
        "context_window": CONTEXT_WINDOW,
        "max_output_tokens": 128_000,
        "pricing": {
            "input_per_million": 5.00,
            "output_per_million": 25.00,
        },
        "strengths": [
            "Best-in-class coding and agentic workflows",
            "Adaptive thinking (dynamic reasoning depth)",
            "1M token context window (beta)",
            "72.7% OSWorld (best computer-use model)",
            "65.4% Terminal-Bench 2.0",
        ],
    }
