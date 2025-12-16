# AI Knowledge Base Methodology

Reusable prompts, scripts, and templates for building Claude-based knowledge bases.

## Purpose

This repository contains Cylentra's methodology for implementing AI knowledge bases using Claude Team Projects. It includes:

- **System prompts** for consistent AI behavior
- **Report templates** for structured output generation
- **Processing scripts** for document conversion (PDF/Word/Excel to Markdown)
- **KB architecture patterns** for organizing knowledge
- **Runbooks** for operations and maintenance

## Repository Structure

```
ai-kb-methodology/
├── CLAUDE.md                    # Claude Code project instructions
├── README.md                    # This file
├── prompts/
│   ├── system-prompts/          # KB system instructions
│   └── report-templates/        # Report generation prompts
├── scripts/                     # Document processing utilities
├── kb-architecture/             # KB structure templates
└── runbooks/                    # Operations documentation
```

## Usage

### For Developers (Phil, Marco)

1. Clone this repo to your local Development folder
2. Client-specific data stays in your local `Client-Work/` folder (NOT here)
3. Work on prompts, scripts, and templates here
4. Push changes to share with the team

### Git Workflow

```bash
# Before starting work
git pull origin main

# After making changes
git add .
git commit -m "feat: description of change"
git push origin main

# For larger changes, use feature branches
git checkout -b feature/your-feature
# ... work ...
git push -u origin feature/your-feature
# Create PR for review
```

## Key Principles

1. **No client data in this repo** - All client documents, deliverables, and PII stay local
2. **Reusable patterns** - Build for reuse across multiple clients
3. **Version control** - All methodology changes tracked in git
4. **Collaborative** - Both Phil and Marco can contribute and update

## Related Resources

- Claude Team: https://claude.ai/team
- Anthropic Docs: https://docs.anthropic.com/

---

*Maintained by Cylentra*
