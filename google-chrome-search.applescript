#!/usr/bin/osascript

# Required parameters:
# @raycast.schemaVersion 1
# @raycast.title Google Chrome Search
# @raycast.mode compact

# Optional parameters:
# @raycast.icon 🔎

# Documentation:
# @raycast.author wenkaiyn
# @raycast.authorURL https://raycast.com/wenkaiyn

tell application "System Events"
    set isRunning to (count of (application processes whose name is "Google Chrome")) > 0
end tell

if isRunning then
    tell application "Google Chrome"
        activate
        if (count of windows) = 0 then
            make new window
        else
            tell window 1
                make new tab at end of tabs
            end tell
        end if
    end tell
else
    tell application "Google Chrome"
        activate
        make new window
    end tell
end if
