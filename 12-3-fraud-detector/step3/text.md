# Правила обнаружения

**TODO 3** — `check_high_amount`:
```python
def check_high_amount(user_id):
    history = user_history[user_id]
    total = sum(a for _, a in history)
    if total > MAX_AMOUNT_PER_10_MIN:
        return {'rule': 'high_amount', 'total_amount': total,
                'window_minutes': 10, 'transaction_count': len(history)}
    return None
```{{copy}}

**TODO 4** — `check_high_frequency`:
```python
def check_high_frequency(user_id):
    cutoff = time.time() - WINDOW_1_MIN
    recent = sum(1 for ts, _ in user_history[user_id] if ts >= cutoff)
    if recent > MAX_TRANSACTIONS_PER_MIN:
        return {'rule': 'high_frequency', 'transaction_count': recent,
                'window_minutes': 1}
    return None
```{{copy}}
