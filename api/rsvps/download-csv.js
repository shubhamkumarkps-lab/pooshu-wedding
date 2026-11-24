const { handleDownloadCsv } = require('../../lib/handlers');

module.exports = (req, res) => handleDownloadCsv(req, res);
