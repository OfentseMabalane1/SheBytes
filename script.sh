
#!/bin/bash

# Start ngrok, display output on the terminal, and log it to a file
C:/Users/Ammu/ngrok-v3-stable-windows-amd64/ngrok.exe http 80 | tee ngrok.log &

# Wait for ngrok to initialize
sleep 3

# Extract the public URL from the log file and save it to a file
grep -o "https://[0-9a-z]*\.ngrok.io" ngrok.log > ngrok_url.txt

# Optionally, print the URL to the terminal
cat ngrok_url.txt
