"""
DET-02 — Unauthorized Component Access Detection

Purpose:
    Detect denied MCP authorization attempts targeting components that are
    outside the approved component allowlist.

Telemetry source:
    ../logs/security-events.jsonl

Detection logic:
    1. Load JSONL security telemetry.
    2. Identify authorization_failure events.
    3. Require a DENIED authorization decision.
    4. Identify components outside the approved allowlist.
    5. Generate a HIGH-severity alert with supporting event evidence.
"""

import json
from pathlib import Path
from typing import Any


# ============================================================
# DET-02 — Unauthorized Component Access
# ============================================================

DETECTION_ID = "DET-02"
DETECTION_NAME = "Unauthorized Component Access"
SEVERITY = "HIGH"


# ============================================================
# Detection Configuration
# ============================================================

AUTHORIZED_COMPONENTS = {
    "mcp-server",
}

UNAUTHORIZED_EVENT_TYPE = "authorization_failure"
DENIED_DECISION = "DENIED"


# ============================================================
# Telemetry Loading
# ============================================================

def load_events(log_file: Path) -> list[dict[str, Any]]:
    """
    Load security telemetry from a JSON Lines (.jsonl) file.

    Invalid or empty lines are skipped so that one malformed event
    does not stop the entire detection process.
    """

    events: list[dict[str, Any]] = []

    if not log_file.exists():
        return events

    try:
        with log_file.open("r", encoding="utf-8") as handle:
            for line_number, line in enumerate(handle, start=1):
                line = line.strip()

                if not line:
                    continue

                try:
                    event = json.loads(line)
                except json.JSONDecodeError:
                    print(
                        f"[WARNING] Invalid JSON skipped "
                        f"at line {line_number}."
                    )
                    continue

                if isinstance(event, dict):
                    events.append(event)

    except OSError as exc:
        print(f"[ERROR] Unable to read telemetry file: {exc}")

    return events


# ============================================================
# Normalization
# ============================================================

def normalize_component(component: Any) -> str:
    """
    Normalize component values before authorization comparison.
    """

    if not isinstance(component, str):
        return ""

    return component.strip().lower()


# ============================================================
# Detection Logic
# ============================================================

def detect_unauthorized_component_access(
    events: list[dict[str, Any]],
) -> list[dict[str, Any]]:
    """
    Return events representing denied access attempts against
    components outside the approved component allowlist.
    """

    alerts: list[dict[str, Any]] = []

    for event in events:
        event_type = str(event.get("event_type", "")).strip().lower()
        decision = str(event.get("decision", "")).strip().upper()
        component = normalize_component(event.get("component"))

        # Only process authorization failure telemetry.
        if event_type != UNAUTHORIZED_EVENT_TYPE:
            continue

        # Detection requires an explicit denied decision.
        if decision != DENIED_DECISION:
            continue

        # Empty component values are not treated as component-access
        # attempts by this detection.
        if not component:
            continue

        # Approved components are excluded.
        if component in AUTHORIZED_COMPONENTS:
            continue

        alerts.append(event)

    return alerts


# ============================================================
# Evidence Rendering
# ============================================================

def print_alerts(alerts: list[dict[str, Any]]) -> None:
    """
    Render detection results in a human-readable evidence format.
    """

    if not alerts:
        print()
        print("[INFO] No unauthorized component access detected.")
        print("Status       : NO ALERT")
        return

    print()
    print("[ALERT] Unauthorized component access detected")
    print(f"Detection ID : {DETECTION_ID}")
    print(f"Severity     : {SEVERITY}")
    print(f"Events       : {len(alerts)}")
    print()

    for index, event in enumerate(alerts, start=1):
        print(f"Event {index}")
        print(f"  Timestamp : {event.get('timestamp', 'N/A')}")
        print(f"  Identity  : {event.get('identity', 'N/A')}")
        print(f"  Component : {event.get('component', 'N/A')}")
        print(f"  Decision  : {event.get('decision', 'N/A')}")
        print(f"  Reason    : {event.get('reason', 'N/A')}")
        print()

    print("Status       : ALERT")


# ============================================================
# Main Detection Runner
# ============================================================

def main() -> None:
    """
    Execute DET-02 against the MCP security telemetry source.
    """

    log_file = (
        Path(__file__).resolve().parent.parent
        / "logs"
        / "security-events.jsonl"
    )

    print("=" * 70)
    print(f"{DETECTION_ID} — {DETECTION_NAME}")
    print("=" * 70)
    print(f"Log source   : {log_file}")
    print(f"Severity     : {SEVERITY}")
    print(
        "Allowlist    : "
        + ", ".join(sorted(AUTHORIZED_COMPONENTS))
    )
    print()

    events = load_events(log_file)

    print(f"Telemetry events loaded: {len(events)}")

    alerts = detect_unauthorized_component_access(events)

    print_alerts(alerts)


# ============================================================
# Entry Point
# ============================================================

if __name__ == "__main__":
    main()