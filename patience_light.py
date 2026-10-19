from gpiozero import LED, Button
from time import sleep, monotonic

led = LED(17)
button = Button(27, bounce_time=0.05)

while True:
    led.off()
    print("Hold button for 2 seconds...")
    button.wait_for_press()
    
    start_hold = monotonic()
    
    # Monitor the button state while held
    while button.is_pressed:
        if monotonic() - start_hold >= 2.0:
            break
        sleep(0.05)
    
    # Check if released before 2 seconds
    if not button.is_pressed and (monotonic() - start_hold) < 2.0:
        print("Released too early! Cancelled.")
        sleep(0.5)
        continue
        
    # Success: held long enough
    led.on()
    print("Success! Patience rewarded.")
    sleep(2.0)
    led.off()
    button.wait_for_release()
