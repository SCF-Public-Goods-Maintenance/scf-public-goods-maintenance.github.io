// At least one SLO row, and every row that was started has all three cells filled.
module.exports = async (field) => {
  // The config is shared by every form; a field this form does not have arrives empty.
  if (!field || typeof field !== 'string') return 'success';
  const rows = field
    .split('\n')
    .map((line) => line.trim())
    .filter((line) => line.startsWith('|'))
    .map((line) => line.replace(/^\||\|$/g, '').split('|').map((cell) => cell.trim()))
    .filter((cells) => !cells.every((cell) => /^:?-*:?$/.test(cell)))
    .filter((cells) => cells.slice(0, 3).join('|').toLowerCase() !== 'obligation|target|evidence source');
  if (rows.length === 0) return 'add at least one SLO row to the table.';
  const incomplete = rows.filter((cells) => cells.length < 3 || cells.slice(0, 3).some((cell) => !cell));
  if (incomplete.length > 0) {
    return `every SLO needs an obligation, a target and an evidence source (${incomplete.length} row(s) incomplete).`;
  }
  return 'success';
};
