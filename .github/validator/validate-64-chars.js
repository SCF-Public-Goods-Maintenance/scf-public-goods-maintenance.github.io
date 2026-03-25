module.exports = async (field) => {
  if (!field || typeof field !== 'string') return 'success';
  if (field.length > 64) return `input exceeds 64 characters (current: ${field.length}). Please shorten.`;
  return 'success';
};
