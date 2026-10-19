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
