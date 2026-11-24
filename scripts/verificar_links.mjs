// Confere os links internos dos arquivos Markdown, como o verificar_links.py (engenharia#58).
// Feito para máquinas sem Python, como o Acer. O CI continua com o .py.
//
// Uso: node scripts/verificar_links.mjs [pasta]
// Sai com código 1 se algum link relativo apontar para um arquivo que não existe.
// Links externos (http, https, mailto) e âncoras puras (#secao) não são conferidos.
import { existsSync, readdirSync, readFileSync } from 'node:fs';
import { join, normalize, relative, sep } from 'node:path';
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
      if (!existsSync(destino)) quebrados.push([relative(raiz, caminho).split(sep).join('/'), alvo]);
    }
  }
  return quebrados;
}

if (process.argv[1] === fileURLToPath(import.meta.url)) {
  const quebrados = linksQuebrados(process.argv[2] ?? '.');
  for (const [arquivo, alvo] of quebrados) console.log(`QUEBRADO ${arquivo}: ${alvo}`);
  console.log(`Links internos quebrados: ${quebrados.length}`);
  process.exitCode = quebrados.length ? 1 : 0;
}
