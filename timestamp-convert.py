#!/opt/homebrew/anaconda3/bin/python

# Required parameters:
# @raycast.schemaVersion 1
# @raycast.title Timestamp Convert
# @raycast.mode fullOutput

# Optional parameters:
# @raycast.icon 🕰
# @raycast.argument1 { "type": "text", "placeholder": "Timestamp (e.g., 1712345678)", "optional": true }

# Documentation:
# @raycast.description Convert the given or current timestamp to all formats.
# @raycast.author wenkaiyn
# @raycast.authorURL https://raycast.com/wenkaiyn

import sys
from datetime import datetime, timezone
from email.utils import parsedate_to_datetime


def to_utc_datetime(timestamp_str: str) -> datetime:
    s = timestamp_str.strip()

    # Try parsing as Unix timestamp (seconds, milliseconds, microseconds, nanoseconds)
    try:
        ts = float(s)
        if 1e8 <= abs(ts) < 1e11:  # seconds
            return datetime.fromtimestamp(ts, tz=timezone.utc)
        elif 1e11 <= abs(ts) < 1e14:  # milliseconds
            return datetime.fromtimestamp(ts / 1e3, tz=timezone.utc)
        elif 1e14 <= abs(ts) < 1e17:  # microseconds
            return datetime.fromtimestamp(ts / 1e6, tz=timezone.utc)
        elif 1e17 <= abs(ts) < 1e20:  # nanoseconds
            return datetime.fromtimestamp(ts / 1e9, tz=timezone.utc)
    except ValueError:
        pass

    # Try ISO8601
    try:
        dt = datetime.fromisoformat(s)
        return dt.astimezone(timezone.utc) if dt.tzinfo else dt.replace(tzinfo=timezone.utc)
    except ValueError:
        pass

    # Try RFC2822
    try:
        dt = parsedate_to_datetime(s)
        return dt.astimezone(timezone.utc) if dt.tzinfo else dt.replace(tzinfo=timezone.utc)
    except (ValueError, TypeError):
        pass

    common_formats = [
        "%Y-%m-%d %H:%M:%S",
        "%Y/%m/%d %H:%M:%S",
        "%d-%m-%Y %H:%M:%S",
        "%d/%m/%Y %H:%M:%S",
        "%Y-%m-%d",
        "%Y/%m/%d",
        "%Y%m%d",
        "%Y%m%d%H%M%S",
    ]
    for fmt in common_formats:
        try:
            return datetime.strptime(s, fmt).replace(tzinfo=timezone.utc)
        except ValueError:
            pass

    simple_day_formats = [
        "%m-%d",
        "%m/%d",
        "%m%d",
    ]
    for fmt in simple_day_formats:
        try:
            return datetime.strptime(s, fmt).replace(year=datetime.now(timezone.utc).year, tzinfo=timezone.utc)
        except ValueError:
            pass

    raise ValueError(f"Unable to parse timestamp: {timestamp_str}")


if len(sys.argv) == 1 or not sys.argv[1]:
    dt = datetime.now(timezone.utc)
else:
    dt = to_utc_datetime(sys.argv[1])

# Unix timestamps
print(f'Unix Epoch Seconds:         \033[31m{int(dt.timestamp())}\033[0m')
print(f'Unix Epoch Milliseconds:    \033[31m{int(dt.timestamp() * 1000)}\033[0m')
print(f'Unix Epoch Microseconds:    \033[31m{int(dt.timestamp() * 1000000)}\033[0m')
print(f'Unix Epoch Nanoseconds:     \033[31m{int(dt.timestamp() * 1000000000)}\033[0m')
print()

# Datetime in UTC timezone
print(f'UTC Datetime:               \033[32m{dt.strftime("%Y-%m-%d %H:%M:%S")}\033[0m')
print(f'UTC Datetime in ISO8601:    \033[32m{dt.isoformat()}\033[0m')
print(f'UTC Datetime in RFC2822:    \033[32m{dt.strftime("%a, %d %b %Y %H:%M:%S %z")}\033[0m')
print()

# Datetime in local timezone
print(f'Local Datetime:             \033[34m{dt.astimezone().strftime("%Y-%m-%d %H:%M:%S")}\033[0m')
print(f'Local Datetime in ISO8601:  \033[34m{dt.astimezone().isoformat()}\033[0m')
print(f'Local Datetime in RFC2822:  \033[34m{dt.astimezone().strftime("%a, %d %b %Y %H:%M:%S %z")}\033[0m')
print()
