# MCP Security Control Matrix

## 1. Purpose

This document maps identified MCP threats and attack paths to preventive, detective, and responsive security controls.

The objective is to establish a traceable security control model that connects threats to practical engineering protections and measurable security evidence.

The control model follows:

```text
Threat
   ↓
Attack Path
   ↓
Security Control
   ↓
Prevention
   ↓
Detection
   ↓
Response
   ↓
Evidence
```

## 2. Control Engineering Principles

MCP security controls must be:

- Identity-aware
- Least-privilege based
- Explicitly authorized
- Input validated
- Resource scoped
- Observable
- Auditable
- Testable
- Recoverable

A control is not considered complete unless its effectiveness can be validated through observable security evidence.

## 3. Control Classification

| Type | Purpose | Examples |
|---|---|---|
| Preventive | Reduce the probability of successful attack | MFA, allowlisting, least privilege |
| Detective | Identify suspicious or malicious activity | SIEM alerts, audit logs, anomaly detection |
| Responsive | Contain and recover from security events | Credential revocation, session termination |
| Governance | Establish security requirements | Policies, approvals, change control |

## 4. Security Control Inventory

| ID | Control | Type | Security Objective |
|---|---|---|---|
| C-01 | Strong Identity Authentication | Preventive | Verify MCP client identity |
| C-02 | Least Privilege Authorization | Preventive | Limit access to approved capabilities |
| C-03 | MCP Tool Allowlisting | Preventive | Restrict executable tool surface |
| C-04 | Tool Input Validation | Preventive | Prevent malicious or invalid arguments |
| C-05 | Resource-Level Authorization | Preventive | Restrict downstream resource access |
| C-06 | Credential and Secret Protection | Preventive | Protect MCP credentials |
| C-07 | Network Segmentation | Preventive | Limit lateral movement and resource exposure |
| C-08 | Centralized Audit Logging | Detective | Record security-relevant activity |
| C-09 | Behavioral Detection | Detective | Identify anomalous MCP activity |
| C-10 | Security Alerting | Detective | Surface high-risk events |
| C-11 | Credential Revocation | Responsive | Contain compromised identities |
| C-12 | Session Termination | Responsive | Stop active malicious sessions |
| C-13 | Tool Isolation | Responsive | Contain compromised MCP tools |
| C-14 | Evidence Preservation | Responsive | Support investigation and forensics |
| C-15 | Change and Tool Approval | Governance | Control MCP environment changes |

## 5. Threat-to-Control Mapping

| Threat | Attack Path | Primary Controls | Detection | Response |
|---|---|---|---|---|
| T-01 Identity / Authentication Abuse | AP-01 | C-01, C-02 | C-08, C-09 | C-11, C-12 |
| T-02 Authorization Bypass | AP-02 | C-02, C-05 | C-08, C-10 | C-12 |
| T-03 Malicious Tool Invocation | AP-03 | C-03, C-04, C-05 | C-08, C-09 | C-13 |
| T-04 Prompt Injection to Tool Abuse | AP-04 | C-03, C-04, C-05 | C-09, C-10 | C-12, C-13 |
| T-05 Credential / Secret Exposure | AP-05 | C-06 | C-08, C-09 | C-11 |
| T-06 Data Exfiltration | AP-06 | C-02, C-05, C-07 | C-08, C-09, C-10 | C-12, C-14 |
| T-07 MCP Server Compromise | AP-07 | C-06, C-07, C-15 | C-08, C-09 | C-13, C-14 |
| T-08 Untrusted Tool Supply Chain | AP-08 | C-03, C-15 | C-08, C-10 | C-13, C-14 |
| T-09 Input Manipulation | AP-09 | C-04, C-05 | C-08, C-09 | C-12 |
| T-10 Detection Evasion | AP-10 | C-08, C-15 | C-10 | C-14 |

## 6. Control C-01 — Strong Identity Authentication

### Objective

Ensure that every MCP client request is associated with a verified identity.

### Preventive Controls

- Strong authentication
- MFA where applicable
- Short-lived credentials
- Conditional access
- Device or workload identity validation

### Detection

Monitor:

- Authentication failures
- Unexpected authentication locations
- Abnormal client identity usage
- Repeated authentication attempts

