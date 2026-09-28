# MCP Detection Engineering

## 1. Purpose

This document defines the detection engineering model for
the MCP security environment.

The objective is to convert MCP security telemetry into
actionable detections that support investigation and response.

The detection lifecycle follows:

```text
MCP Activity
     ↓
Telemetry
     ↓
Detection Logic
     ↓
Alert
     ↓
Investigation
     ↓
Response
     ↓
Evidence
```

## 2. Detection Engineering Principles

MCP detections must be:

- Identity-aware
- Context-aware
- Tool-aware
- Resource-aware
- Behavior-aware
- Correlated
- Actionable
- Testable

A detection should identify not only that an event occurred,
but why the event may represent suspicious security activity.

## 3. Telemetry Sources

| ID | Source | Security Events |
|---|---|---|
| LOG-01 | MCP Server | Tool invocation |
| LOG-02 | MCP Server | Authorization decision |
| LOG-03 | MCP Server | Input validation result |
| LOG-04 | MCP Server | Security warning |
| LOG-05 | MCP Inspector | MCP protocol requests |
| LOG-06 | Identity Layer | Authentication activity |
| LOG-07 | Resource Layer | Resource access |
| LOG-08 | Network Layer | Connection activity |

## 4. Detection Inventory

| ID | Detection | Trigger | Primary Risk | Severity |
|---|---|---|---|---|
| DET-01 | Repeated Authorization Failure | Multiple denied tool requests | Unauthorized access | High |
| DET-02 | Unknown Tool Input | Unapproved tool argument | Input abuse | Medium |
| DET-03 | Path-Like Input Attempt | Suspicious path pattern | Resource access abuse | High |
| DET-04 | Abnormal Tool Frequency | Excessive tool invocations | Automated abuse | Medium |
| DET-05 | Sensitive Tool Usage | High-risk operation | Data exposure | High |
| DET-06 | Credential Anomaly | Unexpected credential activity | Credential compromise | Critical |
| DET-07 | Tool Registration Change | New or modified tool | Supply-chain risk | High |
| DET-08 | Logging Failure | Missing expected telemetry | Detection evasion | High |
| DET-09 | Configuration Change | Security configuration modified | Defense degradation | High |
| DET-10 | Unusual Resource Access | Access outside expected scope | Data exposure | High |

## 5. Detection DET-01 — Repeated Authorization Failure

### Objective

Detect repeated attempts to invoke MCP capabilities outside
the approved authorization scope.

### Example Signal

```text
Authorization Failure
       ↓
Same Identity
       ↓
Multiple Attempts
       ↓
Detection Threshold
       ↓
Alert
```

### Detection Logic

Monitor:

- Repeated denied tool requests
- Same identity making multiple failures
- Multiple tools denied in a short period
- Repeated access to restricted resources

### Investigation

Review:

- Identity
- Tool name
- Request time
- Request parameters
- Resource target
- Previous successful activity

### Response

- Block or suspend suspicious session
- Review identity activity
- Preserve related telemetry
- Investigate affected tools and resources

## 6. Detection DET-02 — Unknown Tool Input

### Objective

Detect repeated use of component or tool values that are
outside the approved allowlist.

### Example Signal

```text
Tool Invocation
      ↓
Allowlist Check
      ↓
DENY
      ↓
Repeated Events
      ↓
Detection
```

### Investigation

Review:

- Supplied input
- Request source
- Identity
- Frequency
- Related tool activity

### Response

- Reject request
- Monitor session
- Investigate repeated attempts

## 7. Detection DET-03 — Path-Like Input Attempt

### Objective

Detect path-like or traversal-style values supplied to
security-sensitive MCP tools.

### Example Patterns

```text
../
../../
..\ 
/etc/
/var/
C:\
```

### Detection Logic

Trigger when suspicious path patterns are observed in
tool arguments.

### Investigation

Review:

- Tool invoked
- Input value
- Identity
- Frequency
- Related resource access

### Response

- Reject the request
- Monitor the session
- Investigate related activity

### Limitation

The current `get_security_status` tool does not perform
filesystem access. This detection therefore identifies
suspicious input patterns rather than demonstrating a
successful filesystem traversal.

## 8. Detection DET-04 — Abnormal Tool Frequency

### Objective

Identify unusually frequent MCP tool invocations that may
indicate automation, abuse, or compromised credentials.

### Detection Signals

- High request rate
- Repeated identical calls
- Burst activity
- Requests outside expected operating patterns

### Investigation

Review:

- Identity
- Tool
- Request frequency
- Time window
- Result distribution

### Response

- Apply rate limiting
- Investigate identity
- Terminate suspicious session where appropriate

## 9. Detection DET-05 — Sensitive Tool Usage

### Objective

Detect execution of high-risk MCP tools or operations.

### Detection Signals

