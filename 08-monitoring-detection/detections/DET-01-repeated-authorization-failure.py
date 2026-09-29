"""
DET-01 — Repeated Authorization Failure Detection

Purpose:
    Detect repeated denied MCP authorization attempts within
    a defined time window.

Detection model:

    Authorization Failure
            ↓
       Same Identity
            ↓
      Multiple Attempts
            ↓
     Detection Threshold
            ↓
          Alert
"""

from __future__ import annotations

from collections import defaultdict
from datetime import datetime, timedelta
from pathlib import Path
import json


# ------------------------------------------------------------
# Detection Configuration
# ------------------------------------------------------------

THRESHOLD = 3
WINDOW_MINUTES = 5

DETECTION_ID = "DET-01"
DETECTION_NAME = "Repeated Authorization Failure"


# ------------------------------------------------------------
# Event Loading
# ------------------------------------------------------------

def load_events(log_file: Path) -> list[dict]:
    """
    Load JSONL security events from the telemetry file.
    """

    events = []

    if not log_file.exists():
        return events

    with log_file.open("r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()

            if not line:
                continue

            try:
                events.append(json.loads(line))
            except json.JSONDecodeError:
                print(f"[WARNING] Invalid telemetry record: {line}")

    return events


# ------------------------------------------------------------
# Detection Logic
# ------------------------------------------------------------

def detect_repeated_authorization_failures(
    events: list[dict],
) -> list[dict]:
    """
    Detect repeated authorization failures from the same identity
    within the configured detection window.
    """

    failures_by_identity = defaultdict(list)

    for event in events:

        if event.get("decision") != "DENIED":
            continue

        if event.get("event_type") != "authorization_failure":
            continue

        identity = event.get("identity", "unknown")

        try:
            timestamp = datetime.fromisoformat(
                event["timestamp"]
            )
        except (KeyError, ValueError):
            continue

        failures_by_identity[identity].append(
            {
                "timestamp": timestamp,
                "event": event,
            }
        )

    alerts = []

    for identity, failures in failures_by_identity.items():

        failures.sort(key=lambda item: item["timestamp"])

        for index, current in enumerate(failures):

            window_start = current["timestamp"] - timedelta(
                minutes=WINDOW_MINUTES
            )

            matching_failures = [
                item
                for item in failures[: index + 1]
                if item["timestamp"] >= window_start
            ]

            if len(matching_failures) >= THRESHOLD:

                alerts.append(
                    {
                        "detection_id": DETECTION_ID,
                        "detection_name": DETECTION_NAME,
                        "severity": "HIGH",
                        "identity": identity,
                        "attempt_count": len(matching_failures),
                        "window_minutes": WINDOW_MINUTES,
                        "first_seen": matching_failures[0]["timestamp"].isoformat(),
                        "last_seen": matching_failures[-1]["timestamp"].isoformat(),
                        "status": "ALERT",
                    }
                )

                break

    return alerts


# ------------------------------------------------------------
# Main Detection Runner
# ------------------------------------------------------------

def main() -> None:

    log_file = (
        Path(__file__).resolve().parent.parent
        / "logs"
        / "security-events.jsonl"
    )

    print("=" * 70)
    print(f"{DETECTION_ID} — {DETECTION_NAME}")
    print("=" * 70)

    print(f"Log source : {log_file}")
    print(f"Threshold  : {THRESHOLD} failures")
    print(f"Window     : {WINDOW_MINUTES} minutes")

    print()

    events = load_events(log_file)

    print(f"Telemetry events loaded: {len(events)}")
    print()

    alerts = detect_repeated_authorization_failures(events)

    if alerts:

        for alert in alerts:

            print("[ALERT] Repeated authorization failure detected")
            print(f"Detection ID : {alert['detection_id']}")
            print(f"Severity     : {alert['severity']}")
            print(f"Identity     : {alert['identity']}")
            print(f"Attempts     : {alert['attempt_count']}")
            print(f"Window       : {alert['window_minutes']} minutes")
            print(f"First Seen   : {alert['first_seen']}")
            print(f"Last Seen    : {alert['last_seen']}")
            print(f"Status       : {alert['status']}")
            print()

    else:

        print("[INFO] No repeated authorization failure detected.")

if __name__ == "__main__":
    main()