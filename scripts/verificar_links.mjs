// Confere os links internos dos arquivos Markdown, como o verificar_links.py (engenharia#58).
// Feito para máquinas sem Python, como o Acer. O CI roda os dois.
//
// Uso: node scripts/verificar_links.mjs [pasta]
// Sai com código 1 se algum link relativo apontar para um arquivo que não existe,
// ou se a pasta não existir (o .py, nesse caso, sai com 0).
// Links externos (http, https, mailto) e âncoras puras (#secao) não são conferidos.
// A caixa das letras é conferida também no Windows, como no CI (Linux).
import { existsSync, readdirSync, readFileSync, statSync } from 'node:fs';
import { join, normalize, relative, resolve, sep } from 'node:path';
import { fileURLToPath } from 'node:url';

const LINK = /\[[^\]]*\]\(([^)\s]+)\)/g;
const IGNORAR_PASTAS = new Set(['.git', 'node_modules']);
const EXTERNO = ['http://', 'https://', 'mailto:'];

function* arquivosMd(pasta) {
  // Mesma ordem do os.walk: os arquivos da pasta antes das subpastas.
  const entradas = readdirSync(pasta, { withFileTypes: true });
  for (const e of entradas) if (e.isFile() && e.name.endsWith('.md')) yield join(pasta, e.name);
  for (const e of entradas) if (e.isDirectory() && !IGNORAR_PASTAS.has(e.name)) yield* arquivosMd(join(pasta, e.name));
}

/** Existe com a mesma caixa em cada parte do caminho (o disco do Windows ignora a caixa). */
export function existeComCaixa(caminho) {
  if (!existsSync(caminho)) return false;
  // Caminho absoluto: assim a 1ª parte depois do disco também é conferida (raiz ".").
  const partes = resolve(caminho).split(sep);
  for (let i = 1; i < partes.length; i++) {
    const nome = partes[i];
    if (nome === '' || nome === '.' || nome === '..') continue;
    let pai = partes.slice(0, i).join(sep);
    if (pai === '') pai = sep;
    else if (pai.endsWith(':')) pai += sep;
    if (!readdirSync(pai).includes(nome)) return false;
  }
  return true;
}

/** Devolve a lista de [arquivo, link] cujo destino não existe. */
export function linksQuebrados(raiz) {
  const quebrados = [];
  for (const caminho of arquivosMd(raiz)) {
    // Blocos de código não têm links de verdade.
    const texto = readFileSync(caminho, 'utf8').replace(/```[\s\S]*?```/g, '');
    const pasta = join(caminho, '..');
    for (const [, alvo] of texto.matchAll(LINK)) {
      if (alvo.startsWith('#') || EXTERNO.some((p) => alvo.startsWith(p))) continue;
      const destino = normalize(join(pasta, alvo.split('#', 1)[0]));
      if (!existeComCaixa(destino)) quebrados.push([relative(raiz, caminho).split(sep).join('/'), alvo]);
    }
  }
  return quebrados;
}

if (process.argv[1] === fileURLToPath(import.meta.url)) {
  const raiz = process.argv[2] ?? '.';
  if (!existsSync(raiz) || !statSync(raiz).isDirectory()) {
    console.log(`Pasta não encontrada: ${raiz}`);
    process.exitCode = 1;
  } else {
    const quebrados = linksQuebrados(raiz);
    for (const [arquivo, alvo] of quebrados) console.log(`QUEBRADO ${arquivo}: ${alvo}`);
    console.log(`Links internos quebrados: ${quebrados.length}`);
    process.exitCode = quebrados.length ? 1 : 0;
  }
}
