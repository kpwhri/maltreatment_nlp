import pytest

from maltreatment_nlp.patterns import ALL, ABUSIVE_PAT, HITTING_PAT


@pytest.mark.parametrize('text', [
    'Abuse',
    'Allegations of abuse',
    'Allegations of child abuse due to the bruises on thighs',
    'Allegations of sexual abuse',
    'Alleged sexual assault',
    # 'Bruising',
    'Child abuse report',
    'Child neglect',
    'Child reported to a teacher that her mother and stepfather hit her',
    'Child was hit by father',
    'CPS',
    'DCFS report',
    'Disclosed a long history of his parents hitting him with objects',
    'Disclosed sexual abuse',
    'Emotional abuse',
    'Father hit me twice',
    # 'Forced sexual intercourse',
    'He says father would beat him; punch him and hit him with a belt all over his body.',
    'History of sexual abuse',
    # 'Hit',
    'Medical neglect',
    'Molested',
    # 'Patient had bruising',
    'Patient here stating her dad hit her',
    # 'Perpetrator',
    'Physical abuse',
    'Physically abused',
    'Possible abuse',
    'Possible rape',
    'Sexual abuse',
    'Sexual assault',
    'Sexually abused',
    'Sexually assaulted',
    # 'Sometimes he would hit her',
    'Suspected child abuse',
    'Suspected physical abuse',
    'Suspected sexual abuse',
    'Suspicious for child abuse',
    'child maltreatment',
    'child protective services',
    'department of child and family services',
    'possible molestation of this patient',
])
def test_all_patterns_match(text):
    for pattern in ALL:
        if pattern.search(text):
            return True
    assert False, 'All patterns failed to match.'


@pytest.mark.parametrize('text, exp', [
    ('abusive boyfriend', False),
    ('abusive father', True),
])
def test_abusive_pattern(text, exp):
    assert bool(ABUSIVE_PAT.search(text)) == exp


@pytest.mark.parametrize('text, exp', [
    ('mom has hit patient', True),
    ('brother hit her', True),
    ('his father hit him', True),
    ('mother punched her', True),
    ('his brother accidentally hit him', False),
    ('sister hit her', True),
    ('her mother hit her', True),
    ('hit by brother', True),
    ('brother hit him', True),
    ('her dad hit her', True),
    ('her father hit her', True),
    ('her father used to threaten her and hit her', True),
    ('father hitting her', True),
    ('his brother until he hits him', False),
    ('his brother hits him', True),
    ('hit by father', True),
    ('dad beat him', True),
    ('stepfather hit her', True),
    ('hit by mom', True),
    ('hit by her mom', True),
    ('her sister and will hit her', False),
    ('her parents she hit her', False),
    ('mom calling states she hit her', False),
    ('his father will hit him', True),
    ('mother reported she hit her', False),
])
def test_hitting_pattern(text, exp):
    assert bool(HITTING_PAT.search(text)) == exp
