-- Presentation-only filter: no change to the Markdown research source.
-- Permit wrapping of literal identifiers/paths and give text-mode mathematical
-- symbols their proper mathematical glyphs rather than missing-font squares.
local symbols = {
  ['−']='-', ['≥']='\\ge', ['≤']='\\le', ['∎']='\\blacksquare',
  ['→']='\\to', ['′']='{}^{\\prime}', ['ℓ']='\\ell',
  ['₂']='{}_{2}', ['₀']='{}_{0}', ['₃']='{}_{3}',
  ['μ']='\\mu', ['ε']='\\varepsilon', ['γ']='\\gamma',
  ['Δ']='\\Delta', ['β']='\\beta', ['≡']='\\equiv',
  ['∈']='\\in', ['≠']='\\ne', ['∤']='\\nmid', ['ℕ']='\\mathbb{N}',
  ['⋯']='\\cdots', ['∪']='\\cup', ['∑']='\\sum',
  ['∀']='\\forall', ['∃']='\\exists', ['∞']='\\infty',
  ['⁵']='{}^{5}', ['¹']='{}^{1}', ['³']='{}^{3}', ['²']='{}^{2}'
}
local function literal(s)
  if s:find('{',1,true) or s:find('}',1,true) then return nil end
  return pandoc.RawInline('latex','\\nolinkurl{'..s..'}')
end
function Code(el)
  if FORMAT:match('latex') and #el.text > 24 and not el.text:find('\n',1,true) then
    return literal(el.text)
  end
end
function Str(el)
  if not FORMAT:match('latex') then return nil end
  if #el.text > 35 and el.text:find('_',1,true) and not el.text:find('\\',1,true) then
    return literal(el.text)
  end
  local parts, pending = {}, ''
  local changed = false
  for _, c in utf8.codes(el.text) do
    local char = utf8.char(c)
    if symbols[char] then
      if #pending > 0 then table.insert(parts,pandoc.Str(pending)); pending='' end
      table.insert(parts,pandoc.Math('InlineMath',symbols[char]))
      changed=true
    else
      pending = pending..char
    end
  end
  if #pending > 0 then table.insert(parts,pandoc.Str(pending)) end
  if changed then return parts end
end
