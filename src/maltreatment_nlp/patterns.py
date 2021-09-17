import re

hit_pat = r'hit|attack|struck|beat|punch'
_family = (
    r'((his|her|their|(pt|patient|client)\W?s?|mom\W?s?|dad\W?s?)\W*)?'
    r'((older|younger|elder|bio|biological|adopted|adoptive)\W*)?'
    r'((step|ex)\W*)*'
    r'('
    r'father|dad|brother|bro|mom|mother|sis|sister|aunt|uncle|relative|parents?'
    r'{}|family|care\W?giver'
    r'|grandfather|grandpa|grandma|grandmother|cousin|nephew|niece'
    r')\b'
)
strict_family = _family.format('')  # no husband/wife/bf/gf in this context
# parent possibly has one of these:
family = _family.format(r'|bf|boy\W?friend|girl\W?friend|gf|husband|wife|partner')
by_family = fr'by\W*(an?\W*)?{family}'
from_family = fr'(by|from)\W*(an?\W*)?{family}'

target = r'\b(him|her|them|me|child|son|daughter|pt|patient|client)\b'

ABUSE_PAT = re.compile(
    r'('
    rf'(emotion|child|physical|sexual|verbal)\w*\W*(abused?|abusive|haras|molest[ei])(\s+\w+){{0,5}}\s+{from_family}'
    rf'|{family}(\s+\w+){{0,2}}\s+(emotion|child|physical|sexual|verbal)\w*\W*(abused?|abusive|haras|molest[ei])'
    r')',
    re.I
)

ABUSIVE_PAT = re.compile(
    r'('
    rf'abusive\s+({strict_family}|childhood|adolescence|growing\W?up)'
    rf'|{strict_family}\s+abusive\s+(emotionally|physically|verbally|sexually)'
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
    rf'(fear(ful)?|scared|afraid|intimated)\s+(by|of)\s+{family}',
    re.I
)

HISTORY_PAT = re.compile(
    rf'('
    rf'\b((history|hx|signs|victim)\s+of|h/o)\w*(\s+\w+){{0,5}}\s+'
    rf'(abus|rap(e|ing)|maltreat|assault|haras|molest|{hit_pat})\w*'  # removed harm: always self-harm
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
    # x hit pt
    rf'{family}(\s+(has|had|will|have|did|would|used to|possibly)){{0,5}}'
    rf'(\s+\w+\s+({target}\s+)?and)?'
    rf'\s+({hit_pat})'
    rf'\w*\s*{target}'
    # hit by
    rf'|\b({hit_pat})\s*{by_family}'
    rf')',
    re.I
)

CPS_PAT = re.compile(
    r'('
    r'child\W*protect\w+\W*service'
    r'|\bcps\b'
    r'|dep(t|artment)(\W+\w+){0,3}\W*(child|family)(\W+\w+){0,3}\W*service'
    r'|dcfs\W*report'
    r')',
    re.I
)

CHILD_MALTREATMENT_PAT = re.compile(
    r'child\W*maltreatment',
    re.I
)

CODE_PAT = re.compile(
    r'('
    r'sexual\s+abuse\s+of\s+child\s+or\s+adolescent'
    r'|sexual\s+abuse\s+of\s+adolescent'
    r'|confirmed\s+victim\s+of\s+sexual\s+abuse\s+in\s+childhood'
    r'|sexual\s+abuse\s+victim'
    r')',
    re.I
)

ALL_PATTERNS = {
    'ABUSE_PAT': ABUSE_PAT,
    'CODE_PAT': CODE_PAT,
    'FEAR_PAT': FEAR_PAT,
    'ABUSIVE_PAT': ABUSIVE_PAT,
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
