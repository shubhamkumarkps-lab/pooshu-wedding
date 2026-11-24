const { handleDownloadExcel } = require('../../lib/handlers');

module.exports = (req, res) => handleDownloadExcel(req, res);
