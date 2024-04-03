from um import count


def test_count():
  assert count("um") == 1
  assert count("um?") == 1
  assert count("Um...") == 1
  assert count("Um, thanks for the album.") == 1
  assert count("Um, thanks, um...") == 2
  assert count("Yum") == 0
  assert count("rumble") == 0
