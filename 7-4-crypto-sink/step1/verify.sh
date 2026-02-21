#!/bin/bash
docker exec postgres psql -U kafka -d crypto -c "\dt" 2>/dev/null | grep -q crypto_analytics
