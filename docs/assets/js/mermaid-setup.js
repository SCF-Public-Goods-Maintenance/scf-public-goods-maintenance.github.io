import mermaid from 'https://cdn.jsdelivr.net/npm/mermaid@11/dist/mermaid.esm.min.mjs';
import elkLayouts from 'https://cdn.jsdelivr.net/npm/@mermaid-js/layout-elk@0/dist/mermaid-layout-elk.esm.min.mjs';

mermaid.registerLayoutLoaders(elkLayouts);
mermaid.initialize({
  startOnLoad: false,
  theme: 'dark',
  layout: 'elk'
});

(async () => {
  const codeBlocks = document.querySelectorAll('pre > code.language-mermaid');
  for (const codeBlock of codeBlocks) {
    const container = codeBlock.parentElement;
    const content = codeBlock.textContent;
    const mermaidDiv = document.createElement('pre');
    mermaidDiv.className = 'mermaid';
    mermaidDiv.textContent = content;
    container.parentNode.replaceChild(mermaidDiv, container);
  }
  await mermaid.run();
})();
