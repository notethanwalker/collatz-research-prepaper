"""Read-only validation of Pandoc math parsing and TeX brace balance."""
from pathlib import Path
import json, re, subprocess
base = Path(__file__).resolve().parents[1]
report = {'chapters': [], 'raw_inline_tex': [], 'unbalanced_math': []}
for path in sorted((base / 'chapters').glob('*.md')):
    ast = json.loads(subprocess.check_output([
        'pandoc', str(path), '-f', 'markdown+tex_math_single_backslash+tex_math_dollars+raw_tex', '-t', 'json'
    ]))
    counts = {'chapter': path.name, 'inline_math': 0, 'display_math': 0, 'raw_inline_tex': 0}
    def visit(node):
        if isinstance(node, dict):
            if node.get('t') == 'Math':
                kind, formula = node['c']
                counts['inline_math' if kind['t'] == 'InlineMath' else 'display_math'] += 1
                depth, bad = 0, False
                for match in re.finditer('[{}]', formula):
                    k = match.start() - 1
                    while k >= 0 and formula[k] == '\\': k -= 1
                    if (match.start() - 1 - k) % 2: continue
                    depth += 1 if match[0] == '{' else -1
                    bad = bad or depth < 0
                if depth or bad:
                    report['unbalanced_math'].append({'chapter': path.name, 'formula': formula, 'balance': depth})
            elif node.get('t') == 'RawInline' and node['c'][0] in {'tex', 'latex'}:
                counts['raw_inline_tex'] += 1
                report['raw_inline_tex'].append({'chapter': path.name, 'text': node['c'][1]})
            for value in node.values(): visit(value)
        elif isinstance(node, list):
            for value in node: visit(value)
    visit(ast)
    report['chapters'].append(counts)
report['passed'] = not report['raw_inline_tex'] and not report['unbalanced_math']
(base / 'build/math-validation.json').write_text(json.dumps(report, indent=2) + '\n')
print(json.dumps(report, indent=2))
raise SystemExit(0 if report['passed'] else 1)
