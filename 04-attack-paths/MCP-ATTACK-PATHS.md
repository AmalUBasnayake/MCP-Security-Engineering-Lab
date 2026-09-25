# MCP Attack Path Engineering

## 1. Purpose

This document defines realistic attack paths against the
Model Context Protocol (MCP) security environment.

The objective is to translate identified threats into
end-to-end attack chains that connect:

- Threat actor
- Entry point
- Identity
- Authorization
- Tool invocation
- Input
- Resource access
- Impact
- Detection
- Response

The attack paths are designed to support security control
validation and defensive engineering.

## 2. Attack Path Model

Each attack path follows this engineering sequence:

```text
Threat Actor
     ↓
Entry Point
     ↓
Identity
     ↓
Authorization
     ↓
Tool Invocation
     ↓
Input / Arguments
     ↓
MCP Resource
     ↓
Security Impact
     ↓
Detection
     ↓
Response
```

## 3. Attack Path Principles

MCP attack paths must be evaluated across the complete
execution chain rather than against a single component.

Security validation must determine:

- Who initiated the request
- How the identity was authenticated
- What authorization was granted
- Which MCP tool was invoked
- What arguments were supplied
- Which resource was accessed
- What security boundary was crossed
- What impact occurred
- What telemetry was generated
- How the activity would be detected
- How the incident would be contained

## 4. Attack Path Inventory

| ID | Attack Path | Entry Point | Target | Primary Impact |
|---|---|---|---|---|
| AP-01 | Identity Compromise | MCP Client | MCP Client Identity | Unauthorized access |
| AP-02 | Authorization Bypass | Tool Invocation | MCP Tool | Privilege escalation |
| AP-03 | Malicious Tool Invocation | MCP Tool | Enterprise Resource | Unauthorized action |
| AP-04 | Prompt Injection to Tool Abuse | AI Prompt / Context | Tool Arguments | Unintended execution |
| AP-05 | Credential Exposure | MCP Server / Tool | MCP Credentials | Credential compromise |
| AP-06 | Data Exfiltration | Tool Invocation | Enterprise Data | Confidentiality loss |
| AP-07 | MCP Server Compromise | MCP Server | MCP Server | Integrity and availability loss |
| AP-08 | Untrusted Tool Supply Chain | Tool Registration | MCP Tool | Malicious code execution |
| AP-09 | Input Manipulation | Tool Arguments | Downstream Resource | Unauthorized data access |
| AP-10 | Detection Evasion | Logging Pipeline | Security Logs | Reduced investigation capability |

## 5. Attack Path AP-01 — Identity Compromise

### Attack Objective

Obtain or abuse an MCP client identity to invoke MCP
capabilities without legitimate authorization.

### Attack Chain

```text
Threat Actor
     ↓
Compromised Client Credential
     ↓
MCP Client Identity
     ↓
Authentication
     ↓
MCP Server
     ↓
Authorized Tool Invocation
     ↓
Enterprise Resource
     ↓
Unauthorized Access
```

### Target Assets

- MCP Client Identity
- MCP Credentials
- MCP Server
- Enterprise Resources

### Security Controls

- Strong authentication
- MFA where applicable
- Short-lived credentials
- Least privilege
- Credential rotation
- Conditional access
- Session monitoring
- Audit logging

### Detection

Detect:

- Authentication anomalies
- Unusual client activity
- Unexpected geographic or network origin
- Abnormal tool invocation frequency
- Access outside normal patterns
- Repeated authentication failures

### Response

- Revoke compromised credentials
- Terminate active sessions
- Investigate affected identity
- Review tool invocation history
- Identify accessed resources
- Rotate associated secrets

## 6. Attack Path AP-02 — Authorization Bypass

### Attack Objective

Cause an MCP client or tool to perform an action beyond
its intended authorization scope.

### Attack Chain

```text
Threat Actor
     ↓
Valid MCP Identity
     ↓
Tool Invocation
     ↓
Authorization Weakness
     ↓
Unauthorized Tool Capability
     ↓
Privileged Resource
     ↓
Privilege Escalation
```

### Target Assets

