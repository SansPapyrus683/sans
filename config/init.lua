-- https://stackoverflow.com/a/234578/12128483
vim.cmd('filetype plugin indent on')
-- show existing tab with 4 spaces width
vim.opt.tabstop = 4
-- when indenting with '>', use 4 spaces width
vim.opt.shiftwidth = 4
-- On pressing tab, insert 4 spaces
vim.opt.expandtab = true -- set expandtab& to just indent w/ tabs
-- https://vi.stackexchange.com/a/4250
vim.opt.softtabstop = 4
vim.opt.ignorecase = true
vim.opt.smartcase = true

vim.opt.guicursor="a:ver10"

-- https://superuser.com/a/35421/1503424
vim.opt.whichwrap:append("<,>,h,l,[,]")

-- https://superuser.com/a/181381/1503424
vim.opt.autoread = true -- apparently :e manually reloads asw

vim.opt.list = true
-- https://www.reddit.com/r/vim/comments/4hoa6e
vim.opt.listchars = { lead = '·', tab = '» ', trail = '·', precedes = '←', extends = '→', eol = '↲' }

vim.opt.number = true -- just adds line numbers
vim.opt.cursorline = true -- highlights current line
vim.opt.mouse = 'a' -- actually allows me to use my goddamned mouse
vim.opt.virtualedit = 'onemore'
vim.opt.clipboard = 'unnamedplus'
vim.opt.cc = '80,100'
vim.opt.splitbelow = true
vim.opt.splitright = true
vim.opt.autochdir = true -- https://superuser.com/a/604180

-- https://stackoverflow.com/a/11994072/12128483
vim.api.nvim_set_keymap('n', 'd', '"_d', { noremap = true })
vim.api.nvim_set_keymap('v', 'd', '"_d', { noremap = true })
-- https://superuser.com/a/760272
vim.api.nvim_set_keymap('i', '<C-a>', '<esc>ggVG', { noremap = true })
vim.api.nvim_set_keymap('n', '<C-a>', 'ggVG', { noremap = true })

vim.api.nvim_set_keymap('n', '<C-e>', '<C-w>w', { noremap = true })

-- https://stackoverflow.com/a/55761306/12128483
vim.api.nvim_exec([[
  autocmd TextChanged,TextChangedI <buffer> if &readonly == 0 && filereadable(bufname('%')) | silent write | endif
]], false)

-- https://github.com/junegunn/vim-plug
local Plug = vim.fn['plug#']
vim.call('plug#begin')

Plug('arcticicestudio/nord-vim')
Plug('tmsvg/pear-tree')
Plug('scrooloose/nerdtree')
Plug('vim-airline/vim-airline')
Plug('xiyaowong/transparent.nvim')

vim.call('plug#end')

vim.g.transparent_enabled = true
vim.cmd('colorscheme nord')

vim.api.nvim_set_keymap('n', '<C-s>', ':NERDTreeToggle<CR>', { noremap = true })
-- Start NERDTree and put the cursor back in the other window.
-- vim.cmd('autocmd VimEnter * NERDTree | wincmd p')
-- Close the tab if NERDTree is the only window remaining in it.
vim.cmd('autocmd BufEnter * if winnr(\'$\') == 1 && exists(\'b:NERDTree\') && b:NERDTree.isTabTree() | quit | endif')
-- Open the existing NERDTree on each new tab.
vim.cmd('autocmd BufWinEnter * if getcmdwintype() == \'\' | silent NERDTreeMirror | endif')
-- If another buffer tries to replace NERDTree, put it in the other window, and bring back NERDTree.
vim.cmd([[
  autocmd BufEnter * if bufname('#') =~ 'NERD_tree_\\d\\+' && bufname('%') !~ 'NERD_tree_\\d\\+' && winnr('$') > 1 |
    \ let buf=bufnr() | buffer# | execute "normal! \<C-W>w" | execute 'buffer'.buf | endif
]])

vim.g.NERDTreeShowHidden = 1
