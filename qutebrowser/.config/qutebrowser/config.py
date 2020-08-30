## Documentation:
##   qute://help/configuring.html
##   qute://help/settings.html

# Load settings configured via the GUI
config.load_autoconfig()

bg0 = '#282828'
bg1 = '#3c3836'
bg2 = '#504945'
bg3 = '#665c54'
bg4 = '#7c6f64'
fg0 = '#fbf1c7'
fg1 = '#ebdbb2'
fg2 = '#d5c4a1'
fg3 = '#bdae93'
fg4 = '#a89984'
red = '#cc241d'
brred = '#fb4934'
green = '#98971a'
brgreen = '#b8bb26'
yellow = '#d79921'
bryellow = '#fabd2f'
blue = '#458588'
brblue = '#83a598'
purple = '#b16286'
brpurple = '#d3869b'
aqua = '#689d6a'
braqua = '#8ec07c'
orange = '#d65d0e'
brorange = '#fe8019'

c.colors.completion.category.bg = bg3
c.colors.completion.category.border.bottom = bg0
c.colors.completion.category.border.top = c.colors.completion.category.border.bottom
c.colors.completion.category.fg = fg1
c.colors.completion.even.bg = bg1
c.colors.completion.odd.bg = bg2
c.colors.completion.fg = fg1
c.colors.completion.item.selected.bg = blue
c.colors.completion.item.selected.border.bottom = c.colors.completion.item.selected.bg
c.colors.completion.item.selected.border.top = c.colors.completion.item.selected.border.bottom
c.colors.completion.item.selected.fg = c.colors.completion.fg
c.colors.completion.item.selected.match.fg = bryellow
c.colors.completion.match.fg = c.colors.completion.item.selected.match.fg
c.colors.completion.scrollbar.bg = bg0
c.colors.completion.scrollbar.fg = fg4
c.colors.contextmenu.menu.bg = bg0
c.colors.contextmenu.menu.fg = fg1
c.colors.contextmenu.selected.bg = bg3
c.colors.contextmenu.selected.fg = fg1
c.colors.downloads.bar.bg = bg0
c.colors.downloads.error.bg = c.colors.downloads.bar.bg
c.colors.downloads.error.fg = brred
c.colors.downloads.start.bg = c.colors.downloads.bar.bg
c.colors.downloads.start.fg = brblue
c.colors.downloads.stop.bg = c.colors.downloads.bar.bg
c.colors.downloads.stop.fg = brgreen
c.colors.hints.bg = '#CC' + yellow[1:]
c.colors.hints.fg = bg0
c.colors.hints.match.fg = red
c.colors.keyhint.bg = '#CC' + bg0[1:]
c.colors.keyhint.fg = fg1
c.colors.keyhint.suffix.fg = bryellow
c.colors.messages.error.bg = red
c.colors.messages.error.border = c.colors.messages.error.bg
c.colors.messages.error.fg = fg1
c.colors.messages.info.bg = blue
c.colors.messages.info.border = c.colors.messages.info.bg
c.colors.messages.info.fg = c.colors.messages.error.fg
c.colors.messages.warning.bg = orange
c.colors.messages.warning.border = c.colors.messages.warning.bg
c.colors.messages.warning.fg = c.colors.messages.error.fg
c.colors.prompts.bg = bg0
c.colors.prompts.border = bg2
c.colors.prompts.fg = fg1
c.colors.prompts.selected.bg = blue
c.colors.statusbar.normal.bg = bg0
c.colors.statusbar.normal.fg = fg1
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
c.colors.statusbar.private.bg = bg2
c.colors.statusbar.private.fg = c.colors.statusbar.normal.fg
c.colors.statusbar.progress.bg = bg4
c.colors.statusbar.url.error.fg = brred
c.colors.statusbar.url.fg = fg1
c.colors.statusbar.url.hover.fg = brblue
c.colors.statusbar.url.success.http.fg = bryellow
c.colors.statusbar.url.success.https.fg = brgreen
c.colors.statusbar.url.warn.fg = brorange
c.colors.tabs.bar.bg = bg0
c.colors.tabs.even.bg = bg1
c.colors.tabs.even.fg = bg4
c.colors.tabs.odd.bg = c.colors.tabs.even.bg
c.colors.tabs.odd.fg = c.colors.tabs.even.fg
c.colors.tabs.indicator.error = red
c.colors.tabs.indicator.start = blue
c.colors.tabs.indicator.stop = green
c.colors.tabs.selected.even.bg = c.colors.tabs.even.bg
c.colors.tabs.selected.even.fg = brgreen
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