- Authorization policies
- MCP Tool Definitions
- Enterprise Resources
- Administrative operations

### Security Controls

- Explicit authorization policies
- Tool allowlisting
- Resource-level authorization
- Least privilege
- Deny-by-default access
- Privileged operation approval
- Authorization logging

### Detection

Detect:

- Authorization failures
- Access to restricted tools
- Unexpected privilege changes
- Privileged operations from non-privileged identities
- Tool calls outside approved scope

### Response

- Block unauthorized invocation
- Revoke excessive permissions
- Investigate the identity
- Review authorization configuration
- Audit affected resources

## 7. Attack Path AP-03 — Malicious Tool Invocation

### Attack Objective

Abuse an approved MCP tool to perform unauthorized actions
against enterprise resources.

### Attack Chain

```text
Threat Actor
     ↓
Compromised or Abused Identity
     ↓
Approved MCP Tool
     ↓
Malicious Tool Invocation
     ↓
Enterprise Resource
     ↓
Unauthorized Action
```

### Security Controls

- Tool allowlisting
- Function-level authorization
- Input validation
- Rate limiting
- Resource-level permissions
- Audit logging

### Detection

Detect:

- Unusual tool invocation patterns
- High-frequency requests
- Sensitive operations
- Unexpected resource access
- Tool usage outside normal behavior

### Response

- Disable affected tool
- Block suspicious identity
- Preserve logs
- Review impacted resources
- Restore secure configuration

## 8. Attack Path AP-04 — Prompt Injection to Tool Abuse

### Attack Objective

Use malicious instructions within AI input or context to
cause unintended MCP tool execution.

### Attack Chain

```text
Attacker-Controlled Content
     ↓
AI Prompt / Context
     ↓
Prompt Injection
     ↓
AI Agent Decision
     ↓
MCP Tool Selection
     ↓
Malicious Tool Arguments
     ↓
Enterprise Resource
     ↓
Unintended Action
```

### Target Assets

- AI prompts
- Model context
- Tool arguments
- MCP tools
- Enterprise resources

### Security Controls

- Prompt boundary enforcement
- Tool authorization
- Input validation
- Tool allowlisting
- Human approval for high-risk actions
- Sensitive operation confirmation
- Output and action monitoring

### Detection

Detect:

- Unexpected tool selection
- Suspicious prompt patterns
- High-risk tool arguments
- Tool invocation inconsistent with user intent
- Sensitive actions following untrusted content

### Response

- Block high-risk tool invocation
- Isolate suspicious context
- Review prompt and tool history
- Revoke affected session
- Investigate downstream activity

## 9. Attack Path AP-05 — Credential Exposure

### Attack Objective

Obtain MCP credentials or secrets and use them to access
protected resources.

### Attack Chain

```text
Threat Actor
     ↓
Credential Exposure
     ↓
MCP Server / Tool
     ↓
MCP Credential
     ↓
Credential Abuse
     ↓
Enterprise Resource
     ↓
Unauthorized Access
```

### Security Controls

- Secret management
- Credential isolation
- Environment protection
- Short-lived credentials
- Secret rotation
- Access logging
- No hard-coded secrets

### Detection

Detect:

- Secret access anomalies
- Credential usage from unexpected locations
- Repeated authentication failures
- Unusual resource access
- Secret retrieval outside normal workflows

### Response

- Revoke exposed credential
- Rotate secrets
- Investigate usage
- Identify affected resources
- Preserve evidence

## 10. Attack Path AP-06 — Data Exfiltration

### Attack Objective

Use an MCP tool to retrieve sensitive enterprise data and
transfer it to an unauthorized destination.

### Attack Chain

```text
Threat Actor
     ↓
Compromised MCP Session
     ↓
Tool Invocation
     ↓
Enterprise Data Access
     ↓
Sensitive Data Retrieval
     ↓
External Destination
     ↓
Data Exfiltration
```

### Security Controls

- Data access controls
- Least privilege
- Data classification
- DLP controls
- Network restrictions
- Output filtering
- Audit logging

### Detection

Detect:

