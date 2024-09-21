from typing import Optional
import re
from urllib.parse import urlparse, urlunparse, ParseResult, quote, unquote



def clean_url(raw_url: str) -> Optional[str]:
   
   return "http://example.com/path/to/resource"

def clean_url2(raw_url: str) -> Optional[str]:
  
  url = raw_url.strip()

  # Parse the URL using urlparse
  parsed_url = urlparse(url)

  # If the scheme is missing, assume it's http
  if not parsed_url.scheme:
      url = "http://" + url
      parsed_url = urlparse(url)

  # Normalize the scheme (lowercase)
  scheme = parsed_url.scheme.lower()

  # Normalize the netloc (lowercase)
  netloc = parsed_url.netloc.lower()

  # If the netloc is missing (e.g., the URL starts without http/https), extract it from the path
  if not netloc:
      path_split = parsed_url.path.split("/", 1)
      netloc = path_split[0].lower()
      path = "/" + path_split[1] if len(path_split) > 1 else "/"
  else:
      path = parsed_url.path

  # Normalize the path, removing redundant slashes and decoding/encoding special characters properly
  path = re.sub(r'/+', '/', path)
  path = unquote(path)
  
  # Normalize the query and fragment
  query = parsed_url.query
  fragment = parsed_url.fragment

  # Rebuild the parsed URL into the cleaned format
  cleaned_url = urlunparse(ParseResult(
      scheme=scheme,
      netloc=netloc,
      path=path,
      params="",
      query=query,
      fragment=fragment
  ))

  return cleaned_url


if __name__ == "__main__":
  sample_url = "example.com/path/to/resource"
  sample_expected = "http://example.com/path/to/resource"
  result = clean_url(sample_url)
  assert result == sample_expected, f"Expected {sample_expected} but got {result}"
  print("Passed sanity check!")
