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

tell application "Google Chrome"
    activate
    if isRunning and (count of windows) = 0 then
        make new window
    else
        tell window 1
            make new tab at end of tabs
        end tell
    end if
end tell

tell application "System Events"
    keystroke (key code 53) -- Press Escape key
    tell process "Google Chrome"
        set frontmost to true
        keystroke "l" using command down -- Press Command+L to focus address bar
    end tell
end tell
