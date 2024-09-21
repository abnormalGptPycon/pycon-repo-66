from typing import Any, Dict
import re

def traverse_json(json_obj: Dict[str, Any], path: str) -> Any:
  pass


if __name__ == "__main__":
  sample_input = {"a": {"b": {"c": 42}}}
  sample_path = "a.b.c"
  sample_expected_output = 42

  output = traverse_json(sample_input, sample_path)
  assert output == sample_expected_output
  print("Passed sanity check!")
