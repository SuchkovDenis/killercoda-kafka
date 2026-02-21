#!/bin/bash
docker ps --format '{{.Names}}' | grep -q kafka-ui
