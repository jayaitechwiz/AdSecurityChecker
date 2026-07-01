"""Validate HTTP and HTTPS URLs without performing network checks."""

from urllib.parse import urlparse
    

def validate_url(url):
    """Return True when the provided value is a valid HTTP or HTTPS URL.

    The function only checks the URL structure and does not perform any
    network, DNS, redirect, or certificate validation.
    """
    # Reject non-string values and empty input early.
    if not isinstance(url, str):
        return False

    candidate = url.strip()
    if not candidate:
        return False

    try:
        # Parse the URL and require an HTTP or HTTPS scheme.
        parsed = urlparse(candidate)
        if parsed.scheme not in {"http", "https"}:
            return False

        # Require a host name so the URL is structurally complete.
        if not parsed.netloc:
            return False

        hostname = parsed.hostname
        if not hostname:
            return False

        # Reject obvious whitespace issues in the host portion.
        if any(char.isspace() for char in hostname):
            return False

        return True
    except (TypeError, ValueError):
        # Return False instead of raising for malformed input.
        return False
