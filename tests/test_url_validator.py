"""Tests for the URL validation helper."""

from src.validators.url_validator import validate_url


def test_validate_url_accepts_https_url():
    """A standard HTTPS URL should be accepted."""
    assert validate_url("https://example.com") is True


def test_validate_url_accepts_http_url():
    """A standard HTTP URL should also be accepted."""
    assert validate_url("http://example.com") is True


def test_validate_url_rejects_empty_string():
    """An empty string should not be treated as a valid URL."""
    assert validate_url("") is False


def test_validate_url_rejects_none():
    """A None value should be handled safely and rejected."""
    assert validate_url(None) is False


def test_validate_url_rejects_non_http_protocols():
    """URLs with unsupported schemes such as FTP should be rejected."""
    assert validate_url("ftp://example.com") is False


def test_validate_url_rejects_malformed_string():
    """Plain text without URL structure should be rejected."""
    assert validate_url("hello world") is False
