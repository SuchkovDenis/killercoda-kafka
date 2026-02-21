#!/bin/bash
docker ps --format '{{.Names}}' | grep -q kafka-1 && docker ps --format '{{.Names}}' | grep -q kafka-2 && docker ps --format '{{.Names}}' | grep -q kafka-3
