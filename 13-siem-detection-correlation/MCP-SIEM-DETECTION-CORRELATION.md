# MCP SIEM & Detection Correlation

## 1. Purpose

This document defines the SIEM and detection correlation model for the MCP security engineering environment.

The objective is to transform individual MCP security events into correlated, enriched, and actionable security signals.

The correlation lifecycle follows:

```text
MCP Event
    ↓
Telemetry Normalization
    ↓
Context Enrichment
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

---

## 2. SIEM Security Objectives

The monitoring and correlation layer should provide:

- Centralized security telemetry
- Event normalization
- Identity context
- Session context
- Tool context
- Resource context
- Cross-event correlation
- Alert enrichment
- Detection validation
- Investigation support
- Evidence traceability

A single event may have limited context. Correlation combines related events to produce a higher-confidence security signal.

---

## 3. Telemetry Sources

| ID | Source | Example Events |
|---|---|---|
| SIEM-01 | MCP Server | Tool invocation |
| SIEM-02 | Authorization Layer | ALLOW / DENY |
| SIEM-03 | Input Validation | Invalid or suspicious input |
| SIEM-04 | Identity Layer | Authentication events |
| SIEM-05 | Session Layer | Session creation or termination |
| SIEM-06 | Resource Layer | Resource access |
| SIEM-07 | Tool Supply Chain | Tool or dependency changes |
| SIEM-08 | Detection Engine | DET-01 / DET-02 alerts |
| SIEM-09 | Response Layer | Containment actions |

---

## 4. Event Normalization

Security events should use a consistent structure.

Recommended normalized event fields:

```text
Timestamp
Event ID
Event Type
Identity
Session ID
Client
Tool
Component
Resource
Action
Decision
Result
Reason
Source
Severity
```

Normalization model:

```text
Raw Event
   ↓
Field Extraction
   ↓
Value Normalization
   ↓
Common Event Schema
   ↓
Correlation
```

---

## 5. Common Event Schema

Example normalized authorization event:

```json
{
  "timestamp": "2026-09-28T15:00:00",
  "event_id": "EVT-AUTH-001",
  "event_type": "authorization_failure",
  "identity": "test-identity",
  "session_id": "session-001",
  "client": "mcp-client",
  "tool": "get_security_status",
  "component": "unknown-component",
  "decision": "DENIED",
  "reason": "component_not_in_allowlist",
  "source": "mcp-server",
  "severity": "HIGH"
}
```

The schema should preserve the original security context needed for investigation.

---

## 6. Event Enrichment

Correlation becomes more useful when events contain additional context.

Possible enrichment fields:

| Context | Example |
|---|---|
| Identity | `test-identity` |
| Session | `session-001` |
| Tool | `get_security_status` |
| Component | `unknown-component` |
| Resource | Security target |
| Decision | `DENIED` |
| Detection | `DET-02` |
| Severity | `HIGH` |
| First Seen | Event start |
| Last Seen | Event end |
| Count | Number of related events |

Enrichment model:

```text
Raw Security Event
       ↓
Identity Context
       ↓
Session Context
       ↓
Tool Context
       ↓
Resource Context
       ↓
Detection Context
       ↓
Enriched Security Event
```

---

## 7. Correlation Dimensions

Events should be correlated using relevant dimensions:

```text
Identity
Session
Tool
Component
Resource
Timestamp
Source
Decision
Event Type
```

Correlation should avoid relying on a single field when multiple context fields are available.

---

## 8. Temporal Correlation

Temporal correlation identifies events occurring within a defined time window.

Example:

```text
15:00  Authorization Failure
15:02  Authorization Failure
15:04  Authorization Failure
```

Within:

```text
5-minute window
```

Correlation:

```text
3 Related Failures
       ↓
Same Identity
       ↓
5-Minute Window
       ↓
DET-01
       ↓
HIGH Alert
```

---

## 9. Identity Correlation

Events from the same identity can reveal behavioral patterns.

Example:

```text
Identity: test-identity

Authorization DENIED
        ↓
Unknown Component
        ↓
