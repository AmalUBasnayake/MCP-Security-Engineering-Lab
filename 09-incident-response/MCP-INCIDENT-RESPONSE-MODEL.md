# MCP Incident Response Model

## 1. Purpose

This document defines the incident response model for the MCP security engineering environment.

The incident response lifecycle follows:

```text
Security Event
      ↓
Detection
      ↓
Alert
      ↓
Triage
      ↓
Investigation
      ↓
Containment
      ↓
Evidence Preservation
      ↓
Remediation
      ↓
Recovery
      ↓
Validation
      ↓
Lessons Learned
```

---

## 2. Incident Response Principles

MCP incident response must be identity-aware, evidence-driven, repeatable, auditable, traceable, and recoverable.

Response decisions should be based on validated security telemetry and documented evidence.

---

## 3. Incident Sources

| ID | Source | Example Signal |
|---|---|---|
| IR-01 | MCP Server | Authorization failure |
| IR-02 | Tool Invocation | Unauthorized tool request |
| IR-03 | Input Validation | Malicious or invalid input |
| IR-04 | Identity Layer | Authentication anomaly |
| IR-05 | Resource Layer | Unauthorized resource access |
| IR-06 | Logging Layer | Missing or abnormal telemetry |
| IR-07 | Configuration | Security control modification |
| IR-08 | Supply Chain | Untrusted tool or dependency |

---

## 4. Incident Classification

| Class | Description | Example |
|---|---|---|
| Low | Single low-impact security event | One invalid input |
| Medium | Repeated suspicious activity | Multiple denied requests |
| High | Significant unauthorized activity | Repeated authorization failures |
| Critical | Potential compromise or major impact | Credential compromise with sensitive access |

Severity should be determined using event context, scope, impact, and corroborating telemetry.

---

## 5. Incident Identification

An incident begins when security telemetry indicates activity that may violate an MCP security boundary.

```text
Tool Invocation
      ↓
Authorization Failure
      ↓
Repeated Attempts
      ↓
DET-01
      ↓
HIGH Severity Alert
```

---

## 6. Initial Triage

### 6.1 Validate the Alert

Confirm:

- Detection ID
- Detection name
- Severity
- Event type
- Timestamp
- Identity
- Tool
- Component
- Authorization decision
- Detection threshold

### 6.2 Determine Scope

```text
Who?       → Identity
What?      → Tool / component
When?      → Time range
How often? → Event frequency
Where?     → Resource / security boundary
Impact?    → Security property affected
```

### 6.3 Preserve Initial Evidence

```text
Alert
Telemetry
Timestamp
Identity
Tool
Component
Arguments
Decision
Detection Reason
Related Events
```

---

## 7. Investigation Model

The investigation should connect the complete MCP execution chain:

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
```

### 7.1 Identity Analysis

Review authentication context, recent successful activity, denied activity, and related sessions.

### 7.2 Tool Analysis

Review the tool, its authorization scope, registration state, and related tool activity.

### 7.3 Input Analysis

Review input values, validation and normalization results, suspicious patterns, and repeated values.

### 7.4 Resource Analysis

Review the target resource, authorization boundary, access result, data sensitivity, and related activity.

---

## 8. Containment

Containment should reduce ongoing risk while preserving evidence.

```text
Suspicious Activity
        ↓
Validate Scope
        ↓
Prevent Unauthorized Access
        ↓
Preserve Evidence
        ↓
Continue Investigation
```

Possible containment actions include maintaining authorization denial, restricting the affected identity or session, disabling an affected MCP capability, isolating a component, applying temporary access restrictions, and preserving telemetry.

---

## 9. Evidence Preservation

Preserve:

```text
Security Events
Detection Output
Alert Metadata
Identity Context
Tool Information
Input Data
Target Resource
Authorization Decision
Investigation Notes
Response Actions
Timestamps
```

Evidence chain:

```text
Event
  ↓
Detection
  ↓
Alert
  ↓
Investigation Record
  ↓
Response Record
  ↓
Validation Evidence
```

---

## 10. Eradication and Remediation

After containment, remediate the underlying security condition.

Potential actions include removing unauthorized configuration, revoking compromised credentials, restoring approved tool versions, correcting authorization policies, restoring secure logging, removing untrusted components, and patching affected dependencies.

Remediation must be validated before returning the system to normal operation.

---

## 11. Recovery

Recovery should restore normal operation while preserving security controls.

```text
Remediation Completed
       ↓
