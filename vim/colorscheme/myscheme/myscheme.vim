" Vim color scheme
" Name:         blackboard.vim
" Maintainer:   ratazzi.potts <ratazzi.potts@gmail.com> 
" Link:         http://www.ratazzi.org

:set background=dark
highlight clear
if version > 580
    hi clear
    if exists("syntax_on")
        syntax reset
    endif
endif
let g:colors_name = 'myscheme'

if has('gui_running')
    "hi Normal guifg=#eeeeee guibg=#090B18
    hi Normal guifg=#eeeeee guibg=#0e0606
    hi Cursor guifg=Black guibg=Yellow

    hi LineNr guifg=#333333 ctermfg=236
    "hi LineNr guibg=#323232 guifg=#888888
    hi VertSplit guibg=#c2bfa5 guifg=grey40 gui=none ctermfg=241
    hi Folded guibg=black guifg=grey40 ctermfg=241
    hi FoldColumn guibg=black guifg=grey20 ctermfg=236
    hi IncSearch guibg=black guifg=yellow 
    hi ModeMsg guifg=goldenrod
    hi MoreMsg guifg=SeaGreen
""    hi NonText guifg=RoyalBlue guibg=#151825 ctermfg=234
    hi Question guifg=springgreen
    hi Search guibg=#0099ff guifg=White
    hi Visual gui=none guifg=khaki guibg=olivedrab

    hi SpecialKey guifg=#cbfe29 ctermfg=190
    hi Title guifg=#ff9900 gui=bold ctermfg=208 cterm=bold
    hi Statement guifg=#4e8e50 ctermfg=202
    hi htmlStatement guifg=#61c3fe ctermfg=39
    hi String guifg=#99ec5c ctermfg=155
    hi Comment guifg=grey52 ctermfg=240
    hi CommentDoc guifg=grey60 ctermfg=244
    hi Conditional guifg=#ffee14 ctermfg=226
    hi Constant guifg=#cbfe29 ctermfg=190
    hi Special guifg=#86A7D0 ctermfg=110
    hi Identifier guifg=#ff9900 gui=bold ctermfg=208 cterm=bold
    hi Include guifg=#8fde00 ctermfg=220
    hi PreProc guifg=grey ctermfg=grey
    hi Operator gui=bold guifg=#ff9900 ctermfg=208 cterm=bold
    "hi Define guifg=#ffde00 gui=bold ctermfg=220 cterm=bold
    "hi Define guifg=#ffde00  ctermfg=220 
    ""  From ir_black
    hi PreProc guifg=#7180e5 guibg=NONE guisp=NONE gui=NONE ctermfg=68 ctermbg=NONE cterm=NONE
    hi Macro guifg=#7180e5 guibg=NONE guisp=NONE gui=NONE ctermfg=68 ctermbg=NONE cterm=NONE

    hi DefinedName  guifg=#7180e5 guibg=NONE guisp=NONE gui=NONE ctermfg=68 ctermbg=NONE cterm=NONE

    hi Function guifg=#c8a000 guibg=NONE guisp=NONE gui=bold ctermfg=180 ctermbg=NONE cterm=NONE
    hi Tag guifg=#e6c280 guibg=NONE guisp=NONE gui=NONE ctermfg=173 ctermbg=NONE cterm=NONE

""    hi Typedef guifg=#fff000 guibg=NONE guisp=NONE gui=NONE ctermfg=186 ctermbg=NONE cterm=NONE


    hi Type guifg=#61c3fe ctermfg=39
    "hi Function guifg=#ffde00 gui=NONE ctermfg=220
    "hi Structure gui=bold guifg=#fe6600 ctermfg=202 cterm=bold

    hi Ignore guifg=grey40 ctermfg=241
    hi StatusLineNC guibg=#c2bfa5 guifg=grey40 gui=none ctermfg=241
    hi StatusLine guibg=#c2bfa5 guifg=black gui=bold
    hi Todo guifg=orangered guibg=yellow2
    hi WarningMsg guifg=#990000 ctermfg=88
    hi ErrorMsg guifg=#990000 guibg=#ffeaea ctermfg=88 ctermbg=224
    hi Error guifg=#990000 guibg=#ffeaea ctermfg=88 ctermbg=224
    hi SpellErrors guifg=White guibg=Red
else
    hi Normal guifg=#eeeeee guibg=#090B18
    "hi Normal guifg=#eeeeee guibg=#000000
    hi Cursor guifg=Black guibg=Yellow

    hi LineNr guifg=#333333 ctermfg=236
    "hi LineNr guibg=#323232 guifg=#888888
    hi VertSplit guibg=#c2bfa5 guifg=grey40 gui=none ctermfg=241
    hi Folded guibg=black guifg=grey40 ctermfg=241
    hi FoldColumn guibg=black guifg=grey20 ctermfg=236
    hi IncSearch guibg=black guifg=yellow 
    hi ModeMsg guifg=goldenrod
    hi MoreMsg guifg=SeaGreen
    hi NonText guifg=RoyalBlue guibg=#151825 ctermfg=234
    hi Question guifg=springgreen
    hi Search guibg=#0099ff guifg=White
    hi Visual gui=none guifg=khaki guibg=olivedrab

    hi SpecialKey guifg=#cbfe29 ctermfg=190
    hi Title guifg=#ff9900 gui=bold ctermfg=208 cterm=bold
    hi Statement guifg=#ff6600 ctermfg=202
    hi htmlStatement guifg=#61c3fe ctermfg=39
    hi String guifg=#99ec5c ctermfg=155
    hi Comment guifg=grey35 ctermfg=240
    hi CommentDoc guifg=grey50 ctermfg=244
    hi Conditional guifg=#ffee14 ctermfg=226
    hi Constant guifg=#cbfe29 ctermfg=190
    hi Special guifg=#86A7D0 ctermfg=110
    hi Identifier guifg=#ff9900 gui=bold ctermfg=208 cterm=bold
    hi Include guifg=#ffde00 ctermfg=220
    hi PreProc guifg=grey ctermfg=grey
    hi Operator gui=bold guifg=#ff9900 ctermfg=208 cterm=bold
    hi Define guifg=#ffde00 gui=bold ctermfg=220 cterm=bold
    hi Type guifg=#61c3fe ctermfg=39
    hi Function guifg=#ffde00 gui=NONE ctermfg=220
    hi Structure gui=bold guifg=#ff6600 ctermfg=202 cterm=bold

    hi Ignore guifg=grey40 ctermfg=241
    hi StatusLineNC guibg=#c2bfa5 guifg=grey40 gui=none ctermfg=241
    hi StatusLine guibg=#c2bfa5 guifg=black gui=bold
    hi Todo guifg=orangered guibg=yellow2
    hi WarningMsg guifg=#990000 ctermfg=88
    hi ErrorMsg guifg=#990000 guibg=#ffeaea ctermfg=88 ctermbg=224
    hi Error guifg=#990000 guibg=#ffeaea ctermfg=88 ctermbg=224
    hi SpellErrors guifg=White guibg=Red
endif
