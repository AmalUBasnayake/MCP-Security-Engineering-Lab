# MCP Security Threat Model

## 1. Purpose

This document defines the threat model for the MCP security engineering environment.

The objective is to identify realistic attack paths against MCP identities, servers, tools, credentials, enterprise data, and downstream resources.

## 2. Threat Modeling Approach

Each threat is evaluated using the following engineering flow:

```text
Asset
  ↓
Threat Actor
  ↓
Entry Point
  ↓
Attack Path
  ↓
Target Asset
  ↓
Impact
  ↓
Prevention
  ↓
Detection
  ↓
Response
```

## 3. Threat Categories

The primary MCP threat categories considered in this lab are:

- Identity and authentication abuse
- Authorization bypass
- Malicious tool invocation
- Prompt injection leading to tool abuse
- Credential and secret exposure
- Enterprise data exfiltration
- MCP server compromise
- Untrusted or malicious tool supply chain
- Malicious input manipulation
- Logging and detection evasion

## 4. Threat Inventory

| ID | Threat | Entry Point | Target Asset | Primary Impact |
|---|---|---|---|---|
| T-01 | Identity / Authentication Abuse | MCP Client | MCP Client Identity | Unauthorized access |
| T-02 | Authorization Bypass | Tool Invocation | MCP Tool Definitions | Privilege escalation |
| T-03 | Malicious Tool Invocation | MCP Tool | Enterprise Resources | Unauthorized actions |
| T-04 | Prompt Injection -> Tool Abuse | AI Prompt / Context | Tool Arguments | Unintended tool execution |
| T-05 | Credential / Secret Exposure | MCP Server / Tool | MCP Credentials | Credential compromise |
| T-06 | Data Exfiltration | Tool Invocation | Enterprise Data | Confidentiality loss |
| T-07 | MCP Server Compromise | MCP Server | MCP Server | Integrity and availability loss |
| T-08 | Untrusted Tool Supply Chain | Tool Registration | MCP Tool Definitions | Malicious code execution |
| T-09 | Input Manipulation | Tool Arguments | Downstream Resources | Unauthorized data access |
| T-10 | Detection Evasion | Logging Pipeline | Security Logs | Reduced investigation capability |

## 5. Threat T-01 - Identity and Authentication Abuse

### Attack Path

```text
Attacker
  ↓
Compromised or forged identity
  ↓
MCP Client
  ↓
Authentication attempt
  ↓
MCP Server
  ↓
Unauthorized tool access
```

### Target Assets

- MCP Client Identity
- MCP Server
- MCP Tool Definitions

### Potential Impact

- Unauthorized access
- Privilege escalation
- Unauthorized tool invocation
- Loss of accountability

### Preventive Controls

- Strong authentication
- MFA where applicable
- Short-lived credentials
- Identity validation
- Least privilege

### Detection

- Authentication failures
- Unusual client identities
- Abnormal authentication patterns
- Repeated authentication attempts

### Response

- Revoke compromised credentials
- Disable affected identity
- Review authentication logs
- Investigate subsequent tool activity

## 6. Threat T-02 - Authorization Bypass

### Attack Path

```text
Authorized MCP Client
  ↓
Tool Invocation
  ↓
Authorization Weakness
  ↓
Restricted Tool
  ↓
Unauthorized Resource Access
```

### Target Assets

- MCP Tool Definitions
- Enterprise Data
- Database
- Cloud APIs

### Potential Impact

- Privilege escalation
- Unauthorized data access
- Unauthorized administrative actions

### Preventive Controls

- Explicit tool authorization
- Role-based access control
- Resource-level authorization
- Least privilege
- Tool allowlisting

### Detection

- Access denied events
- Unexpected tool usage
- Privilege changes
- Access to restricted resources

### Response

- Block unauthorized invocation
- Revoke excessive permissions
- Investigate affected resources
- Review authorization policies

## 7. Threat T-03 - Malicious Tool Invocation

### Attack Path

```text
AI Application / Agent
  ↓
MCP Client
  ↓
Malicious or abused tool request
  ↓
MCP Server
  ↓
Enterprise Resource
```

### Target Assets

- MCP Tool Definitions
- Tool Arguments
- Enterprise Resources

### Potential Impact

- Unauthorized actions
- Data modification
- Data deletion
- Resource abuse

### Preventive Controls

- Tool allowlisting
- Input validation
- Parameter constraints
- Least privilege
- Approval controls for high-risk actions

### Detection

- Abnormal tool invocation
- High-risk parameters
- Unusual request frequency
- Unexpected resource modifications

### Response

- Block the tool invocation
- Disable affected tool
- Revert unauthorized changes
- Investigate related activity

## 8. Threat T-04 - Prompt Injection Leading to Tool Abuse

### Attack Path

```text
Untrusted Content
  ↓
Prompt Injection
  ↓
AI Model / Agent
  ↓
Manipulated Tool Decision
  ↓
MCP Client
  ↓
MCP Tool
  ↓
Enterprise Resource
```

### Target Assets

- AI Prompts
- Model Context
- Tool Arguments
- Enterprise Data

### Potential Impact

- Unintended tool execution
- Data disclosure
- Unauthorized actions
- Security control bypass

### Preventive Controls

- Treat external content as untrusted
- Separate instructions from retrieved data
- Tool authorization boundaries
- Input validation
- High-risk action confirmation

