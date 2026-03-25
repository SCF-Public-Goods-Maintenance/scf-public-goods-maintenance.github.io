module.exports = async (field) => {
  if (!field || typeof field !== 'string' || field.length > 64) {
    return 'release-date must be ≤64 characters and contain a year between 2000-2099 (e.g. "March 2024" or "Launched early 2025").';
  }
  const yearMatch = field.match(/\b(20[0-9][0-9])\b/);
  if (!yearMatch || parseInt(yearMatch[1]) < 2000 || parseInt(yearMatch[1]) > 2099) {
    return 'field must contain a year between 2000-2099 anywhere in the text.';
  }
  return 'success';
};
