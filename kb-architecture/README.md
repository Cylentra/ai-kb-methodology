# Knowledge Base Architecture

This folder contains templates and guidance for structuring Claude Project knowledge bases.

## 3-Layer Architecture

Claude Project knowledge bases are organized into three layers:

| Layer | Purpose | Content Examples |
|-------|---------|------------------|
| **Layer 1: Canonical SOPs** | Official methodology documentation | Policies, procedures, compliance docs, process flows |
| **Layer 2: Expert Voice** | Tacit knowledge from SMEs | Interview transcripts, decision principles, "how we actually do it" notes |
| **Layer 3: Guardrails** | Boundaries and triggers | Escalation rules, compliance constraints, quality gates, red flags |

## Folder Structure Template

```
client-kb/
├── layer-1-sops/
│   ├── policies/
│   ├── procedures/
│   └── process-flows/
├── layer-2-expert-voice/
│   ├── interviews/
│   └── decision-principles/
├── layer-3-guardrails/
│   ├── escalation-triggers/
│   ├── compliance-rules/
│   └── quality-gates/
└── reference/
    └── glossary.md
```

## Document Naming Conventions

- Use lowercase with hyphens: `account-opening-procedure.md`
- Prefix with category when helpful: `sop-kyc-verification.md`
- Include version if tracking revisions: `policy-aml-v2.md`

## See Also

- [Claude Project Build Process](../runbooks/claude-project-build-process.md)
