grammar VUQ;

start: rule_block*;

// [ ]
rule_block: '[' rule_match '\\' func ']';
// g=1
rule_match: obj=CHAR compare value=param;
// -g>
// -i,g>
func: '-' CHAR (',' CHAR)* '>' (arith SPACE?)* ('<' '-')?;
// +
// -
// *
// /
arith: first=var arithOp second=param;
compare: NOT? LESS? EQUALS (boolOp compare)?;
boolOp: AND | OR;

arithOp: arg=(PLUS | MINUS | MULTIPLY | DIVIDE);

var: ','+;
param: INT | CHAR | var;

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

CHAR: [a-z];
INT: [0-9]+;

SPACE: '_';

WS: [ \t\r\n\f]+ -> skip;