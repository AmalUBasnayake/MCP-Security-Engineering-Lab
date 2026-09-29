# PB-02 — Unauthorized Component Access Response Playbook

## 1. Purpose

This playbook defines the response procedure for **DET-02 — Unauthorized Component Access**.

The objective is to provide a repeatable workflow for investigating and responding to MCP authorization failures involving components outside the approved allowlist.

The response lifecycle is:

```text
Detection
   ↓
Alert Validation
   ↓
Context Collection
   ↓
Identity Analysis
   ↓
Component Validation
   ↓
Containment Decision
   ↓
Evidence Preservation
   ↓
Recovery
   ↓
Lessons Learned
```

---

## 2. Trigger

This playbook is triggered when:

```text
Detection ID      : DET-02
Detection Name    : Unauthorized Component Access
Severity          : HIGH
Condition         : Denied authorization request
                  : Target component not in approved allowlist
```

Example trigger:

```text
Identity   : test-identity
Component  : unknown-component
Decision   : DENIED
Reason     : component_not_in_allowlist
```

---

## 3. Detection Signal

The detection signal is generated when MCP security telemetry contains an authorization failure for a component that is not present in the approved component allowlist.

Example:

```text
Authorization Request
        ↓
Component Validation
        ↓
Component NOT in Allowlist
        ↓
Authorization Decision = DENIED
        ↓
DET-02
        ↓
HIGH Severity Alert
```

---

## 4. Initial Triage

The analyst should first confirm that the alert represents a genuine security event.

Review:

- Timestamp
- Identity
- Component
- Authorization decision
- Reason
- Event type
- Frequency of attempts
- Related MCP activity

Example:

```text
Timestamp  : 2026-09-28T15:00:00
Identity   : test-identity
Component  : unknown-component
Decision   : DENIED
Reason     : component_not_in_allowlist
```

### Triage Questions

1. Is the identity expected to access the MCP environment?
2. Is the requested component approved?
3. Is the component name valid?
4. Was the request intentionally denied?
5. Are there repeated attempts?
6. Are other suspicious events associated with the same identity?

---

## 5. Investigation

### 5.1 Identity Investigation

Determine:

- Identity associated with the request
- Whether the identity is known
- Whether the identity is expected to use the MCP server
- Whether recent activity from the identity is consistent with normal behavior

Record:

```text
Identity:
Expected:
Observed:
Assessment:
```

---

### 5.2 Component Investigation

Compare the requested component against the approved allowlist.

Approved example:

```text
AUTHORIZED_COMPONENTS = {
    "mcp-server"
}
```

Observed unauthorized component:

```text
unknown-component
```

If the component is not explicitly approved, treat the request as unauthorized.

---

### 5.3 Telemetry Investigation

Review the source telemetry:

```text
logs/security-events.jsonl
```

Look for:

- Repeated authorization failures
- Multiple unauthorized components
- Changes in identity
- Changes in request pattern
- Related security events

---

## 6. Containment

The MCP authorization control should remain enforced.

Do not add an unknown component to the allowlist merely to make the alert disappear.

Recommended containment principles:

```text
Unknown Component
        ↓
Deny Access
        ↓
Preserve Telemetry
        ↓
Investigate Identity
        ↓
Determine Legitimacy
```

If the activity is confirmed malicious or unauthorized:

- Maintain denial
- Restrict the associated identity if required
- Preserve relevant telemetry
- Escalate according to the incident process

---

## 7. Evidence Preservation

Preserve the following evidence:

```text
Detection output
Security telemetry
Timestamp
Identity
Requested component
Authorization decision
Reason
Detection ID
```

For this lab, the DET-02 validation evidence demonstrates:

```text
Telemetry events loaded : 3
Detection               : Unauthorized Component Access
Severity                : HIGH
Events                  : 3
Decision                : DENIED
Reason                  : component_not_in_allowlist
```

Evidence should be stored under:

```text
07-evidence/test-results/
```

---

## 8. Response Decision

Use the following decision model:

```text
Unauthorized Component Detected
              ↓
       Is request legitimate?
          ↙          ↘
        YES           NO
         ↓             ↓
Validate change     Maintain Denial
         ↓             ↓
Update allowlist    Investigate
if formally        identity/activity
approved
```

Any allowlist change must follow an explicit change-control process.

---

## 9. Recovery

If the activity is legitimate:

1. Confirm business/security requirement.
2. Validate the component.
3. Obtain appropriate approval.
4. Update the allowlist through controlled change management.
5. Re-test authorization.
6. Record the change.

If the activity is unauthorized:

1. Keep the component denied.
2. Continue monitoring the identity.
3. Preserve evidence.
4. Escalate when required.
5. Review related events.

---

## 10. Validation

After response actions, validate that the security control remains effective.

Expected secure behavior:

```text
Approved Component
        ↓
Authorization Allowed

Unauthorized Component
        ↓
Authorization Denied
        ↓
Telemetry Recorded
        ↓
DET-02 Generated
```

The detection should remain reproducible using controlled test telemetry.

---

## 11. Detection-to-Response Flow

```text
MCP Activity
     ↓
Authorization Failure
     ↓
Security Telemetry
     ↓
DET-02 Detection
     ↓
HIGH Severity Alert
     ↓
PB-02 Response Playbook
     ↓
Triage
     ↓
Investigation
     ↓
Containment
     ↓
Evidence Preservation
     ↓
Recovery / Escalation
     ↓
Validation
```

---

## 12. Analyst Checklist

```text
[ ] Confirm DET-02 alert
[ ] Validate timestamp
[ ] Identify requesting identity
[ ] Identify requested component
[ ] Confirm authorization decision
[ ] Confirm component is outside allowlist
[ ] Review related telemetry
[ ] Assess whether activity is legitimate
[ ] Maintain denial during investigation
[ ] Preserve evidence
[ ] Escalate if required
[ ] Validate control after response
[ ] Document final disposition
```

---

## 13. Engineering Principle

Unauthorized access should be handled through **deny-by-default authorization**, not through assumptions.

The security chain is:

```text
Identity
   ↓
Authorization
   ↓
Allowlist Validation
   ↓
Decision
   ↓
Telemetry
   ↓
Detection
   ↓
Response
   ↓
Evidence
```

A denied request is not merely an error message.

It is a security signal that can support:

- Detection
- Investigation
- Correlation
- Incident response
- Auditability
- Continuous security validation

---

## 14. Expected Outcome

A correctly implemented MCP security environment should ensure that:

```text
Approved Component
→ Authorized
→ Logged

Unauthorized Component
→ Denied
→ Logged
→ Detected
→ Investigated
→ Responded
→ Evidenced
```

**PB-02 Status: VALIDATED**