Authorization DENIED
        ↓
Unknown Component
        ↓
Repeated Activity
        ↓
Detection
```

Identity correlation supports investigation of repeated or unusual activity.

---

## 10. Session Correlation

Session context helps connect events occurring within the same execution context.

```text
Session Created
      ↓
Tool Invocation
      ↓
Authorization Failure
      ↓
Second Authorization Failure
      ↓
Detection
      ↓
Session Review
```

A suspicious session should be reviewed for related successful and denied activity.

---

## 11. Tool Correlation

Tool-level correlation identifies abnormal usage patterns.

Example:

```text
Tool A
  ↓
Authorization Failure

Tool A
  ↓
Authorization Failure

Tool B
  ↓
Authorization Failure

       ↓

Potential Multi-Tool Abuse Pattern
```

This can identify behavior that may not be visible when each event is examined separately.

---

## 12. Detection Correlation Model

The correlation pipeline is:

```text
Event Collection
      ↓
Normalization
      ↓
Enrichment
      ↓
Grouping
      ↓
Correlation Rule
      ↓
Detection Signal
      ↓
Alert
```

Grouping may be based on:

- Identity
- Session
- Tool
- Component
- Resource
- Time window

---

## 13. Correlation Rule Model

A correlation rule should define:

```text
Rule ID
Detection Name
Data Source
Grouping Fields
Time Window
Threshold
Filter Conditions
Severity
Response
Evidence
```

Example:

```text
Rule ID       : CORR-01
Detection     : Repeated Authorization Failure
Group By      : Identity
Window        : 5 minutes
Threshold     : 3
Decision      : DENIED
Severity      : HIGH
Response      : PB-01
```

---

## 14. Correlation Rule — CORR-01

### Objective

Identify repeated authorization failures from the same identity within five minutes.

### Logic

```text
Event Type = authorization_failure
        +
Decision = DENIED
        +
Same Identity
        +
3 or more events
        +
5-minute window
        ↓
DET-01
        ↓
HIGH Alert
```

### Response

```text
DET-01
   ↓
PB-01
   ↓
Investigation
   ↓
Containment
   ↓
Evidence
```

---

## 15. Correlation Rule — CORR-02

### Objective

Identify unauthorized component access.

### Logic

```text
Event Type = authorization_failure
        +
Decision = DENIED
        +
Component NOT in allowlist
        ↓
DET-02
        ↓
HIGH Alert
```

### Response

```text
DET-02
   ↓
PB-02
   ↓
Investigation
   ↓
Containment
   ↓
Evidence
```

---

## 16. Multi-Signal Correlation

Higher-confidence detections can combine different event types.

Example:

```text
Authentication Failure
        ↓
Successful Authentication
        ↓
Repeated Authorization Failure
        ↓
Unauthorized Component Access
        ↓
Suspicious Session
        ↓
Correlated Alert
```

Multi-signal correlation should include only signals with a meaningful relationship.

---

## 17. Alert Enrichment

Every generated alert should contain enough context for initial investigation.

Recommended alert fields:

```text
Alert ID
Detection ID
Severity
Timestamp
First Seen
Last Seen
Identity
Session
Client
Tool
Component
Resource
Event Count
Decision
Reason
Correlation Rule
Recommended Response
Evidence Reference
```

Example:

```text
Detection ID   : DET-02
Severity       : HIGH
Identity       : test-identity
Component      : unknown-component
Event Count    : 3
Decision       : DENIED
Reason         : component_not_in_allowlist
```

---

## 18. Alert Lifecycle

```text
Generated
    ↓
Enriched
    ↓
Triaged
    ↓
Investigating
    ↓
Contained
    ↓
Resolved
    ↓
Validated
    ↓
Closed
```

Alert closure should require sufficient evidence and validation.

---

## 19. False Positive Handling

Correlation rules should minimize unnecessary alerts.

A potential false positive should be reviewed using:

```text
Identity
   ↓
Expected Behavior
   ↓
Tool
   ↓
Component
   ↓
Frequency
   ↓
Resource
   ↓
