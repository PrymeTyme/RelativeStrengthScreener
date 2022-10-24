const sorted_sector_daily = require('../data/sectorSorted/daily/sector_daily.json');
const sorted_sector_weekly = require('../data/sectorSorted/weekly/sector_weekly.json');
const sorted_sector_monthly = require('../data/sectorSorted/monthly/sector_monthly.json');
const sorted_sector_yearly = require('../data/sectorSorted/yearly/sector_yearly.json');
const raw_sectors = require('./sectors_test.json');
const xle_df = require('./xle_df.json');
const xlk_daily = require('./xlk_daily_df.json');
const xlk_df = require('./xlk_df.json');

// Something more

module.exports = () => ({
  sorted_sector_daily: sorted_sector_daily,
  sorted_sector_weekly: sorted_sector_weekly,
  sorted_sector_monthly: sorted_sector_monthly,
  sorted_sector_yearly: sorted_sector_yearly,

  raw_sectors: raw_sectors,
  xle_df: xle_df,
  xlk_daily: xlk_daily,
  xlk_df: xlk_df
  // Something more
});