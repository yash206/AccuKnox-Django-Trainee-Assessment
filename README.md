# AccuKnox Django Trainee Assignment

## 🔧 App 1 – Synchronous Signal Execution

**Question:** Do Django signals block the main thread?  
**Answer:** Yes — by default, signals run synchronously and block the caller.

This is demonstrated by placing an artificial delay (`time.sleep(5)`) inside the signal. The view waits until the signal is finished before sending a response.

**How to test:**

- Visit: `/app1/place-order/`
- The UI will show a confirmation message.
- Check the terminal to see logs with the delay clearly showing the signal is blocking.

---

## 🧵 App 2 – Signal & Thread Relationship

**Question:** Do Django signals run in the same thread as the view?  
**Answer:** Yes — they share the same thread by default.

I log the thread ID inside both the view and the signal. Since they match, it's confirmed that the signal doesn't start a separate thread.

**How to test:**

- Visit: `/app2/thread-test/`
- The UI shows both thread IDs.
- Console output confirms they are the same.

---

## 💾 App 3 – Same Database Transactions

**Question:** Do Django signals run in the same DB transaction as the caller?  
**Answer:** Yes — by default, signals are executed within the same database transaction.

To prove it, we check if the transaction is still open using `transaction.get_autocommit()` from inside the signal. The result is printed to the terminal.

**How to test:**

- Visit: `/app3/save/`
- UI will show example console logs.
- Terminal logs show the signal sees the transaction as active.

## 🧑‍💻 App 4 — Custom Iterable Rectangle Class

- **File**: `app4.py`
- **Description**: A basic Python class `Rectangle` that takes `length` and `width`, and supports iteration.
