import server


def run_test(name: str, actual: str, expected: str) -> bool:
    passed = actual == expected

    if passed:
        print(f"[PASS] {name}")
    else:
        print(f"[FAIL] {name}")
        print(f"       Expected: {expected}")
        print(f"       Actual:   {actual}")

    return passed


def main() -> None:
    tests = [
        (
            "Approved component",
            server.get_security_status("mcp-server"),
            "Component 'mcp-server' is registered as an approved read-only security target.",
        ),
        (
            "Uppercase + whitespace normalization",
            server.get_security_status("  MCP-SERVER  "),
            "Component 'mcp-server' is registered as an approved read-only security target.",
        ),
        (
            "Unknown component rejection",
            server.get_security_status("unknown-component"),
            "DENIED: component is not in the approved allowlist.",
        ),
        (
            "Empty input rejection",
            server.get_security_status("   "),
            "DENIED: component cannot be empty.",
        ),
        (
            "Path-like input rejection",
            server.get_security_status("../../etc/passwd"),
            "DENIED: component is not in the approved allowlist.",
        ),
    ]

    results = [
        run_test(name, actual, expected)
        for name, actual, expected in tests
    ]

    passed = sum(results)
    total = len(results)

    print()
    print(f"Security test summary: {passed}/{total} passed.")

    if passed != total:
        raise SystemExit(1)


if __name__ == "__main__":
    main()