import re

hit_pat = r'hit|attack|struck|beat|punch'

ABUSE_PAT = re.compile(
    r'('
    r'(emotion|child|physical|sexual)\w*\W*(abused?|abusive|haras|molest)'
    r')',
    re.I
)

GENERAL_ABUSE_PAT = re.compile(r'\b(abus|molest|assault)\w*', re.I)

PERPETRATOR_PAT = re.compile(r'perpetrator', re.I)

SIGNS_PAT = re.compile(
    r'\b('
    r'bruis\w+'
    r')',
    re.I
)

SUSPICIOUS_ABUSE_PAT = re.compile(
    rf'('
    rf'\b(possib|sometime|alleg|forc|disclos|suspici|history|past|hx)\w*(\W+\w+){{0,5}}\W*'
    rf'(abus|rap(e|ing)|assault|sexual|physical|haras|molest|{hit_pat})\w*'
    rf')',
    re.I
)

NEGLECT_PAT = re.compile(
    r'(medical|child)\W*neglect',
    re.I
)

HITTING_PAT = re.compile(
    rf'('
    rf'\b({hit_pat})\w*(\W+\w+){{0,2}}\W*(him|her|me)\b'
    rf'|\b({hit_pat})\W*(\W+\w+){{0,2}}by\b'
    rf')',
    re.I
)

FORMAL_PAT = re.compile(
    r'('
    r'child\W*protect\w+\W*service'
    r'|\bcps\b'
    r'|dep(t|artment)(\W+\w+){0,3}\W*(child|family)(\W+\w+){0,3}\W*service'
    r'|dcfs\W*report'
    r'|child\W*maltreatment'
    r')',
    re.I
)

ALL_PATTERNS = {
    'ABUSE_PAT': ABUSE_PAT,
    'NEGLECT_PAT': NEGLECT_PAT,
    'HITTING_PAT': HITTING_PAT,
    'FORMAL_PAT': FORMAL_PAT,
    'SUSPICIOUS_ABUSE_PAT': SUSPICIOUS_ABUSE_PAT,
    'SIGNS_PAT': SIGNS_PAT,
    'GENERAL_ABUSE_PAT': GENERAL_ABUSE_PAT,
    'PERPETRATOR_PAT': PERPETRATOR_PAT,
}

ALL = list(ALL_PATTERNS.values())
