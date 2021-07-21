
# Overview

A series of regular expressions to aid in identification of childhood maltreatment in clinical notes.

# Prerequisites

* Python 3.8+

# Algorithm

Incorporating these into an algorithm should involve the following steps:

* Collect relevant text for relevant individuals
* Run the patterns (`run.run` is entrypoint)
* Apply post-processing filters to clean up troublesome patterns (e.g., handle negation, etc.)

See example in Jupyter notebook: `nbs/run_algorithm.ipynb`

# Pattern Descriptions

| Pattern | Description | Notes |
| --- | --- | --- |
| ABUSE_PAT | General description of abuse/harassment | Good |
| ABUSIVE_PAT | Abusive family member | May not describe abuse of target individual |
| GENERAL_ABUSE_PAT | Generic abuse for exploration | Do not use in algorithm: Too many FPs |
| PERPETRATOR_PAT | Language sometimes used to describe actor of abuse | Needs Review (rare) |
| SIGNS_PAT | Discussion of identifying/noticing bruises, etc. after a visit | Needs Review (rare) |
| FEAR_PAT | Discussion of being afraid or intimidated of family, etc. | Likely requires additional evidence |
| HISTORY_PAT | Discussion of history of abuse | Very good, but historical (often distantly) |
| SUSPICIOUS_ABUSE_PAT | Abuse described with some ambiguous terms | Mostly good, a few negated |
| NEGLECT_PAT | Description of child/medical neglect | Excellent |
| HITTING_PAT | Description of being hit/attacked by family member | 'hit' terms are ambiguous; sometimes other referent |
| CPS_PAT | Description of CPS involvement | Good |
| CHILD_MALTREATMENT_PAT | Description of child maltreatment | Needs review |
| CODE_PAT | Looking for dumping of diagnostic/related codes in text | Good |


# License

Licensed under MIT: https://kpwhri.mit-license.org/
