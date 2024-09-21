from typing import Optional


def clean_url(raw_url: str) -> Optional[str]:
  # Populate this function
  pass


if __name__ == "__main__":
  sample_url = "example.com/path/to/resource"
  sample_expected = "http://example.com/path/to/resource"
  result = clean_url(sample_url)
  assert result == sample_expected, f"Expected {sample_expected} but got {result}"
  print("Passed sanity check!")
