// Testes do verificar_links.mjs: os mesmos 4 casos do test_verificar_links.py (engenharia#58).
// Uso: node --test scripts/
import { test } from 'node:test';
import assert from 'node:assert/strict';
import { mkdirSync, mkdtempSync, writeFileSync } from 'node:fs';
import { tmpdir } from 'node:os';
import { dirname, join } from 'node:path';
import { linksQuebrados } from './verificar_links.mjs';

function montar(arquivos) {
  const raiz = mkdtempSync(join(tmpdir(), 'links-'));
  for (const [nome, texto] of Object.entries(arquivos)) {
    const caminho = join(raiz, nome);
    mkdirSync(dirname(caminho), { recursive: true });
    writeFileSync(caminho, texto, 'utf8');
  }
  return raiz;
}

test('link válido passa', () => {
  const raiz = montar({ 'a.md': '[b](pasta/b.md)', 'pasta/b.md': '[a](../a.md#secao)' });
  assert.deepEqual(linksQuebrados(raiz), []);
});

test('link quebrado aparece', () => {
  const raiz = montar({ 'a.md': '[x](nao-existe.md)' });
  assert.deepEqual(linksQuebrados(raiz), [['a.md', 'nao-existe.md']]);
});

test('externo, âncora e bloco de código são ignorados', () => {
  const texto = '[s](https://exemplo.org) [t](#topo)\n```\n[c](falso.md)\n```\n';
  assert.deepEqual(linksQuebrados(montar({ 'a.md': texto })), []);
});

test('pasta como destino vale', () => {
  const raiz = montar({ 'a.md': '[p](pasta/)', 'pasta/b.md': '' });
  assert.deepEqual(linksQuebrados(raiz), []);
});

test('link quebrado em subpasta sai com caminho em barras normais', () => {
  const raiz = montar({ 'pasta/c.md': '[y](../falta.md)' });
  assert.deepEqual(linksQuebrados(raiz), [['pasta/c.md', '../falta.md']]);
});
