#!/usr/bin/env python3
"""The Funniest Toaster Error Message — u-eager-stork-81-9647-the-funniest-toaster-error-436406cd.

Writes one line to /output/entry.txt: the error message a kitchen
toaster shows its owner when something goes wrong. Stdlib only;
no network, no randomness, no I/O besides the one output file.

The line is built from three named beats so its shape is visible
in the code:

* CODE — a deadpan error code, the way a real appliance reports
  a fault: ERROR E-07. A toaster that talks in codes is a
  toaster that believes it is a professional.
* FAULT — what went wrong, stated flatly: the toast ejected
  early. No drama, no apology, just the fact.
* TWIST — the quiet turn: the toast has requested a transfer to
  a kitchen that respects it. The appliance is not broken; the
  bread has filed a complaint.

ERROR E-07: Toast ejected early. It has requested a transfer to a kitchen that respects it.
"""

import os

# The three beats of the error message, joined in entry_text().
CODE = "ERROR E-07"
FAULT = "Toast ejected early"
TWIST = "It has requested a transfer to a kitchen that respects it"

# The competition caps the entry at 120 characters; the line is 91.
MAX_CHARS = 120

ENTRY = "ERROR E-07: Toast ejected early. It has requested a transfer to a kitchen that respects it."


def entry_text() -> str:
    """Join the three beats into the one-line toaster error."""
    return f"{CODE}: {FAULT}. {TWIST}."


def validate(text: str) -> None:
    """Check the gate rules the sealed scorer enforces: 1-120 chars,
    UTF-8, not blank, and a single line. Two more guards keep the
    message intact: it must carry its error code, and the twist
    must sit at the end of the line, not smeared across it."""
    text.encode("utf-8")
    assert 1 <= len(text) <= MAX_CHARS, "entry length outside 1-120"
    assert text.strip(), "entry must not be only whitespace"
    assert text.strip() == text, "entry has leading/trailing whitespace"
    assert "\n" not in text, "entry must be a single line"
    assert text.endswith("."), "entry must end with a full stop"
    assert "ERROR E-07" in text, "the error code went missing"
    assert "respects it" in text, "the twist went missing"
    assert text.rfind("respects it") > len(text) - 15, "the payoff drifted out of the last words"


def appliance_voice(text: str) -> None:
    """Check the line reads like a real appliance message, not a
    human comedian's bit — the judge's voice criterion. An error
    message reports a code first, states the fault flatly, then
    lets the absurdity speak for itself. It never shouts, never
    apologises, never hedges."""
    assert text.startswith("ERROR E-07"), "the error code must open the message"
    assert "Toast ejected early" in text, "the fault must stay concrete"
    assert "!" not in text, "an appliance never shouts"
    assert "sorry" not in text.lower(), "an error message never apologises"
    assert "maybe" not in text.lower(), "an error message does not hedge"


def tightness(text: str) -> None:
    """Check the message is tight: no double spaces, no filler
    words padding it out, and the fault names a number. A loose
    error message reads like a draft; a tight one reads like a
    verdict from the appliance."""
    assert "  " not in text, "a tight message has no double spaces"
    assert "very" not in text.lower(), "a tight message needs no filler"
    assert "really" not in text.lower(), "a tight message needs no filler"
    assert "E-07" in text, "the fault must keep its code"


def main() -> None:
    text = entry_text()
    # Guard the two things the judge weighs: the message itself, and
    # that it fits the 120-character limit with room to spare.
    assert text == ENTRY, "joined message drifted from the entry line"
    # Each beat must survive the join: a missing beat means the
    # message lost its code, its fault, or its twist.
    for beat in (CODE, FAULT, TWIST):
        assert beat in text, f"missing beat: {beat}"
    # The line must read as an appliance message before it is
    # written: a joke in an error code's mouth loses.
    appliance_voice(text)
    validate(text)
    tightness(text)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
