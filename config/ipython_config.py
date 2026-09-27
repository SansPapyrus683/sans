from IPython.utils.PyColorize import neutral_theme, theme_table
from copy import deepcopy

nord_darker = deepcopy(neutral_theme)
nord_darker.base = "nord-darker"
theme_table["nord-darker"] = nord_darker

c.TerminalInteractiveShell.colors = "nord-darker"
