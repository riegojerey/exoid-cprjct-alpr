#!/usr/bin/with-contenv bashio

# Log a message to show the script is running
echo "Starting ALPR Watched Plates Manager Add-on..."

# Ensure configuration directories exist
mkdir -p /data

# Start Flask server
python /app/server.py







