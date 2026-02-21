#!/bin/bash
grep -q "Consumer({" /root/fraud_detector.py && grep -q "Producer({" /root/fraud_detector.py
