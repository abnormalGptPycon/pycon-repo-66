from typing import Dict, Optional
from collections import deque
from typing import Dict, Optional

# Define the function to detect the pattern.
def detect_security_alert(event: Dict[str, str], user_events: Dict[str, deque]) -> Optional[Dict[str, str]]:
    pass

# Initialize a dictionary to store the events for each user
user_events = {}
# Example usage
log_stream = [
    {'user_id': 'user1', 'timestamp': '2023-09-16T12:07:00+00:00', 'status': 'failure'},
    {'user_id': 'user1', 'timestamp': '2023-09-16T12:08:00+00:00', 'status': 'success'},
    {'user_id': 'user1', 'timestamp': '2023-09-16T12:05:00+00:00', 'status': 'failure'},
    {'user_id': 'user1', 'timestamp': '2023-09-16T12:00:00+00:00', 'status': 'failure'}
]

for event in log_stream:
    alert = detect_security_alert([event])
    if alert:
        print(alert)




if __name__ == "__main__":
  sample_log_stream = [
    {"user_id": "user0", "timestamp": "2023-09-16T12:00:00+00:00", "status": "failure"},
    {"user_id": "user0", "timestamp": "2023-09-16T12:05:00+00:00", "status": "failure"},
    {"user_id": "user0", "timestamp": "2023-09-16T12:07:00+00:00", "status": "failure"},
    {"user_id": "user0", "timestamp": "2023-09-16T12:08:00+00:00", "status": "success"},
  ]
  sample_expected_output = [
    None,
    None,
    None,
    {"user_id": "user0", "timestamp": "2023-09-16T12:08:00+00:00"},
  ]

  for i, ev in enumerate(sample_log_stream):
    alert = detect_security_alert(ev)
    assert (
      alert == sample_expected_output[i]
    ), f"Expected {sample_expected_output[i]}, but got {alert}"

  print("Passed sanity check!")