- Large data retrieval
- Sensitive data access
- Unusual export activity
- Unexpected external destinations
- Abnormal tool usage

### Response

- Block data transfer
- Revoke session
- Identify exposed data
- Investigate destination
- Preserve evidence
- Apply containment controls

## 11. Attack Path AP-07 — MCP Server Compromise

### Attack Objective

Compromise the MCP server and abuse its position as a
trusted intermediary between AI applications and resources.

### Attack Chain

```text
Threat Actor
     ↓
MCP Server Vulnerability
     ↓
Server Compromise
     ↓
Tool Manipulation
     ↓
Credential / Resource Access
     ↓
Enterprise Impact
```

### Security Controls

- Secure server configuration
- Patch management
- Network segmentation
- Host protection
- Application allowlisting
- Credential isolation
- Runtime monitoring

### Detection

Detect:

- Unexpected server processes
- Configuration changes
- Unauthorized tool changes
- Abnormal network connections
- Privilege escalation
- Unexpected credential access

### Response

- Isolate MCP server
- Disable affected tools
- Rotate credentials
- Preserve forensic evidence
- Rebuild from trusted configuration
- Review downstream access

## 12. Attack Path AP-08 — Untrusted Tool Supply Chain

### Attack Objective

Introduce a malicious or compromised MCP tool into the
trusted tool ecosystem.

### Attack Chain

```text
Threat Actor
     ↓
Malicious Tool Package
     ↓
Tool Registration
     ↓
MCP Server
     ↓
Tool Invocation
     ↓
Malicious Code Execution
     ↓
Enterprise Impact
```

### Security Controls

- Trusted tool sources
- Code review
- Package integrity verification
- Tool allowlisting
- Dependency scanning
- Version control
- Change approval

### Detection

Detect:

- Unexpected tool registration
- Tool binary changes
- Dependency changes
- Integrity failures
- Unexpected outbound connections

### Response

- Disable malicious tool
- Remove compromised package
- Restore trusted version
- Rotate affected credentials
- Investigate execution history

## 13. Attack Path AP-09 — Input Manipulation

### Attack Objective

Manipulate MCP tool arguments to access or modify resources
outside the intended security scope.

### Attack Chain

```text
Threat Actor
     ↓
Manipulated Tool Arguments
     ↓
MCP Tool
     ↓
Input Validation Failure
     ↓
Downstream Resource
     ↓
Unauthorized Data Access
```

### Security Controls

- Strict input validation
- Schema validation
- Parameter allowlisting
- Type validation
- Output validation
- Resource-level authorization

### Detection

Detect:

- Invalid parameters
- Unexpected parameter values
- Repeated validation failures
- Requests outside normal ranges
- Access to unauthorized resources

### Response

- Reject malicious input
- Block suspicious session
- Review affected requests
- Validate downstream resource integrity

## 14. Attack Path AP-10 — Detection Evasion

### Attack Objective

Prevent or reduce the visibility required to detect and
investigate malicious MCP activity.

### Attack Chain

```text
Threat Actor
     ↓
Logging Configuration Abuse
     ↓
Telemetry Reduction
     ↓
Missing Tool Invocation Events
     ↓
Reduced Detection
     ↓
Extended Attacker Activity
```

### Security Controls

- Centralized logging
- Immutable audit records
- Log integrity protection
- Time synchronization
- Monitoring of logging configuration
- Security alerting

### Detection

Detect:

- Missing expected events
- Logging failures
- Telemetry gaps
- Unexpected changes to logging configuration
- Unexpected reduction in event volume

### Response

- Restore logging
- Investigate telemetry gaps
- Preserve available evidence
- Review affected activity
- Validate monitoring coverage

## 15. Engineering Principle

MCP attack paths must be evaluated as complete execution
chains rather than isolated vulnerabilities.

Security engineering must connect:

```text
Identity
   ↓
Authorization
   ↓
Tool
   ↓
Input
   ↓
Resource
   ↓
Impact
   ↓
Telemetry
   ↓
Detection
   ↓
Response
```

A secure MCP environment must assume that a single control
can fail and therefore enforce multiple security boundaries
across the complete execution path.
