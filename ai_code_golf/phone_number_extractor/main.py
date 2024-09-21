from typing import List


def extract_international_phone_numbers(text: str) -> List[str]:
  # Populate this function
  pass


if __name__ == "__main__":
  sample_input = "Call us at +1-800-555-1234 ext123 or +44 20.7946 0958#4567."
  sample_extracted = ["+1-800-555-1234", "+44 20.7946 0958"]

  sample_output = extract_international_phone_numbers(sample_input)
  assert sample_output == sample_extracted, f"Expected {sample_extracted}, but got {sample_output}"
  print("Passed sanity check!")