### Response

- Revoke compromised credentials
- Terminate sessions
- Investigate identity activity

### Evidence

Expected evidence includes:

- Authentication logs
- Identity sign-in records
- Failed authentication events
- Session records

## 7. Control C-02 — Least Privilege Authorization

### Objective

Ensure identities and tools receive only the permissions required to perform their intended function.

### Preventive Controls

- Deny-by-default authorization
- Role-based access
- Resource-level permissions
- Privileged operation approval
- Separation of duties

### Detection

Monitor:

- Authorization failures
- Privilege changes
- Access outside approved scope
- Unexpected privileged operations

### Response

- Remove excessive permissions
- Revoke unauthorized access
- Review affected identities

### Evidence

Expected evidence includes:

- Authorization policy
- Role assignments
- Permission change logs
- Access events

## 8. Control C-03 — MCP Tool Allowlisting

### Objective

Restrict MCP execution to approved and trusted tools.

### Preventive Controls

- Explicit tool allowlist
- Trusted tool sources
- Tool registration approval
- Version control
- Integrity verification

### Detection

Monitor:

- New tool registration
- Tool configuration changes
- Unexpected tool versions
- Tool integrity failures

### Response

- Disable untrusted tool
- Restore approved version
- Investigate tool activity

### Evidence

Expected evidence includes:

- Approved tool inventory
- Registration records
- Tool hashes or integrity records
- Change approvals

## 9. Control C-04 — Tool Input Validation

### Objective

Prevent malicious, malformed, or unauthorized tool arguments from reaching downstream resources.

### Preventive Controls

- Schema validation
- Type validation
- Parameter allowlisting
- Input length restrictions
- Output validation

### Detection

Monitor:

- Invalid arguments
- Repeated validation failures
- Unexpected parameter values
- Abnormal request patterns

### Response

- Reject malicious input
- Block suspicious sessions
- Investigate affected requests

### Evidence

Expected evidence includes:

- Validation logs
- Rejected request records
- Tool argument audit records
- Security alerts

## 10. Control C-05 — Resource-Level Authorization

### Objective

Ensure MCP tools can access only explicitly authorized downstream resources.

### Preventive Controls

- Resource-level permissions
- Data access policies
- Network restrictions
- Separate service identities
- Least privilege

### Detection

Monitor:

- Unauthorized resource access
- Sensitive data retrieval
- Cross-boundary access
- Abnormal resource usage

### Response

- Block access
- Revoke permissions
- Investigate affected resource

### Evidence

Expected evidence includes:

- Resource access logs
- Authorization records
- Data access events
- Network flow records

## 11. Control C-06 — Credential and Secret Protection

### Objective

Protect MCP credentials, tokens, API keys, and other authentication secrets.

### Preventive Controls

- Centralized secret management
- Credential isolation
- Short-lived tokens
- Secret rotation
- No hard-coded credentials

### Detection

Monitor:

- Secret access
- Unusual credential usage
- Secret retrieval anomalies
- Authentication from unexpected sources

### Response

- Revoke exposed credential
- Rotate secrets
- Investigate credential usage

### Evidence

Expected evidence includes:

- Secret access logs
- Credential rotation records
- Authentication events
- Secret scanning results

## 12. Control C-07 — Network Segmentation

### Objective

Limit network exposure and prevent compromised MCP components from freely accessing enterprise resources.

### Preventive Controls

- Network segmentation
- Firewall rules
- Private network paths
- Restricted outbound access
- Service-to-service filtering

### Detection

Monitor:

- Unexpected network connections
- New destinations
- Lateral movement indicators
- Abnormal outbound traffic

### Response

- Block malicious connection
- Isolate affected component
- Review network activity

### Evidence

Expected evidence includes:

- Firewall logs
- Network flow records
- Connection events
- Segmentation configuration

## 13. Control C-08 — Centralized Audit Logging

### Objective

Maintain reliable security telemetry for MCP activity.

### Required Events

- Authentication
- Authorization
- Tool invocation
- Tool arguments
- Resource access
- Configuration changes
- Security failures

### Security Requirements

- Centralized collection
- Time synchronization
- Log integrity
- Access control
- Retention policy

### Detection

Monitor:

