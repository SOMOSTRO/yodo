import os
import sys

CLR_INPUT = '\033[1m\033[96m'; # bold bright cyan
CLR_ERROR = '\033[1m\033[91m' # bold bright red
CLR_WARNING = '\033[1m\033[93m' # bold bright yellow

# normal colors
CLR_YELLOW = '\033[33m'
CLR_GREEN = '\033[32m'
CLR_CYAN = '\033[36m'
CLR_BLUE = '\033[34m'
CLR_RED = '\033[31m'

# bright colors
CLR_BRIGHT_YELLOW = '\033[93m'
CLR_BRIGHT_GREEN = '\033[92m'
CLR_BRIGHT_CYAN = '\033[96m'
CLR_BRIGHT_BLUE = '\033[94m'

# 256 color palette codes
CLR_LIME = '\033[38;5;154m'
CLR_ORANGE = '\033[38;5;208m'
CLR_CORAL = '\033[38;5;210m'

CLR_DIM = '\033[2m' # dim/faint
CLR_RESET = '\033[0m'

# text styles
CLR_BOLD = '\033[1m'
CLR_ITALIC = '\033[3m'
CLR_STRIKETHROUGH = '\033[9m'

CLR_RESET_BOLD = '\033[22m'
CLR_RESET_ITALIC = '\033[23m'
CLR_RESET_STRIKE = '\033[29m'

# Extras
MOVE_UP_1_LINE = "\x1b[1A" # to go back to previous line


# Windows ANSI support
def _win_ansi_enabled():
  """Try to enable VT processing on Windows. Returns True if successful."""
  try:
    import ctypes
    kernel32 = ctypes.windll.kernel32
    # Enable ENABLE_VIRTUAL_TERMINAL_PROCESSING (0x0004)
    return kernel32.SetConsoleMode(kernel32.GetStdHandle(-11), 7) != 0
  except Exception:
    return False

# Basic ANSI support
_no_ansi = (
  not (
    sys.stdout.isatty() # check whether output is redirected (pipe/file), if yes return false
    or os.environ.get('TERM') != 'dumb' # explicitly dumb terminal
    or (sys.platform == 'win32' and _win_ansi_enabled()) # old Windows console
  )
)
  
# 256-color palette codes support
_no_256 = (
  not (
    os.environ.get('TERM', '') in ('xterm-256color', 'screen-256color', 'tmux-256color')
    or os.environ.get('COLORTERM', '') in ('truecolor', '24bit')
    or 'TERMUX_VERSION' in os.environ
    or (sys.platform == 'win32' and not _no_ansi) # Win Terminal supports 256c
  )
)

# Reset all vars if no ANSI support at all
if _no_ansi:
  # Custom colors
  CLR_INPUT = CLR_ERROR = CLR_WARNING = ''
  
  # Basic/normal colors
  CLR_YELLOW = CLR_GREEN = CLR_CYAN = CLR_BLUE = CLR_RED = ''
  
  # Basic/normal bright colors
  CLR_BRIGHT_YELLOW = CLR_BRIGHT_GREEN = CLR_BRIGHT_CYAN = CLR_BRIGHT_BLUE = ''
  
  # 256 color palette
  CLR_LIME = CLR_ORANGE = CLR_CORAL = ''
  
  # Special text styles
  CLR_DIM = CLR_BOLD = CLR_ITALIC = CLR_STRIKETHROUGH = ''
  
  # Color/style reset codes
  CLR_RESET = CLR_RESET_BOLD = CLR_RESET_ITALIC = CLR_RESET_STRIKE = ''
  
  # Extra special ANSI codes
  MOVE_UP_1_LINE = ''

# Reset all 256-palete codes and special codes
elif _no_256:
  # Custom colors
  CLR_INPUT = CLR_BOLD + CLR_CYAN
  CLR_ERROR = CLR_BOLD + CLR_RED
  CLR_WARNING = CLR_BOLD + CLR_YELLOW
  
  # 256 color palette
  CLR_LIME = CLR_ORANGE = CLR_CORAL = ''