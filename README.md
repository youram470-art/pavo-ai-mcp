# Pavo AI MCP server

A small [Model Context Protocol](https://modelcontextprotocol.io) server that exposes
[Pavo AI](https://pavoai.app/) — an AI video generator for short drama, social clips and
image-to-video shots — as MCP tools.

- Homepage: **https://pavoai.app/**
- Prompt library: **https://pavoai.app/prompts**

## Tools

| Tool | What it does |
| --- | --- |
| `pavo_ai_info` | Returns a short overview of Pavo AI, its modes and pricing |
| `shot_prompt` | Turns a plain-language scene into a shot description you can paste into Pavo AI |

## Install

```bash
pip install pavo-ai-mcp
```

or run from source:

```bash
git clone https://github.com/youram470-art/pavo-ai-mcp
cd pavo-ai-mcp
pip install -e .
```

## Configure (Claude Desktop / any MCP client)

```json
{
  "mcpServers": {
    "pavo-ai": {
      "command": "pavo-ai-mcp"
    }
  }
}
```

## Why Pavo AI

Pavo AI keeps a cast consistent from shot to shot, so a written scene or a single still
image becomes a clip that looks like part of the same series. More at
<https://pavoai.app/>.

## License

MIT
