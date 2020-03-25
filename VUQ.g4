grammar VUQ;

start: rule_block*;

// [ ]
rule_block: '[' rule_match END_LINE func ']';
// g=1
rule_match: obj=CHAR compare value=param;
// -g>
// -i,g>
func: '-' CHAR (',' CHAR)* '>' func_block ('<' '-')?;
func_block: ((arith | imp | output) SPACE?)*;
// +
// -
// *
// /
arith: first=var arithOp second=param;

// expression: arith | imp | output;

// Python won't let me have input, so it's imp
imp: OR;
output: AND var END_LINE?;

// Any combination of '!', '<' and '='
compare: NOT? LESS? EQUALS? /* (boolOp compare)? */;
// &
// |
// boolOp: AND | OR;

arithOp: arg=(PLUS | MINUS | MULTIPLY | DIVIDE);

var: ','+;
param: INT | CHAR | var | imp;

COMMENT: GRAVE ~[\r\n]* -> skip;
fragment GRAVE: '`';

AND: '&';
OR: '|';
NOT: '!';

EQUALS: '=';
LESS: '<';

PLUS: '+';
MINUS: '-';
MULTIPLY: '*';
DIVIDE: '/';

END_LINE: '\\';

CHAR: [a-z];
INT: [0-9]+;

SPACE: '_';

WS: [ \t\r\n\f]+ -> skip;