- Sensitive resource access
- Data export operations
- Administrative actions
- Credential-related operations
- High-impact tool invocation

### Investigation

Review:

- Identity
- Authorization scope
- Tool
- Arguments
- Target resource
- Result

### Response

- Require additional authorization where applicable
- Block high-risk operation
- Investigate activity

## 10. Detection DET-06 — Credential Anomaly

### Objective

Detect abnormal use of MCP credentials, tokens, or secrets.

### Detection Signals

- Unexpected credential usage
- Repeated authentication failures
- New source location
- Unusual access pattern
- Credential use outside approved workflow

### Investigation

Review:

- Credential identity
- Source
- Time
- Resource
- Historical activity

### Response

- Revoke credential
- Rotate secret
- Terminate affected sessions
- Investigate related activity

## 11. Detection DET-07 — Tool Registration Change

### Objective

Detect unauthorized creation, modification, or replacement
of MCP tools.

### Detection Signals

- New tool registration
- Tool version change
- Configuration modification
- Integrity failure
- Unexpected dependency change

### Investigation

Review:

- Change source
- Approver
- Tool version
- Integrity data
- Deployment history

### Response

- Disable untrusted tool
- Restore approved version
- Preserve evidence
- Investigate change

## 12. Detection DET-08 — Logging Failure

### Objective

Detect loss of telemetry required for MCP security
monitoring and investigation.

### Detection Signals

- Missing expected events
- Logging errors
- Unexpected event-volume reduction
- Telemetry gaps
- Logging configuration changes

### Investigation

Review:

- Logging configuration
- Server health
- Collection pipeline
- Last known event
- Configuration changes

### Response

- Restore logging
- Investigate telemetry gap
- Preserve available evidence
- Review activity during the gap

## 13. Detection DET-09 — Configuration Change

### Objective

Detect unauthorized modifications to MCP security
configuration.

### Detection Signals

- Allowlist changes
- Authorization changes
- Logging changes
- Tool configuration changes
- Security control disablement

### Investigation

Review:

- Changed setting
- Identity
- Time
- Previous configuration
- Change approval

### Response

- Roll back unauthorized change
- Disable affected capability
- Investigate change source

## 14. Detection DET-10 — Unusual Resource Access

### Objective

Detect MCP-driven access to resources outside the
expected security scope.

### Detection Signals

- Unexpected resource
- Unusual data volume
- Cross-boundary access
- Access outside normal workflow
- Repeated authorization failures

### Investigation

Review:

- Identity
- Tool
- Resource
- Authorization decision
- Data accessed
- Related network events

### Response

- Block access
- Revoke permissions where necessary
- Investigate affected resource
- Preserve evidence

## 15. Detection Correlation Model

Individual events should be correlated into a security
signal.

```text
Authentication
       ↓
Tool Invocation
       ↓
Input Validation
       ↓
Authorization
       ↓
Resource Access
       ↓
Telemetry
       ↓
Correlation
       ↓
Detection
       ↓
Alert
```

Correlation should consider:

- Identity
- Session
- Tool
- Input
- Resource
- Time
- Frequency
- Result

## 16. Detection Severity Model

| Severity | Meaning | Example |
|---|---|---|
| Low | Low-risk abnormal behavior | Single invalid input |
| Medium | Repeated suspicious activity | Repeated unknown inputs |
| High | Strong indicator of abuse | Repeated authorization failures |
| Critical | Potential compromise or major impact | Credential compromise with sensitive access |

Severity must be assigned using the available context rather
than a single event alone.

## 17. Alert Engineering Model

Every actionable alert should contain:

```text
Alert
 ↓
Identity
 ↓
Session
 ↓
Tool
 ↓
Input
 ↓
Resource
 ↓
Timestamp
 ↓
Detection Reason
 ↓
Recommended Response
```

## 18. Detection Test Mapping

| Test | Detection | Expected Signal |
|---|---|---|
| Unknown component | DET-02 | Allowlist denial |
| Empty input | DET-02 | Validation failure |
| Path-like input | DET-03 | Suspicious input pattern |
| Repeated denied requests | DET-01 | Authorization failure pattern |
| Tool invocation | LOG-01 | MCP tool telemetry |

## 19. Current Lab Detection Coverage

The current implementation provides observable telemetry
for:

- Tool invocations
- Authorized requests
- Unauthorized requests
- Empty input rejection
- Allowlist rejection
- Path-like input rejection

The current lab does not yet implement centralized SIEM
correlation or automated alert generation.

## 20. Engineering Principle

Detection engineering must connect security telemetry to
security decisions.

The monitoring chain should be:

```text
Event
   ↓
Context
   ↓
Correlation
   ↓
Detection
   ↓
Alert
   ↓
Investigation
   ↓
Response
   ↓
Evidence
```

A security event becomes useful only when the organization
can determine what happened, why it matters, and what action
should follow.