- Missing events
- Logging failures
- Telemetry gaps
- Unexpected configuration changes

### Response

- Restore logging
- Investigate telemetry gaps
- Preserve available evidence

### Evidence

Expected evidence includes:

- Centralized audit records
- Log integrity records
- SIEM events
- Logging configuration

## 14. Control C-09 — Behavioral Detection

### Objective

Identify abnormal MCP behavior that may indicate compromise or abuse.

### Detection Signals

- Unusual tool invocation frequency
- Unexpected resource access
- Abnormal client behavior
- Unusual data retrieval
- Unexpected tool selection
- Privilege anomalies

### Response

- Investigate alert
- Validate identity
- Review tool activity
- Contain suspicious session

### Evidence

Expected evidence includes:

- Detection alerts
- Behavioral baselines
- Investigation records
- Correlated security events

## 15. Control C-10 — Security Alerting

### Objective

Generate actionable alerts for high-risk MCP activity.

### Alert Examples

- Repeated authentication failures
- Authorization bypass attempts
- Sensitive resource access
- Untrusted tool registration
- Credential anomalies
- Logging failures
- Large data transfers

### Response

Alerts should support:

- Identity investigation
- Tool investigation
- Resource investigation
- Automated response where appropriate

### Evidence

Expected evidence includes:

- SIEM alerts
- Alert rules
- Incident records
- Automated response logs

## 16. Control C-11 — Credential Revocation

### Objective

Rapidly invalidate compromised MCP credentials.

### Response Actions

- Revoke credential
- Rotate secret
- Terminate associated sessions
- Identify affected resources
- Review historical usage

### Evidence

Expected evidence includes:

- Revocation records
- Secret rotation records
- Session termination events

## 17. Control C-12 — Session Termination

### Objective

Stop active malicious or compromised MCP sessions.

### Response Actions

- Terminate session
- Block identity
- Revoke tokens
- Preserve session telemetry
- Investigate activity

### Evidence

Expected evidence includes:

- Session termination logs
- Identity block records
- Token revocation records

## 18. Control C-13 — Tool Isolation

### Objective

Contain a malicious, compromised, or abused MCP tool.

### Response Actions

- Disable tool
- Remove tool registration
- Isolate execution environment
- Block downstream access
- Preserve tool evidence

### Evidence

Expected evidence includes:

- Tool disablement records
- Registration changes
- Isolation events
- Investigation records

## 19. Control C-14 — Evidence Preservation

### Objective

Preserve reliable evidence required for security investigation and forensic analysis.

### Evidence Sources

- Authentication logs
- Authorization logs
- Tool invocation logs
- Tool arguments
- Resource access logs
- Network telemetry
- Configuration changes
- Security alerts

### Requirements

Evidence must maintain:

- Integrity
- Timestamp accuracy
- Chain of custody
- Appropriate retention

## 20. Control C-15 — Change and Tool Approval

### Objective

Ensure MCP tools, configurations, and security-sensitive changes are reviewed and approved before deployment.

### Preventive Controls

- Change approval
- Code review
- Tool registration approval
- Version control
- Integrity verification
- Separation of duties

### Detection

Monitor:

- Unauthorized changes
- Unexpected tool registration
- Configuration drift
- Integrity failures

### Response

- Roll back unauthorized change
- Disable affected component
- Investigate change source
- Preserve evidence

## 21. Control Validation Model

Every security control should be validated using:

```text
Control Definition
       ↓
Implementation
       ↓
Security Test
       ↓
Expected Telemetry
       ↓
Detection
       ↓
Response
       ↓
Evidence
```

A control should not be considered effective solely because it is documented.

Its effectiveness must be demonstrated through testing and observable evidence.

## 22. Engineering Principle

MCP security controls must form a layered defense.

No single control should be assumed to prevent every attack.

The security architecture should connect:

```text
Identity
   ↓
Authorization
   ↓
Tool Security
   ↓
Input Validation
   ↓
Resource Protection
   ↓
Network Security
   ↓
Logging
   ↓
Detection
   ↓
Response
   ↓
Evidence
```

The objective is to make every MCP operation:

**Authenticated → Authorized → Validated → Controlled → Logged → Detected → Recoverable**
