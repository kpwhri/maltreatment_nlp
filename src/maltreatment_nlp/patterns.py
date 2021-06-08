import re

hit_pat = r'hit|attack|struck|beat|punch'
family = (
    r'((his|her|their|(pt|patient|client)\W?s?|mom\W?s?|dad\W?s?)\W*)?'
    r'((older|younger|elder|bio|biological|adopted|adoptive)\W*)?'
    r'((step|ex)\W*)?'
    r'\b('
    r'father|dad|brother|bro|mom|mother|sis|sister|aunt|uncle|relative|parents?'
    r'|bf|boy\W?friend|girl\W?friend|gf|husband|wife|partner|family|care\W?giver'
    r'|grandfather|grandpa|grandma|grandmother|cousin|nephew|niece'
    r')\b'
)
by_family = fr'by\W*{family}'
from_family = fr'(by|from)\W*{family}'

ABUSE_PAT = re.compile(
    r'('
    rf'(emotion|child|physical|sexual)\w*\W*(abused?|abusive|haras|molest[ei])(\s+\w+){{0,5}}\s+{from_family}'
    rf'|{family}(\s+\w+){{0,2}}\s+(emotion|child|physical|sexual)\w*\W*(abused?|abusive|haras|molest[ei])'
    r')',
    re.I
)

GENERAL_ABUSE_PAT = re.compile(
    rf'\b(abus[ei]|molest[ei]|assault)\w*',
    re.I
)

PERPETRATOR_PAT = re.compile(
    rf'perpetrators?(\s+\w+){{0,5}}\s+{family}',
    re.I
)

SIGNS_PAT = re.compile(
    r'('
    r'document( (his|her))? bruis\w+'
    rf'|bruis\w+(\s+\w+){{0,5}}\s+caused\s+{from_family}'
    rf'|bruis\w+\s+{from_family}'
    rf'|bruis\w+(\s+\w+){{0,5}}\s+(home|back|return\w*|on( (his|her|their))? return)(\s+\w+){{0,5}}\s+{from_family}'
    rf'|(home|back|return\w*|on( (his|her|their))? return)(\s+\w+){{0,5}}\s+bruis\w+(\s+\w+){{0,5}}\s+{from_family}'
    r')',
    re.I
)

FEAR_PAT = re.compile(  # not currently used
    rf'(fear|scared|afraid) of {family}',
    re.I
)

HISTORY_PAT = re.compile(
    rf'('
    rf'\b((history|hx|signs)\s+of|h/o)\w*(\s+\w+){{0,5}}\s*'
    rf'(abus|rap(e|ing)|maltreat|assault|harm|haras|molest|{hit_pat})\w*'
    rf')',
    re.I
)

SUSPICIOUS_ABUSE_PAT = re.compile(
    rf'('
    rf'\b(possib|sometime|alleg|forc|disclos|suspici|past)\w*(\s+\w+){{0,5}}\s+'
    rf'(abus|maltreat|rap(e|ing)|assault|haras|molest)\w*'  # removed hit: too many FPs
    rf')',
    re.I
)

NEGLECT_PAT = re.compile(
    r'(medical|child)\W*neglect',
    re.I
)

HITTING_PAT = re.compile(
    rf'('
    rf'{family}(\s+\w+){{0,5}}\s+({hit_pat})\w*(\s+\w+){{0,2}}\s*\b(him|her|me|child|son|daughter|pt|patient|client)\b'
    rf'|\b({hit_pat})\s*(\s+\w+){{0,2}}{by_family}'
    rf')',
    re.I
)

CPS_PAT = re.compile(
    r'('
    r'child\W*protect\w+\W*service'
    r'|\bcps\b'
    r'|dep(t|artment)(\W+\w+){0,3}\W*(child|family)(\W+\w+){0,3}\W*service'
    r'|dcfs\W*report'
    r'|child\W*maltreatment'
    r')',
    re.I
)

CHILD_MALTREATMENT_PAT = re.compile(
    r'child\W*maltreatment'
)

ALL_PATTERNS = {
    'ABUSE_PAT': ABUSE_PAT,
    'NEGLECT_PAT': NEGLECT_PAT,
    'HITTING_PAT': HITTING_PAT,
    'CPS_PAT': CPS_PAT,
    'SUSPICIOUS_ABUSE_PAT': SUSPICIOUS_ABUSE_PAT,
    'SIGNS_PAT': SIGNS_PAT,
    'GENERAL_ABUSE_PAT': GENERAL_ABUSE_PAT,
    'PERPETRATOR_PAT': PERPETRATOR_PAT,
    'HISTORY_PAT': HISTORY_PAT,
    'CHILD_MALTREATMENT_PAT': CHILD_MALTREATMENT_PAT,
}

ALL = list(ALL_PATTERNS.values())
