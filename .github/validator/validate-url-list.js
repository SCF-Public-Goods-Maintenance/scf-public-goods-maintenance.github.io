// One https:// URL per line, optionally followed by "(upstream)".
module.exports = async (field) => {
  // The config is shared by every form; a field this form does not have arrives empty.
  if (!field || typeof field !== 'string') return 'success';
  const lines = field.split('\n').map((line) => line.trim().replace(/^[-*]\s*/, '')).filter(Boolean);
  const urlRegex = /^<?https:\/\/[^\s/$.?#].[^\s>]*>?(\s+\(upstream\))?$/i;
  const bad = lines.filter((line) => !urlRegex.test(line));
  if (lines.length === 0) return 'add at least one repository URL.';
  if (bad.length > 0) return `each line must be one https:// URL, optionally followed by "(upstream)": ${bad.join(', ')}`;
  return 'success';
};
