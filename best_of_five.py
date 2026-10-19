from gpiozero import LED, Button
from time import monotonic, sleep
from random import uniform

led = LED(17)
button = Button(27, bounce_time=0.05)

scores = []
target_rounds = 5

print(f"Starting Best of {target_rounds} Session...")

while len(scores) < target_rounds:
    round_num = len(scores) + 1
    print(f"\n--- Round {round_num} of {target_rounds} ---")
    
    led.off()
    print("Get ready...")
    delay = uniform(2.0, 5.0)
    waited = 0.0
    false_start = False
    
    while waited < delay:
        if button.is_pressed:
            false_start = True
            break
        sleep(0.01)
        waited += 0.01
        
    if false_start:
        print("FALSE START! Round restarted.")
        button.wait_for_release()
        continue  # Excluded from valid round count
        
    led.on()
    t0 = monotonic()
    button.wait_for_press()
    reaction = (monotonic() - t0) * 1000
    led.off()
    
    print(f"Reaction: {reaction:.0f} ms")
    scores.append(reaction)
    
    button.wait_for_release()
    sleep(1.0)

# Session summary outputs
best_time = min(scores)
avg_time = sum(scores) / len(scores)

print("\n==============================")
print("SESSION COMPLETE!")
print(f"Scores recorded: {[round(s, 1) for s in scores]}")
print(f"Best Time:   {best_time:.1f} ms")
print(f"Average Time: {avg_time:.1f} ms")
print("==============================")
