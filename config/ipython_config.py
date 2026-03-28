"""
this is for windows
if it's linux it's just
c.TerminalInteractiveShell.highlighting_style = "nord"
"""

from IPython.utils.PyColorize import neutral_theme, theme_table
from copy import deepcopy

nord = deepcopy(neutral_theme)
nord.base = "nord-darker"
theme_table["nord"] = nord

c.TerminalInteractiveShell.colors = "nord"
