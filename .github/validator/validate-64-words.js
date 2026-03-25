module.exports = async (field) => {
  if (!field || typeof field !== 'string') return 'success';
  const words = field.trim().split(/\s+/).length;
  if (words > 64) return `text exceeds 64 words (current: ${words}). Please shorten.`;
  return 'success';
};
