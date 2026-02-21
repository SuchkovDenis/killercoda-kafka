#!/bin/bash
curl -s http://localhost:8081/subjects 2>/dev/null | grep -q orders-value