### Detection

- Unexpected tool selection
- Tool calls inconsistent with user intent
- Suspicious prompt patterns
- Abnormal tool parameters

### Response

- Stop affected tool execution
- Isolate the session
- Review model context
- Investigate downstream actions

## 9. Threat T-05 - Credential and Secret Exposure

### Attack Path

```text
MCP Server / Tool
  ↓
Credential Access
  ↓
Secret Exposure
  ↓
Attacker
  ↓
Downstream Resource Access
```

### Target Assets

- MCP Credentials
- Cloud APIs
- Database
- Enterprise Data

### Potential Impact

- Credential compromise
- Unauthorized resource access
- Data exposure
- Lateral movement

### Preventive Controls

- Secret management
- Credential isolation
- Short-lived credentials
- Least privilege
- Secret rotation

### Detection

- Secret access events
- Unusual API usage
- Authentication from unexpected sources
- Credential misuse

### Response

- Revoke exposed credentials
- Rotate secrets
- Review downstream access
- Investigate affected identities

## 10. Threat T-06 - Enterprise Data Exfiltration

### Attack Path

```text
AI Application / Agent
  ↓
MCP Tool
  ↓
Enterprise Data
  ↓
Unauthorized Retrieval
  ↓
External Destination
```

### Target Assets

- Enterprise Data
- Files
- Database
- Cloud APIs

### Potential Impact

- Confidentiality loss
- Sensitive information disclosure
- Regulatory exposure
- Business impact

### Preventive Controls

- Data access controls
- Least privilege
- Data classification
- Output filtering
- Network restrictions

### Detection

- Large data retrieval
- Unusual query patterns
- Unexpected data destinations
- Abnormal API activity

### Response

- Block suspicious access
- Revoke affected permissions
- Preserve logs
- Investigate data exposure

## 11. Threat T-07 - MCP Server Compromise

### Attack Path

```text
Attacker
  ↓
MCP Server Vulnerability
  ↓
Server Compromise
  ↓
Tool Execution
  ↓
Enterprise Resources
```

### Target Assets

- MCP Server
- MCP Tool Definitions
- Enterprise Resources

### Potential Impact

- Code execution
- Credential theft
- Data access
- Service disruption

### Preventive Controls

- Secure server configuration
- Patch management
- Process isolation
- Network segmentation
- Least privilege

### Detection

- Process anomalies
- Unexpected network connections
- File modifications
- Privilege changes
- Security alerts

### Response

- Isolate the MCP server
- Disable affected services
- Rotate credentials
- Preserve forensic evidence
- Rebuild from a trusted state

## 12. Threat T-08 - Untrusted Tool Supply Chain

### Attack Path

```text
Untrusted Tool
  ↓
Tool Registration
  ↓
MCP Server
  ↓
Tool Invocation
  ↓
Enterprise Resource
```

### Target Assets

- MCP Tool Definitions
- MCP Server
- Enterprise Resources

### Potential Impact

- Malicious code execution
- Data theft
- Credential compromise
- Persistent access

### Preventive Controls

- Trusted tool sources
- Code review
- Tool allowlisting
- Dependency validation
- Integrity verification

### Detection

- Unexpected tool behavior
- File or process anomalies
- Network anomalies
- Tool integrity changes

### Response

- Disable untrusted tool
- Isolate affected server
- Review tool source and dependencies
- Rotate exposed credentials

## 13. Threat T-09 - Malicious Input Manipulation

### Attack Path

```text
Attacker-Controlled Input
  ↓
Tool Arguments
  ↓
Input Validation Failure
  ↓
MCP Tool
  ↓
Downstream Resource
```

### Target Assets

- Tool Arguments
- Files
- Database
- Cloud APIs

### Potential Impact

- Unauthorized queries
- Data modification
- Command or parameter abuse
- Resource manipulation

### Preventive Controls

- Strict input validation
- Parameter allowlists
- Type validation
- Boundary checks
- Safe error handling

### Detection

- Invalid parameter patterns
- Repeated validation failures
- Unexpected query structures
- Abnormal resource activity

### Response

- Reject malicious input
- Block affected session
- Review tool logs
- Investigate downstream activity

## 14. Threat T-10 - Logging and Detection Evasion

### Attack Path

```text
Attacker
  ↓
MCP Activity
  ↓
Logging Weakness
  ↓
Missing Security Telemetry
  ↓
Reduced Detection Capability
```

### Target Assets

- Security Logs
- Audit Events
- Detection Pipeline

### Potential Impact

- Delayed detection
- Reduced forensic visibility
- Incomplete incident investigation

### Preventive Controls

- Centralized logging
- Immutable or protected logs
- Complete tool invocation logging
- Time synchronization
- Log integrity controls

### Detection

- Missing expected events
- Logging failures
- Telemetry gaps
- Unexpected changes to logging configuration

### Response

- Restore logging
- Investigate telemetry gaps
- Preserve available evidence
- Review affected activity

## 15. Engineering Principle

MCP threats must be evaluated across the complete execution chain rather than against the MCP server alone.

Security decisions must connect:

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
Telemetry
  ↓
Detection
  ↓
Response
```

The objective is to prevent a compromised identity, tool, server, or model interaction from becoming unrestricted access to enterprise resources.
