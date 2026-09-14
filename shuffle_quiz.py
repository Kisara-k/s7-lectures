"""
Shuffles the answer options of every quiz file (quiz*/*.md) under the current directory.

Each file must have a ## Questions section and a ## Answers section. Questions list
options as plain "A) ..." lines; answers repeat those options prefixed with ✓/✗ and end
each block with a "**Correct:** ..." line. Both sections are reshuffled in sync and the
Correct line is updated to match the new letter assignments.

Order is determined by SEED: same seed always produces the same arrangement. Change SEED
to reshuffle all files to a new deterministic order.
"""
import hashlib
import re
from pathlib import Path


SEED = "franz"

OPTION_LETTER = re.compile(r'^([A-Z])\) (.+)$')


def parse_option_block(lines):
    options = []
    for line in lines:
        m = OPTION_LETTER.match(line)
        if not m:
            return None
        options.append((m.group(1), m.group(2)))
    return options


def _sort_key(text: str) -> str:
    return hashlib.sha256(f"{SEED}\0{text}".encode()).hexdigest()


def shuffle_file(path: Path) -> bool:
    text = path.read_text(encoding='utf-8')

    split_m = re.search(r'^## Answers[ \t]*$', text, re.MULTILINE)
    if not split_m:
        print(f"LINT {path}: missing '## Answers' section")
        return False

    questions_text = text[:split_m.start()]
    answers_text = text[split_m.start():]

    q_block_re = re.compile(
        r'^(#### \d+\..+\n)((?:[A-Z]\) .+\n)+)',
        re.MULTILINE
    )
    a_block_re = re.compile(
        r'^(#### \d+\..+\n)((?:[A-Z]\) .+\n)+)\n(\*\*Correct:\*\*.+)',
        re.MULTILINE
    )

    q_matches = list(q_block_re.finditer(questions_text))
    a_matches = list(a_block_re.finditer(answers_text))

    if not q_matches:
        print(f"LINT {path}: no question option blocks found")
        return False
    if not a_matches:
        print(f"LINT {path}: no answer blocks found")
        return False
    if len(q_matches) != len(a_matches):
        print(f"LINT {path}: {len(q_matches)} question blocks but {len(a_matches)} answer blocks")
        return False

    q_replacements = []
    a_replacements = []

    for i, (qm, am) in enumerate(zip(q_matches, a_matches), 1):
        q_opts = parse_option_block([l.rstrip('\n') for l in qm.group(2).splitlines(keepends=True)])
        a_opts = parse_option_block([l.rstrip('\n') for l in am.group(2).splitlines(keepends=True)])

        if q_opts is None or a_opts is None:
            print(f"LINT {path}: Q{i} option lines don't match expected format")
            return False
        if len(q_opts) != len(a_opts):
            print(f"LINT {path}: Q{i} has {len(q_opts)} question options but {len(a_opts)} answer options")
            return False

        q_letters = [o[0] for o in q_opts]
        a_letters = [o[0] for o in a_opts]
        if q_letters != a_letters:
            print(f"LINT {path}: Q{i} option letters don't match between sections: {q_letters} vs {a_letters}")
            return False

        correct_m = re.search(r'\*\*Correct:\*\*\s*(.+)', am.group(3))
        if not correct_m:
            print(f"LINT {path}: Q{i} can't parse **Correct:** line")
            return False
        correct_letters = set(re.findall(r'[A-Z]', correct_m.group(1)))

        perm = sorted(range(len(q_opts)), key=lambda i: _sort_key(q_opts[i][1].rstrip()))

        new_q_opts = ''
        new_a_opts = ''
        new_correct = []

        for new_pos, old_pos in enumerate(perm):
            new_letter = q_letters[new_pos]
            old_letter = q_letters[old_pos]
            new_q_opts += f"{new_letter}) {q_opts[old_pos][1].rstrip()}  \n"
            new_a_opts += f"{new_letter}) {a_opts[old_pos][1].rstrip()}  \n"
            if old_letter in correct_letters:
                new_correct.append(new_letter)

        new_correct.sort()
        new_correct_str = f"**Correct:** {', '.join(new_correct)}"

        q_replacements.append((qm.start(2), qm.end(2), new_q_opts))
        a_replacements.append((am.start(3), am.end(3), new_correct_str))
        a_replacements.append((am.start(2), am.end(2), new_a_opts))

    new_questions_text = _apply_replacements(questions_text, sorted(q_replacements, key=lambda x: x[0], reverse=True))
    new_answers_text = _apply_replacements(answers_text, sorted(a_replacements, key=lambda x: x[0], reverse=True))

    new_text = new_questions_text + new_answers_text
    if new_text == text:
        return None  # parsed fine, already in hashed order
    path.write_text(new_text, encoding='utf-8')
    return True


def _apply_replacements(text, replacements):
    for start, end, new_text in replacements:
        text = text[:start] + new_text + text[end:]
    return text


def main():
    files = sorted(Path('.').rglob('quiz*/*.md'))
    changed = unchanged = fail = 0
    for f in files:
        result = shuffle_file(f)
        if result is True:
            changed += 1
        elif result is False:
            fail += 1
        else:
            unchanged += 1
    parts = [f"{changed} shuffled", f"{unchanged} unchanged due to seed", f"{fail} skipped due to lint errors"]
    print(", ".join(parts) + ".")


if __name__ == '__main__':
    main()
