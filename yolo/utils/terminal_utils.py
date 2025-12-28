from shutil import get_terminal_size
import re

# Getting informations about CLI
# Get terminal size
terminal_size = get_terminal_size()

# Width
terminal_width = terminal_size.columns

def get_terminal_width():
  return terminal_size.columns
  
def print_crossline(char='—'):
  return char * terminal_width
  
def center_title(title, divider="—"):
  """return title in center with a divider"""
  ANSI_ESCAPE_RE = re.compile(r"\x1b\[[0-9;]*m")
  plain_title = ANSI_ESCAPE_RE.sub("", title)
  padded_plain = f" {plain_title} ".center(terminal_width, divider)
  return padded_plain.replace(plain_title, title)
