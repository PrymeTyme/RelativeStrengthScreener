const sector_daily = require('./sector_daily_df.json');
const sectors = require('./sectors.json');
const xle_df = require('./xle_df.json');
const xlk_daily = require('./xlk_daily_df.json');
const xlk_df = require('./xlk_df.json');

// Something more

module.exports = () => ({
  sector_daily: sector_daily,
  sectors: sectors,
  xle_df: xle_df,
  xlk_daily: xlk_daily,
  xlk_df: xlk_df
  // Something more
});