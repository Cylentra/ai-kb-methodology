# CLAUDE.md - AI Knowledge Base Methodology

## Project Context

This repository contains Cylentra's reusable methodology for building Claude-based knowledge bases. It supports multiple client engagements.

**Current Engagements:**
- STRIDE Financial (Phase 1: Dec 2025 - Jan 2026)

## Key Constraints (Apply to All KB Projects)

From typical SOW constraints:
- Knowledge base document limits (typically 50 docs)
- Limited revision cycles (typically 2)
- No real client PII/PHI - use anonymized/sample data only
- No integrations unless explicitly scoped
- Client owns Claude Team subscription

## File Organization

| Folder | Purpose | Examples |
|--------|---------|----------|
| `prompts/system-prompts/` | KB behavior instructions | Base system prompt, guardrails |
| `prompts/report-templates/` | Report generation prompts | Distribution analysis template |
| `scripts/` | Document processing | PDF-to-markdown, Excel parser |
| `kb-architecture/` | KB structure patterns | 3-layer architecture, folder templates |
| `runbooks/` | Operations docs | Maintenance procedures, troubleshooting |

## Development Patterns

### Hybrid Build Strategy
1. **Build** prompts and templates in Cylentra's Claude workspace
2. **Test** with synthetic/anonymized data
3. **Deploy** to client's Claude Team workspace
4. **Validate** with client feedback

### Document Processing Pipeline
```
Source (PDF/Word/Excel)
    → scripts/convert-to-markdown
    → Organize by KB layer
    → Ingest to Claude Project
    → Test retrieval accuracy
```

### KB Architecture (3 Layers)
- **Layer 1**: Canonical knowledge (SOPs, policies, procedures)
- **Layer 2**: Expert voice (CEO decisions, principles, exceptions)
- **Layer 3**: Guardrails (citations required, no hallucination)

## Conventions

### Commit Messages
Use conventional commits:
- `feat:` New prompts, templates, or scripts
- `fix:` Bug fixes or corrections
- `docs:` Documentation updates
- `refactor:` Code restructuring

### Naming
- Prompts: `[purpose]-[version].md` (e.g., `system-prompt-v1.md`)
- Scripts: `[action]-[format].py` (e.g., `convert-pdf-to-md.py`)
- Templates: `[report-type]-template.md`

## What Does NOT Go Here

- Client documents (PDFs, Word files, Excel data)
- Client-specific deliverables
- Any PII or PHI
- API keys or credentials

**Client data stays in local `Client-Work/[ClientName]/` folders.**

## Team

- **Phil**: PM/Solution Architect
- **Marco**: Primary Delivery

Both can update this CLAUDE.md with learnings and conventions.

---
*Last Updated: 2025-12-16*
