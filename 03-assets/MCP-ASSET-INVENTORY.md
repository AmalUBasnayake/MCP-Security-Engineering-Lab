# MCP Asset Inventory

## 1. Purpose

This document identifies the assets that require protection
within the MCP security environment.

The inventory establishes the security value, sensitivity,
access requirements, and potential impact associated with
each asset.

## 2. Asset Inventory

| ID | Asset | Asset Type | Sensitivity | Primary Security Requirement |
|---|---|---|---|---|
| A-01 | AI Prompts | Data | High | Confidentiality and integrity |
| A-02 | Model Context | Data | High | Confidentiality |
| A-03 | MCP Client Identity | Identity | High | Authentication and authorization |
| A-04 | MCP Server | Compute | High | Integrity and availability |
| A-05 | MCP Tool Definitions | Application | High | Integrity and trust |
| A-06 | Tool Arguments | Input Data | High | Validation and abuse prevention |
| A-07 | MCP Credentials | Secret | Critical | Secret protection |
| A-08 | Enterprise Data | Data | Critical | Confidentiality and integrity |
| A-09 | Files | Resource | High | Access control and integrity |
| A-10 | Database | Resource | Critical | Authorization and data protection |
| A-11 | Cloud APIs | Service | High | Authorization and abuse prevention |
| A-12 | Security Logs | Security Data | High | Integrity and forensic availability |

## 3. Asset Protection Principle

Every asset must have an explicitly defined security
requirement and access boundary.

Access must follow the principle of least privilege.

Sensitive operations must be:

- Authenticated
- Authorized
- Validated
- Logged

## 4. Security Impact

Compromise of a high-value MCP asset may affect:

- Confidentiality
- Integrity
- Availability
- Identity security
- Enterprise data security
- Cloud resource security
- Security monitoring and investigation

## 5. Engineering Principle

An MCP security design must protect not only the MCP server,
but also the identities, tools, credentials, data, resources,
and telemetry that participate in the MCP workflow.