Security Controls Rechecked
       ↓
Approved Access Tested
       ↓
Monitoring Confirmed
       ↓
Detection Rules Revalidated
       ↓
Service Restored
```

---

## 12. Post-Incident Validation

A response is not complete until the security controls are revalidated.

```text
Control
   ↓
Security Test
   ↓
Expected Result
   ↓
Observed Result
   ↓
Evidence
   ↓
Final Status
```

Example:

```text
Unauthorized Component
        ↓
Authorization DENIED
        ↓
Telemetry Recorded
        ↓
DET-02 Triggered
        ↓
PB-02 Response
        ↓
Control Revalidated
```

---

## 13. Incident Record

| Field | Description |
|---|---|
| Incident ID | Unique incident identifier |
| Detection ID | Detection that generated the alert |
| Severity | Current incident severity |
| Identity | Identity associated with activity |
| Tool | MCP tool involved |
| Component | Target MCP component |
| Start Time | First observed event |
| End Time | Last observed event |
| Scope | Affected security boundary |
| Impact | Observed or potential impact |
| Containment | Actions performed |
| Evidence | Evidence references |
| Recovery | Recovery actions |
| Status | Current incident state |

---

## 14. Incident Status Model

```text
Detected
   ↓
Triaged
   ↓
Investigating
   ↓
Contained
   ↓
Remediated
   ↓
Recovering
   ↓
Validated
   ↓
Closed
```

An incident should not be marked **Closed** until the required validation and documentation are complete.

---

## 15. Automation Model

Automation can perform repeatable low-risk response tasks.

```text
Detection
    ↓
Decision
    ↓
Automation
    ↓
Containment Action
    ↓
Evidence Capture
    ↓
Notification
    ↓
Validation
```

Potential automated actions include creating an incident record, preserving telemetry, tagging the affected identity, triggering an investigation workflow, notifying security operations, and recording the response outcome.

High-impact actions should require appropriate authorization and change control.

---

## 16. DET-01 Response Mapping

```text
DET-01
   ↓
Repeated Authorization Failure
   ↓
Identity Investigation
   ↓
Tool / Component Analysis
   ↓
Telemetry Correlation
   ↓
Contain Unauthorized Activity
   ↓
Preserve Evidence
   ↓
Validate Authorization Controls
```

Associated playbook:

```text
PB-01 — Repeated Authorization Failure Response Playbook
```

---

## 17. DET-02 Response Mapping

```text
DET-02
   ↓
Unauthorized Component Access
   ↓
Validate Allowlist Decision
   ↓
Identify Requesting Identity
   ↓
Correlate Related Events
   ↓
Maintain Access Denial
   ↓
Preserve Evidence
   ↓
Validate Allowlist Enforcement
```

Associated playbook:

```text
PB-02 — Unauthorized Component Access Response Playbook
```

---

## 18. Current Lab Response Coverage

The current MCP security lab demonstrates:

- Authorization failure detection
- Unauthorized component detection
- Security telemetry generation
- Repeatable detection logic
- Response playbooks
- Evidence preservation requirements
- Post-response validation requirements

The lab currently models response workflows locally. Production integrations such as enterprise ticketing, centralized SIEM/SOAR platforms, identity-provider actions, and cloud-native containment are outside the current implementation scope.

---

## 19. Response Evidence Model

```text
Security Event
      ↓
Detection Output
      ↓
Incident Record
      ↓
Investigation
      ↓
Containment
      ↓
Evidence Preservation
      ↓
Recovery
      ↓
Validation
```

Every major response action should have an observable record where technically feasible.

---

## 20. Engineering Principle

Incident response must connect detection to controlled action.

```text
Observe
   ↓
Detect
   ↓
Triage
   ↓
Investigate
   ↓
Contain
   ↓
Remediate
   ↓
Recover
   ↓
Validate
   ↓
Learn
```

The objective is to ensure that an MCP security incident is not only detected, but also investigated, contained, evidenced, recovered, and validated through a repeatable engineering process.

---

## 21. Final Security Outcome

```text
Detection
   ↓
Decision
   ↓
Response
   ↓
Evidence
   ↓
Recovery
   ↓
Validation
   ↓
Continuous Improvement
```

**Incident Response Model Status: DEFINED**
