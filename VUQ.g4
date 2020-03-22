grammar VUQ;

start: rule_block*;

// [ ]
rule_block: '[' rule_match '\\' func ']';
// g=1
rule_match: CHAR EQUALS param;
// -g>
// -i,g>
func: '-' CHAR (',' CHAR)* '>' (arith SPACE?)* ('<' '-')?;
// +
// -
// *
// /
arith: first=var op second=param;
param: INT | CHAR | var;

op: arg=(PLUS | MINUS | MULTIPLY | DIVIDE);

var: ','+;

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

WS: [\t\r\n\f]+ -> skip;