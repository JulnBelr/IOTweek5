from gpiozero import LED, Button
from time import monotonic, sleep
from random import uniform

led = LED(17)
button = Button(27, bounce_time=0.05)

best_score = float('inf')  # Tracks the best reaction time of the session

while True:                                   # R6
    led.off()                                 # R1
    print("Get ready...")                     # R1
    delay = uniform(2.0, 5.0)                 # R2
    waited = 0.0
    false_start = False
    
    while waited < delay:                     # the watchful wait
        if button.is_pressed:
            false_start = True
            break                             # EXIT WHILE
        sleep(0.01)
        waited = waited + 0.01
        
    if false_start:                           # R4
        print("FALSE START")
        button.wait_for_release()
        continue                              # next round
        
    led.on()                                  # R2 completed
    t0 = monotonic()
    button.wait_for_press()                   # R3
    reaction = (monotonic() - t0) * 1000
    led.off()
    
    print(f"Reaction: {reaction:.0f} ms")     # R3

    # --- R7 High Score Feature ---
    if reaction < best_score:
        best_score = reaction
        print("NEW HIGH SCORE!")
    # -----------------------------

    button.wait_for_release()
