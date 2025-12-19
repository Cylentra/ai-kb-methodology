# Claude Project Build Process

This document describes the standard process for building a Claude Project knowledge base and report templates for clients.

## Overview

Claude Projects are built directly in the client's Claude Team workspace. Cylentra maintains reusable methodology assets (prompts, scripts, templates) in this repository for use across engagements.

## Component Locations

| Component | Location | Purpose |
|-----------|----------|---------|
| Knowledge Base | Client's Claude Team Project | Client-specific methodology docs |
| Document Processing Scripts | `ai-kb-methodology/scripts/` | Convert PDF/Word/Excel → Markdown |
| System Prompts | `ai-kb-methodology/prompts/` | Reusable prompt templates |
| Report Templates | `ai-kb-methodology/prompts/report-templates/` | Report generation patterns |

## Process Steps

### 1. Document Collection
- Receive client methodology documents
- Supported formats: PDF, Word, Excel, PowerPoint
- Document limits defined in SOW

### 2. Document Processing
- Convert documents to Markdown using scripts from `scripts/` folder
- Clean and normalize formatting
- Preserve document structure and hierarchy

### 3. Knowledge Base Organization
Organize processed documents into a 3-layer architecture:

- **Layer 1 - Canonical SOPs**: Official methodology documentation
- **Layer 2 - Expert Voice**: Tacit knowledge from interviews, decision principles
- **Layer 3 - Guardrails**: Compliance rules, escalation triggers, quality gates

### 4. Claude Project Setup
- Create Project in client's Claude Team workspace
- Upload processed Markdown documents
- Configure system prompts from `prompts/system-prompts/`

### 5. Report Template Development
- Build report template(s) per SOW scope
- Create structured prompts and workflow documentation
- Test with anonymized/sample data only

### 6. Validation & Testing
- Test retrieval accuracy with representative questions
- Validate responses against source materials
- Conduct revision cycles based on client feedback

## Key Principles

- **Client ownership**: All work done in client's Claude Team workspace
- **Data privacy**: No real client PII/PHI - use anonymized data only
- **No data retention**: Cylentra does not retain copies of client documents
- **Reusable assets**: Scripts and prompt templates maintained in this repo

## Related Resources

- `scripts/` - Document processing utilities
- `prompts/system-prompts/` - KB system instructions
- `prompts/report-templates/` - Report generation prompts
- `kb-architecture/` - KB structure templates
