
# parsetab.py
# This file is automatically generated. Do not edit.
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftANDORrightNOTLPARENS RPARENS AND OR NOT VARexpr : VARexpr : LPARENS expr RPARENSexpr : NOT exprexpr : expr AND expr\n            | expr OR  expr'
    
_lr_action_items = {'VAR':([0,3,4,5,6,],[2,2,2,2,2,]),'LPARENS':([0,3,4,5,6,],[3,3,3,3,3,]),'NOT':([0,3,4,5,6,],[4,4,4,4,4,]),'$end':([1,2,8,9,10,11,],[0,-1,-3,-4,-5,-2,]),'AND':([1,2,7,8,9,10,11,],[5,-1,5,-3,-4,-5,-2,]),'OR':([1,2,7,8,9,10,11,],[6,-1,6,-3,-4,-5,-2,]),'RPARENS':([2,7,8,9,10,11,],[-1,11,-3,-4,-5,-2,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'expr':([0,3,4,5,6,],[1,7,8,9,10,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> expr","S'",1,None,None,None),
  ('expr -> VAR','expr',1,'p_expr_var','bool_parser.py',26),
  ('expr -> LPARENS expr RPARENS','expr',3,'p_expr_parens','bool_parser.py',31),
  ('expr -> NOT expr','expr',2,'p_expr_not','bool_parser.py',36),
  ('expr -> expr AND expr','expr',3,'p_expr_op','bool_parser.py',41),
  ('expr -> expr OR expr','expr',3,'p_expr_op','bool_parser.py',42),
]
