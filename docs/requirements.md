| ID | Requirement / Rule | Acceptance Criterion | Verification Result |
| :--- | :--- | :--- | :--- |
| **R1** | The system shall display a prompt and turn off the LED when starting a round. | Watched 3 round starts: LED turns off and message prints. | Pass |
| **R2** | The system shall wait a random delay between 2.0 and 5.0 seconds before lighting up. | Stopwatch timed 5 rounds: delays fell between 2.4s and 4.7s. | Pass |
| **R3** | The system shall record reaction time in milliseconds when the button is pressed after the LED turns on. | Pressed after ~1s: printed a plausible millisecond value. | Pass |
| **R4** | The system shall detect a false start and restart if the button is pressed during the random delay. | Pressed early twice: printed "FALSE START" and restarted round. | Pass |
| **R5** | The system measurement error shall be within ±100 ms. | Argued from the error budget (debounce and polling intervals). | Argued, not measured |
| **R6** | The system shall run continuously in a loop until interrupted by the user. | Played 3 rounds, then exited cleanly with Ctrl+C. | Pass |
| **R7** | When a round ends with a valid press, if the elapsed time is less than any previous time recorded in the session, the system shall print `NEW HIGH SCORE!` alongside the time. | Completed two rounds where the second press was faster: verified message appeared only on the second attempt. | Pass |