Context
```

Detection tuning should preserve meaningful security coverage.

---

## 20. Detection Tuning

Detection rules should be tested and tuned using controlled data.

Tuning objectives:

- Reduce irrelevant alerts
- Preserve true security signals
- Maintain explainable logic
- Avoid excessive thresholds
- Validate detection repeatability

Tuning cycle:

```text
Detection
   ↓
Test
   ↓
Review
   ↓
Tune
   ↓
Retest
   ↓
Validate
```

---

## 21. Investigation Workflow

When a correlated alert is generated:

### Step 1 — Identify the Detection

Record:

```text
Detection ID
Correlation Rule
Severity
Timestamp
```

### Step 2 — Identify the Identity

Review:

```text
Identity
Session
Client
Authentication Context
```

### Step 3 — Review Related Events

```text
Previous Events
      ↓
Triggering Events
      ↓
Subsequent Events
```

### Step 4 — Determine Scope

Review:

- Tools
- Components
- Resources
- Sessions
- Identities
- Time range

---

## 22. SOC Investigation View

The preferred investigation sequence is:

```text
Alert
  ↓
Identity
  ↓
Session
  ↓
Tool
  ↓
Component
  ↓
Resource
  ↓
Event Timeline
  ↓
Detection Reason
  ↓
Response
```

This provides a structured path from alert to security decision.

---

## 23. Response Integration

The correlation layer connects to response playbooks:

| Detection | Correlation | Playbook |
|---|---|---|
| DET-01 | CORR-01 | PB-01 |
| DET-02 | CORR-02 | PB-02 |

Response chain:

```text
Telemetry
    ↓
Correlation
    ↓
Detection
    ↓
Alert
    ↓
Playbook
    ↓
Investigation
    ↓
Containment
    ↓
Evidence
```

---

## 24. Evidence Mapping

Correlation evidence should include:

```text
Source Events
Normalized Events
Correlation Rule
Detection Output
Alert Metadata
Investigation Record
Response Record
Validation Result
```

Recommended evidence path:

```text
13-siem-detection-correlation/
└── evidence/
```

Evidence should preserve the relationship between source events and the final alert.

---

## 25. Detection Test Matrix

| Test ID | Scenario | Expected Detection |
|---|---|---|
| CT-01 | Three denied requests from same identity | DET-01 |
| CT-02 | Unknown component denied | DET-02 |
| CT-03 | Multiple unauthorized components | DET-02 + correlation |
| CT-04 | Successful request after repeated failures | Enriched identity timeline |
| CT-05 | Multi-signal suspicious activity | Correlated alert |
| CT-06 | Missing telemetry | Monitoring investigation |
| CT-07 | Unexpected tool activity | Tool correlation signal |

---

## 26. Current Lab Implementation

The current MCP lab provides:

- MCP security telemetry
- Authorization events
- Identity context
- Detection rules
- DET-01 repeated failure detection
- DET-02 unauthorized component detection
- Response playbooks
- Evidence mapping

The current implementation uses local telemetry and Python-based detection logic.

Production SIEM features such as centralized ingestion, distributed correlation, enterprise case management, UEBA, or cloud-native analytics are outside the current implementation scope.

---

## 27. Validation Model

The SIEM and correlation layer should be validated through:

```text
Telemetry
    ↓
Normalization
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

A correlation rule is considered validated only when its expected signal can be reproduced from controlled telemetry.

---

## 28. Engineering Principle

Individual events provide facts.

Correlation provides security context.

Detection converts correlated context into an actionable signal.

The complete chain is:

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

A strong monitoring system should explain why an alert was generated and preserve the events that support that decision.

---

## 29. Final Security Outcome

The MCP SIEM and detection correlation objective is:

```text
Observable Events
      ↓
Normalized Telemetry
      ↓
Context Enrichment
      ↓
Correlated Activity
      ↓
Actionable Detection
      ↓
Enriched Alert
      ↓
SOC Investigation
      ↓
Controlled Response
      ↓
Traceable Evidence
```

**SIEM & Detection Correlation Model Status: DEFINED**
