# Execution Trace Table

This trace table walks through the state variables during a round of the reaction timer (`reaction.py`), showing both a false start scenario and a valid reaction scenario.

| Step | Current State / Event | `delay` | `waited` | `button.is_pressed` | `false_start` | System Action / Output |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **1** | Round starts, LED off | 3.5s | 0.0s | `False` | `False` | Prints "Get ready...", enters watchful wait loop. |
| **2** | Polling loop step 1 | 3.5s | 0.01s | `False` | `False` | Sleeps 10ms, increments `waited`. |
| **3** | Player presses early | 3.5s | 1.25s | `True` | `True` | `false_start` set to `True`, breaks out of wait loop. |
| **4** | False start handled | 3.5s | 1.25s | `True` | `True` | Prints "FALSE START", waits for release, `continue`s round. |
| **5** | *New Round* - Waiting | 2.8s | 0.0s | `False` | `False` | Starts fresh round, waits out random delay successfully. |
| **6** | LED turns on | 2.8s | 2.8s | `False` | `False` | `led.on()`, starts monotonic timer (`t0`). |
| **7** | Player presses button | 2.8s | N/A | `True` | `False` | Calculates reaction time, turns LED off. |
| **8** | Output & High Score | N/A | N/A | `True` | `False` | Prints reaction in ms, checks `best_score`, prints "NEW HIGH SCORE!" if applicable. |
