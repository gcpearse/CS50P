from watch import parse


def test_https_url():
  assert parse('<iframe width="560" height="315" src="https://www.youtube.com/embed/xvFZjo5PgG0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>') == "https://youtu.be/xvFZjo5PgG0"
  assert parse('<iframe src="https://www.youtube.com/embed/xvFZjo5PgG0"></iframe>') == "https://youtu.be/xvFZjo5PgG0"
  assert parse('<iframe src="https://youtube.com/embed/xvFZjo5PgG0"></iframe>') == "https://youtu.be/xvFZjo5PgG0"


def test_http_url():
  assert parse('<iframe width="560" height="315" src="http://www.youtube.com/embed/xvFZjo5PgG0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>') == "https://youtu.be/xvFZjo5PgG0"
  assert parse('<iframe src="http://www.youtube.com/embed/xvFZjo5PgG0"></iframe>') == "https://youtu.be/xvFZjo5PgG0"
  assert parse('<iframe src="http://youtube.com/embed/xvFZjo5PgG0"></iframe>') == "https://youtu.be/xvFZjo5PgG0"


def test_invalid_url():
  assert parse('<iframe src="https://www.theytube.com/embed/xvFZjo5PgG0"></iframe>') == None


def test_missing_iframe_attribute():
  assert parse('src="https://www.youtube.com/embed/xvFZjo5PgG0"') == None


def test_random_input():
  assert parse("cat") == None
