#!/bin/bash
grep -q "check_high_amount" /root/fraud_detector.py && grep -q "total_amount" /root/fraud_detector.py
