# Prompt the user for the name of a file
# Output the file's media type if it ends with a suffix
# Otherwise, output application/octet-stream
# Ignore leading whitespace
# Treat the input case-insensitively


def main():
  file_name = input("Enter file name: ")
  file_name = file_name.strip().lower()
  result = set_media_type(file_name)
  print(result)


def set_media_type(file_name: str):
  if file_name.endswith(".gif"):
    return "image/gif"
  elif file_name.endswith(".jpg") or file_name.endswith("jpeg"):
    return "image/jpeg"
  elif file_name.endswith(".png"):
    return "image/png"
  elif file_name.endswith(".pdf"):
    return "application/pdf"
  elif file_name.endswith(".txt"):
    return "text/plain"
  elif file_name.endswith(".zip"):
    return "application/zip"
  else:
    return "application/octet-stream"


main()
