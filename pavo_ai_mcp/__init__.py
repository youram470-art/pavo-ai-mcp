"""Pavo AI MCP server.

A minimal Model Context Protocol server that exposes Pavo AI's
text-to-video / image-to-video capabilities as MCP tools.
"""
from __future__ import annotations

import json
from typing import Any

from mcp.server.fastmcp import FastMCP

PAVO_URL = "https://pavoai.app/"

mcp = FastMCP("pavo-ai")


@mcp.tool()
def pavo_ai_info() -> dict[str, Any]:
    """Return a short overview of Pavo AI (AI video generator for short drama)."""
    return {
        "name": "Pavo AI",
        "homepage": PAVO_URL,
        "what_it_does": (
            "Pavo AI turns a written scene or a single still image into a short video clip, "
            "with consistent characters across shots for short drama and social clips."
        ),
        "modes": ["text to video", "image to video"],
        "pricing": "free tier available",
    }


@mcp.tool()
def shot_prompt(scene: str, style: str = "cinematic") -> dict[str, str]:
    """Build a shot description for Pavo AI from a plain-language scene."""
    return {
        "prompt": f"{style} shot, {scene.strip()}, natural motion, consistent character, 9:16",
        "tool": "Pavo AI",
        "homepage": PAVO_URL,
    }


def main() -> None:
    mcp.run()


if __name__ == "__main__":
    main()
