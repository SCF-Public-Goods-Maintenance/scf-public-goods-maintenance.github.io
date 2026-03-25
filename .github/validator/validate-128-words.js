module.exports = async (field) => {
  if (!field || typeof field !== 'string') return 'success';
  const words = field.trim().split(/\s+/).length;
  if (words > 128) return `text exceeds 128 words (current: ${words}). Please shorten.`;
  return 'success';
};
