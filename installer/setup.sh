#!/usr/bin/env bash
set -e

# Basic setup script for DrBimmer OS

if ! command -v docker > /dev/null; then
  echo "Docker is required. Please install Docker." >&2
  exit 1
fi

if ! command -v docker-compose > /dev/null; then
  echo "Docker Compose is required. Please install docker-compose." >&2
  exit 1
fi

echo "Starting DrBimmer OS containers..."
docker-compose up -d

echo "Initialization complete. Access the system via https://localhost"
