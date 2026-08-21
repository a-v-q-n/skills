---
description: Valide la marketplace et tous les skills avant un push
---

Valide la marketplace et les skills. Exécute ce bash depuis la racine du repo, puis
résume : si tout est OK, le confirmer ; sinon, lister les problèmes et proposer la
correction de chacun.

```bash
python3 - <<'PY'
import json, sys, os, glob, re

problems = []

def load(p):
    if not os.path.isfile(p):
        problems.append(f"Manquant : {p}"); return None
    try:
        return json.load(open(p, encoding='utf-8'))
    except Exception as e:
        problems.append(f"JSON invalide : {p} — {e}"); return None

mkt = load('.claude-plugin/marketplace.json')

# Chaque plugin du catalogue : plugin.json présent, SANS champ `version` (ni dans l'entrée
# marketplace) — sans version, chaque commit poussé est une version (SHA git) et la mise à
# jour se propage seule côté claude.ai. Une version posée ÉPINGLE le plugin.
entries = (mkt or {}).get('plugins', [])
if mkt and not entries:
    problems.append("marketplace.json : aucun plugin déclaré")
total_skills = 0
for entry in entries:
    pname = entry.get('name') or '?'
    src = (entry.get('source') or '').lstrip('./')
    if entry.get('version'):
        problems.append(
            f"marketplace.json : 'version' ({entry['version']}) épingle {pname} — la retirer")
    plg = load(os.path.join(src, '.claude-plugin/plugin.json'))
    if plg is not None:
        if plg.get('version'):
            problems.append(
                f"{pname}/plugin.json : 'version' ({plg['version']}) épingle le plugin — la retirer")
        if plg.get('name') != pname:
            problems.append(f"{pname}/plugin.json : name = '{plg.get('name')}' ≠ entrée marketplace")
    # Skills : SKILL.md présent, frontmatter avec name (== dossier) et description.
    skill_dirs = sorted(glob.glob(os.path.join(src, 'skills', '*/')))
    if not skill_dirs:
        problems.append(f"{pname} : aucun skill dans {src}/skills/")
    total_skills += len(skill_dirs)
    for d in skill_dirs:
        name = os.path.basename(d.rstrip('/'))
        skill = os.path.join(d, 'SKILL.md')
        if not os.path.isfile(skill):
            problems.append(f"{pname}/{name} : SKILL.md manquant"); continue
        txt = open(skill, encoding='utf-8').read()
        m = re.match(r'^---\s*\n(.*?)\n---', txt, re.S)
        if not m:
            problems.append(f"{pname}/{name} : frontmatter absent (--- … ---)"); continue
        fm = m.group(1)
        nm = re.search(r'^name:\s*(\S+)', fm, re.M)
        if not nm:
            problems.append(f"{pname}/{name} : 'name' absent du frontmatter")
        elif nm.group(1).strip() != name:
            problems.append(f"{pname}/{name} : 'name' = '{nm.group(1).strip()}' ≠ dossier '{name}'")
        if not re.search(r'^description:', fm, re.M):
            problems.append(f"{pname}/{name} : 'description' absente du frontmatter")
    # Agents (optionnels) : frontmatter name + description.
    for a in sorted(glob.glob(os.path.join(src, 'agents', '*.md'))):
        aname = os.path.splitext(os.path.basename(a))[0]
        atxt = open(a, encoding='utf-8').read()
        m = re.match(r'^---\s*\n(.*?)\n---', atxt, re.S)
        if not m or not re.search(r'^name:\s*' + re.escape(aname) + r'\s*$', m.group(1), re.M) \
           or not re.search(r'^description:', m.group(1), re.M):
            problems.append(f"{pname}/agents/{aname} : frontmatter name (== fichier) + description requis")

if problems:
    print("PROBLÈMES :")
    for x in problems:
        print(" -", x)
    sys.exit(1)
print(f"OK — marketplace et skills valides ({len(entries)} plugin(s), {total_skills} skill(s), versionnage par SHA git).")
PY
```
