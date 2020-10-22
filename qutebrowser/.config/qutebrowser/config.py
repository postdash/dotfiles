## Documentation:
##   qute://help/configuring.html
##   qute://help/settings.html

# Load settings configured via the GUI
config.load_autoconfig()

background = '#282a36'
selection = '#44475a'
foreground = '#f8f8f2'
comment = '#6272a4'
cyan = '#8be9fd'
green = '#50fa7b'
orange = '#ffb86c'
pink = '#ff79c6'
purple = '#bd93f9'
red = '#ff5555'
yellow = '#f1fa8c'

c.colors.completion.category.bg = selection
c.colors.completion.category.border.bottom = background
c.colors.completion.category.border.top = c.colors.completion.category.border.bottom
c.colors.completion.category.fg = foreground
c.colors.completion.even.bg = background
c.colors.completion.odd.bg = c.colors.completion.even.bg
c.colors.completion.fg = foreground
c.colors.completion.item.selected.bg = selection
c.colors.completion.item.selected.border.bottom = c.colors.completion.item.selected.bg
c.colors.completion.item.selected.border.top = c.colors.completion.item.selected.border.bottom
c.colors.completion.item.selected.fg = c.colors.completion.fg
c.colors.completion.item.selected.match.fg = orange
c.colors.completion.match.fg = c.colors.completion.item.selected.match.fg
c.colors.completion.scrollbar.bg = background
c.colors.completion.scrollbar.fg = selection
c.colors.contextmenu.menu.bg = background
c.colors.contextmenu.menu.fg = foreground
c.colors.contextmenu.selected.bg = selection
c.colors.contextmenu.selected.fg = c.colors.contextmenu.menu.fg
c.colors.downloads.bar.bg = background
c.colors.downloads.error.bg = c.colors.downloads.bar.bg
c.colors.downloads.error.fg = red
c.colors.downloads.start.bg = c.colors.downloads.bar.bg
c.colors.downloads.start.fg = cyan
c.colors.downloads.stop.bg = c.colors.downloads.bar.bg
c.colors.downloads.stop.fg = green
c.colors.hints.bg = '#CC' + orange[1:]
c.colors.hints.fg = background
c.colors.hints.match.fg = red
c.colors.keyhint.bg = '#CC' + background[1:]
c.colors.keyhint.fg = foreground
c.colors.keyhint.suffix.fg = orange
c.colors.messages.error.bg = red
c.colors.messages.error.border = c.colors.messages.error.bg
c.colors.messages.error.fg = background
c.colors.messages.info.bg = cyan
c.colors.messages.info.border = c.colors.messages.info.bg
c.colors.messages.info.fg = c.colors.messages.error.fg
c.colors.messages.warning.bg = orange
c.colors.messages.warning.border = c.colors.messages.warning.bg
c.colors.messages.warning.fg = c.colors.messages.error.fg
c.colors.prompts.bg = background
c.colors.prompts.border = background
c.colors.prompts.fg = foreground
c.colors.prompts.selected.bg = selection
c.colors.statusbar.normal.bg = background
c.colors.statusbar.normal.fg = foreground
c.colors.statusbar.caret.bg = c.colors.statusbar.normal.bg
c.colors.statusbar.caret.fg = c.colors.statusbar.normal.fg
c.colors.statusbar.caret.selection.bg = c.colors.statusbar.normal.bg
c.colors.statusbar.caret.selection.fg = c.colors.statusbar.normal.fg
c.colors.statusbar.command.bg = c.colors.statusbar.normal.bg
c.colors.statusbar.command.fg = c.colors.statusbar.normal.fg
c.colors.statusbar.command.private.bg = c.colors.statusbar.normal.bg
c.colors.statusbar.command.private.fg = c.colors.statusbar.normal.fg
c.colors.statusbar.insert.bg = c.colors.statusbar.normal.bg
c.colors.statusbar.insert.fg = c.colors.statusbar.normal.fg
c.colors.statusbar.passthrough.bg = c.colors.statusbar.normal.bg
c.colors.statusbar.passthrough.fg = c.colors.statusbar.normal.fg
c.colors.statusbar.private.bg = c.colors.statusbar.normal.bg
c.colors.statusbar.private.fg = c.colors.statusbar.normal.fg
c.colors.statusbar.progress.bg = selection
c.colors.statusbar.url.error.fg = red
c.colors.statusbar.url.fg = foreground
c.colors.statusbar.url.hover.fg = cyan
c.colors.statusbar.url.success.http.fg = yellow
c.colors.statusbar.url.success.https.fg = green
c.colors.statusbar.url.warn.fg = orange
c.colors.tabs.bar.bg = background
c.colors.tabs.even.bg = background
c.colors.tabs.even.fg = comment
c.colors.tabs.odd.bg = c.colors.tabs.even.bg
c.colors.tabs.odd.fg = c.colors.tabs.even.fg
c.colors.tabs.indicator.error = red
c.colors.tabs.indicator.start = cyan
c.colors.tabs.indicator.stop = green
c.colors.tabs.selected.even.bg = selection
c.colors.tabs.selected.even.fg = pink
c.colors.tabs.selected.odd.bg = c.colors.tabs.selected.even.bg
c.colors.tabs.selected.odd.fg = c.colors.tabs.selected.even.fg
c.colors.tabs.pinned.even.bg = c.colors.tabs.even.bg
c.colors.tabs.pinned.even.fg = c.colors.tabs.even.fg
c.colors.tabs.pinned.odd.bg = c.colors.tabs.odd.bg
c.colors.tabs.pinned.odd.fg = c.colors.tabs.odd.fg
c.colors.tabs.pinned.selected.even.bg = c.colors.tabs.selected.even.bg
c.colors.tabs.pinned.selected.even.fg = c.colors.tabs.selected.even.fg
c.colors.tabs.pinned.selected.odd.bg = c.colors.tabs.selected.odd.bg
c.colors.tabs.pinned.selected.odd.fg = c.colors.tabs.selected.odd.fg
c.colors.webpage.bg = 'white'

c.fonts.default_family = ['Iosevka Aile']
c.fonts.default_size = '11pt'
c.fonts.contextmenu = 'default_size default_family'
c.fonts.prompts = 'default_size default_family'
c.fonts.web.family.fixed = 'Liberation Mono'
c.fonts.web.family.sans_serif = 'Liberation Sans'
c.fonts.web.family.serif = 'Liberation Serif'

c.tabs.padding = {'top': 4, 'bottom': 4, 'left': 5, 'right': 5}
