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
plg = load('plugins/avqn-skills/.claude-plugin/plugin.json')

# Version : ABSENTE des deux fichiers. Sans champ `version`, chaque commit poussé est une
# version (SHA git) et la mise à jour se propage seule côté claude.ai. Une version posée
# ÉPINGLE le plugin : les clients gardent leur copie tant que la chaîne ne change pas.
if mkt:
    entry = next((p for p in mkt.get('plugins', []) if p.get('name') == 'avqn-skills'), None)
    if not entry:
        problems.append("marketplace.json : entrée 'avqn-skills' introuvable")
    elif entry.get('version'):
        problems.append(
            f"marketplace.json : 'version' ({entry['version']}) épingle le plugin — la retirer "
            "(sans elle, chaque commit se propage seul)")
if plg is not None and plg.get('version'):
    problems.append(
        f"plugin.json : 'version' ({plg['version']}) épingle le plugin — la retirer "
        "(sans elle, chaque commit se propage seul)")

# Skills : SKILL.md présent, frontmatter avec name (== dossier) et description.
skill_dirs = sorted(glob.glob('plugins/avqn-skills/skills/*/'))
if not skill_dirs:
    problems.append("Aucun skill dans plugins/avqn-skills/skills/")
for d in skill_dirs:
    name = os.path.basename(d.rstrip('/'))
    skill = os.path.join(d, 'SKILL.md')
    if not os.path.isfile(skill):
        problems.append(f"{name} : SKILL.md manquant"); continue
    txt = open(skill, encoding='utf-8').read()
    m = re.match(r'^---\s*\n(.*?)\n---', txt, re.S)
    if not m:
        problems.append(f"{name} : frontmatter absent (--- … ---)"); continue
    fm = m.group(1)
    nm = re.search(r'^name:\s*(\S+)', fm, re.M)
    if not nm:
        problems.append(f"{name} : 'name' absent du frontmatter")
    elif nm.group(1).strip() != name:
        problems.append(f"{name} : 'name' = '{nm.group(1).strip()}' ≠ dossier '{name}'")
    if not re.search(r'^description:', fm, re.M):
        problems.append(f"{name} : 'description' absente du frontmatter")

if problems:
    print("PROBLÈMES :")
    for x in problems:
        print(" -", x)
    sys.exit(1)
print(f"OK — marketplace et skills valides ({len(skill_dirs)} skill(s), versionnage par SHA git).")
PY
```
