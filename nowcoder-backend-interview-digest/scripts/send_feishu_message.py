#!/usr/bin/env python3
"""Send a Feishu/Lark bot text message through an incoming webhook."""

from __future__ import annotations

import argparse
import base64
import hashlib
import hmac
import json
import os
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path


SKILL_DIR = Path(__file__).resolve().parents[1]
LOCAL_CONFIG = SKILL_DIR / "config" / "feishu-webhook.local.env"


def sign(timestamp: str, secret: str) -> str:
    string_to_sign = f"{timestamp}\n{secret}".encode("utf-8")
    digest = hmac.new(string_to_sign, b"", hashlib.sha256).digest()
    return base64.b64encode(digest).decode("utf-8")


def read_local_config() -> dict[str, str]:
    values: dict[str, str] = {}
    if not LOCAL_CONFIG.exists():
        return values
    for line in LOCAL_CONFIG.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        key = key.strip()
        value = value.strip().strip('"').strip("'")
        if key and value and "REPLACE_" not in value:
            values[key] = value
    return values


def parse_args() -> argparse.Namespace:
    local_config = read_local_config()
    parser = argparse.ArgumentParser(description="Send a Feishu bot text message.")
    parser.add_argument(
        "--webhook",
        default=os.environ.get("FEISHU_WEBHOOK_URL") or local_config.get("FEISHU_WEBHOOK_URL"),
        help="Feishu webhook URL. Overrides FEISHU_WEBHOOK_URL and config/feishu-webhook.local.env.",
    )
    parser.add_argument(
        "--secret",
        default=os.environ.get("FEISHU_WEBHOOK_SECRET") or local_config.get("FEISHU_WEBHOOK_SECRET"),
        help="Optional Feishu bot signing secret. Overrides FEISHU_WEBHOOK_SECRET and config/feishu-webhook.local.env.",
    )
    parser.add_argument("--text", required=True, help="Text message to send.")
    parser.add_argument("--timeout", type=float, default=15.0, help="HTTP timeout in seconds.")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    if not args.webhook:
        print(
            f"error: provide --webhook, FEISHU_WEBHOOK_URL, or configure {LOCAL_CONFIG}",
            file=sys.stderr,
        )
        return 2

    payload: dict[str, object] = {
        "msg_type": "text",
        "content": {"text": args.text},
    }
    if args.secret:
        timestamp = str(int(time.time()))
        payload["timestamp"] = timestamp
        payload["sign"] = sign(timestamp, args.secret)

    data = json.dumps(payload, ensure_ascii=False).encode("utf-8")
    request = urllib.request.Request(
        args.webhook,
        data=data,
        headers={"Content-Type": "application/json; charset=utf-8"},
        method="POST",
    )

    try:
        with urllib.request.urlopen(request, timeout=args.timeout) as response:
            body = response.read().decode("utf-8", errors="replace")
            status = response.status
    except urllib.error.HTTPError as exc:
        body = exc.read().decode("utf-8", errors="replace")
        print(json.dumps({"ok": False, "http_status": exc.code, "body": body}, ensure_ascii=False))
        return 1
    except urllib.error.URLError as exc:
        print(json.dumps({"ok": False, "error": str(exc.reason)}, ensure_ascii=False))
        return 1

    try:
        parsed = json.loads(body) if body else {}
    except json.JSONDecodeError:
        parsed = {"raw": body}

    code = parsed.get("code", parsed.get("StatusCode", 0))
    ok = status < 400 and code in (0, "0", None)
    print(json.dumps({"ok": ok, "http_status": status, "response": parsed}, ensure_ascii=False))
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
