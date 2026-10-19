# Design & Pseudocode Specification

## 1. Reaction Timer & High Score (R1 - R7)

WHILE True DO
    OUTPUT "Get ready..."
    SET led TO OFF
    SET delay TO RANDOM_FLOAT(2.0, 5.0)
    SET waited TO 0.0
    SET false_start TO FALSE

    // Watchful wait loop
    WHILE waited < delay DO
        IF button IS PRESSED THEN
            SET false_start TO TRUE
            EXIT WHILE
        END IF
        WAIT 0.01 seconds
        SET waited TO waited + 0.01
    END WHILE

    IF false_start == TRUE THEN
        OUTPUT "FALSE START"
        WAIT UNTIL button IS RELEASED
        CONTINUE TO NEXT LOOP
    END IF

    // Ready phase
    SET led TO ON
    SET start_time TO CURRENT_MONOTONIC_TIME()
    WAIT UNTIL button IS PRESSED
    SET reaction_time TO (CURRENT_MONOTONIC_TIME() - start_time) * 1000
    SET led TO OFF

    OUTPUT "Reaction: " + reaction_time + " ms"

    // High score check logic (R7)
    IF reaction_time < best_score OR best_score == 0 THEN
        SET best_score TO reaction_time
        OUTPUT "NEW HIGH SCORE!"
    END IF

    WAIT UNTIL button IS RELEASED
END WHILE

--------------------------------------------------

## 2. Patience Light (R8 - R9)

WHILE True DO
    OUTPUT "Hold button for 2 seconds..."
    SET led TO OFF
    WAIT UNTIL button IS PRESSED
    
    SET hold_start TO CURRENT_MONOTONIC_TIME()
    
    WHILE button IS PRESSED DO
        IF (CURRENT_MONOTONIC_TIME() - hold_start) >= 2.0 THEN
            EXIT WHILE
        END IF
        WAIT 0.05 seconds
    END WHILE
    
    IF (CURRENT_MONOTONIC_TIME() - hold_start) < 2.0 THEN
        OUTPUT "Released too early! Cancelled."
        WAIT 0.5 seconds
        CONTINUE TO NEXT LOOP
    END IF
    
    SET led TO ON
    OUTPUT "Success! Patience rewarded."
    WAIT 2.0 seconds
    SET led TO OFF
    WAIT UNTIL button IS RELEASED
END WHILE

--------------------------------------------------

## 3. Best of Five (R10 - R11)

SET scores TO EMPTY_LIST
SET target_rounds TO 5

WHILE LENGTH(scores) < target_rounds DO
    OUTPUT "Round " + (LENGTH(scores) + 1) + " - Get ready..."
    SET led TO OFF
    SET delay TO RANDOM_FLOAT(2.0, 5.0)
    SET waited TO 0.0
    SET false_start TO FALSE

    WHILE waited < delay DO
        IF button IS PRESSED THEN
            SET false_start TO TRUE
            EXIT WHILE
        END IF
        WAIT 0.01 seconds
        SET waited TO waited + 0.01
    END WHILE

    IF false_start == TRUE THEN
        OUTPUT "FALSE START! Round restarted."
        WAIT UNTIL button IS RELEASED
        CONTINUE TO NEXT LOOP
    END IF

    SET led TO ON
    SET start_time TO CURRENT_MONOTONIC_TIME()
    WAIT UNTIL button IS PRESSED
    SET reaction_time TO (CURRENT_MONOTONIC_TIME() - start_time) * 1000
    SET led TO OFF

    OUTPUT "Reaction: " + reaction_time + " ms"
    APPEND reaction_time TO scores

    WAIT UNTIL button IS RELEASED
    WAIT 1.0 seconds
END WHILE

SET best_time TO MINIMUM(scores)
SET avg_time TO AVERAGE(scores)

OUTPUT "SESSION COMPLETE!"
OUTPUT "Best Time: " + best_time + " ms"
OUTPUT "Average Time: " + avg_time + " ms"
