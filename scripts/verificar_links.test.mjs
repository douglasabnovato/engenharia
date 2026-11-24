// Testes do verificar_links.mjs: os 4 casos do test_verificar_links.py e os casos próprios do .mjs (engenharia#58).
// Uso: node --test scripts/
import { test } from 'node:test';
import assert from 'node:assert/strict';
import { mkdirSync, mkdtempSync, writeFileSync } from 'node:fs';
import { tmpdir } from 'node:os';
import { dirname, join } from 'node:path';
import { spawnSync } from 'node:child_process';
import { fileURLToPath } from 'node:url';
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

test('http e mailto são externos e não são conferidos', () => {
  const texto = '[h](http://exemplo.org/x.md) [m](mailto:alguem@exemplo.org)';
  assert.deepEqual(linksQuebrados(montar({ 'a.md': texto })), []);
});

test('caixa diferente é quebrado, também no Windows (como no CI)', () => {
  const raiz = montar({ 'a.md': '[x](README.MD) [y](Pasta/b.md)', 'readme.md': '', 'pasta/b.md': '' });
  assert.deepEqual(linksQuebrados(raiz), [['a.md', 'README.MD'], ['a.md', 'Pasta/b.md']]);
});

const SCRIPT = fileURLToPath(new URL('./verificar_links.mjs', import.meta.url));
const rodar = (...args) => spawnSync(process.execPath, [SCRIPT, ...args], { encoding: 'utf8' });

test('linha de comando: sai com 0 sem quebrados e com 1 com quebrados', () => {
  assert.equal(rodar(montar({ 'a.md': '[b](b.md)', 'b.md': '' })).status, 0);
  const r = rodar(montar({ 'a.md': '[x](falta.md)' }));
  assert.equal(r.status, 1);
  assert.ok(r.stdout.includes('QUEBRADO a.md: falta.md'), r.stdout);
});

test('linha de comando: pasta inexistente sai com 1 e diz o motivo', () => {
  const r = rodar(join(tmpdir(), 'nao-existe-' + process.pid));
  assert.equal(r.status, 1);
  assert.match(r.stdout, /Pasta não encontrada/);
});
