import logging
import sys

from mcp.server import MCPServer
from mcp.types import ToolAnnotations


# -----------------------------------------------------------------------------
# Logging
# -----------------------------------------------------------------------------
# MCP stdio transport uses stdout for protocol messages.
# Therefore, operational logs are written to stderr.
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
    stream=sys.stderr,
)

logger = logging.getLogger("mcp-security-lab")


# -----------------------------------------------------------------------------
# MCP Server
# -----------------------------------------------------------------------------
mcp = MCPServer(
    "MCP Security Lab",
    instructions=(
        "This server exposes security-focused read-only tools. "
        "Tool input is validated before processing."
    ),
)


# -----------------------------------------------------------------------------
# Security Baseline
# -----------------------------------------------------------------------------
VALID_COMPONENTS = {
    "mcp-server",
    "tool-registry",
    "audit-logging",
}


# -----------------------------------------------------------------------------
# Tool: Get Security Status
# -----------------------------------------------------------------------------
@mcp.tool(
    title="Get Security Status",
    annotations=ToolAnnotations(
        read_only_hint=True,
        open_world_hint=False,
    ),
)
def get_security_status(component: str) -> str:
    """Return the security status of an approved MCP component."""

    normalized_component = component.strip().lower()

    logger.info(
        "Tool invocation: get_security_status | component=%s",
        normalized_component,
    )

    if not normalized_component:
        logger.warning("Rejected request: empty component")
        return "DENIED: component cannot be empty."

    if normalized_component not in VALID_COMPONENTS:
        logger.warning(
            "Rejected request: unauthorized component=%s",
            normalized_component,
        )
        return "DENIED: component is not in the approved allowlist."

    logger.info(
        "Authorized read-only request: component=%s",
        normalized_component,
    )

    return (
        f"Component '{normalized_component}' is registered "
        f"as an approved read-only security target."
    )


# -----------------------------------------------------------------------------
# Server Entry Point
# -----------------------------------------------------------------------------
if __name__ == "__main__":
    logger.info("Starting MCP Security Lab server")
    mcp.run(transport="stdio")