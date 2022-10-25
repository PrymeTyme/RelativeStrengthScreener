const sorted_sector_daily = require('../data/sectorSorted/daily/sector_daily.json');  // all sorted files are formated python pandas dataframes
const sorted_sector_weekly = require('../data/sectorSorted/weekly/sector_weekly.json');
const sorted_sector_monthly = require('../data/sectorSorted/monthly/sector_monthly.json');
const sorted_sector_yearly = require('../data/sectorSorted/yearly/sector_yearly.json');

const raw_sectors = require('../data/sectors/sectors.json'); // all raw files are ticker datas for charting

const raw_xlb = require('../data/stocks/xlb.json');
const raw_xlc = require('../data/stocks/xlc.json');
const raw_xle = require('../data/stocks/xle.json');
const raw_xlf = require('../data/stocks/xlf.json');
const raw_xli = require('../data/stocks/xli.json');
const raw_xlk = require('../data/stocks/xlk.json');
const raw_xlp = require('../data/stocks/xlp.json');
const raw_xlre = require('../data/stocks/xlre.json');
const raw_xlu = require('../data/stocks/xlu.json');
const raw_xlv = require('../data/stocks/xlv.json');
const raw_xly = require('../data/stocks/xly.json');


const sorted_xlb_daily = require('../data/stockSorted/daily/xlb_daily.json');
const sorted_xlc_daily = require('../data/stockSorted/daily/xlc_daily.json');
const sorted_xle_daily = require('../data/stockSorted/daily/xle_daily.json');
const sorted_xlf_daily = require('../data/stockSorted/daily/xlf_daily.json');
const sorted_xli_daily = require('../data/stockSorted/daily/xli_daily.json');
const sorted_xlk_daily = require('../data/stockSorted/daily/xlk_daily.json');
const sorted_xlp_daily = require('../data/stockSorted/daily/xlp_daily.json');
const sorted_xlre_daily = require('../data/stockSorted/daily/xlre_daily.json');
const sorted_xlu_daily = require('../data/stockSorted/daily/xlu_daily.json');
const sorted_xlv_daily = require('../data/stockSorted/daily/xlv_daily.json');
const sorted_xly_daily = require('../data/stockSorted/daily/xly_daily.json');

const sorted_xlb_weekly = require('../data/stockSorted/weekly/xlb_weekly.json');
const sorted_xlc_weekly = require('../data/stockSorted/weekly/xlc_weekly.json');
const sorted_xle_weekly = require('../data/stockSorted/weekly/xle_weekly.json');
const sorted_xlf_weekly = require('../data/stockSorted/weekly/xlf_weekly.json');
const sorted_xli_weekly = require('../data/stockSorted/weekly/xli_weekly.json');
const sorted_xlk_weekly = require('../data/stockSorted/weekly/xlk_weekly.json');
const sorted_xlp_weekly = require('../data/stockSorted/weekly/xlp_weekly.json');
const sorted_xlre_weekly = require('../data/stockSorted/weekly/xlre_weekly.json');
const sorted_xlu_weekly = require('../data/stockSorted/weekly/xlu_weekly.json');
const sorted_xlv_weekly = require('../data/stockSorted/weekly/xlv_weekly.json');
const sorted_xly_weekly = require('../data/stockSorted/weekly/xly_weekly.json');

const sorted_xlb_monthly = require('../data/stockSorted/monthly/xlb_monthly.json');
const sorted_xlc_monthly = require('../data/stockSorted/monthly/xlc_monthly.json');
const sorted_xle_monthly = require('../data/stockSorted/monthly/xle_monthly.json');
const sorted_xlf_monthly = require('../data/stockSorted/monthly/xlf_monthly.json');
const sorted_xli_monthly = require('../data/stockSorted/monthly/xli_monthly.json');
const sorted_xlk_monthly = require('../data/stockSorted/monthly/xlk_monthly.json');
const sorted_xlp_monthly = require('../data/stockSorted/monthly/xlp_monthly.json');
const sorted_xlre_monthly = require('../data/stockSorted/monthly/xlre_monthly.json');
const sorted_xlu_monthly = require('../data/stockSorted/monthly/xlu_monthly.json');
const sorted_xlv_monthly = require('../data/stockSorted/monthly/xlv_monthly.json');
const sorted_xly_monthly = require('../data/stockSorted/monthly/xly_monthly.json');

const sorted_xlb_yearly = require('../data/stockSorted/yearly/xlb_yearly.json');
const sorted_xlc_yearly = require('../data/stockSorted/yearly/xlc_yearly.json');
const sorted_xle_yearly = require('../data/stockSorted/yearly/xle_yearly.json');
const sorted_xlf_yearly = require('../data/stockSorted/yearly/xlf_yearly.json');
const sorted_xli_yearly = require('../data/stockSorted/yearly/xli_yearly.json');
const sorted_xlk_yearly = require('../data/stockSorted/yearly/xlk_yearly.json');
const sorted_xlp_yearly = require('../data/stockSorted/yearly/xlp_yearly.json');
const sorted_xlre_yearly = require('../data/stockSorted/yearly/xlre_yearly.json');
const sorted_xlu_yearly = require('../data/stockSorted/yearly/xlu_yearly.json');
const sorted_xlv_yearly = require('../data/stockSorted/yearly/xlv_yearly.json');
const sorted_xly_yearly = require('../data/stockSorted/yearly/xly_yearly.json');


//const xle_df = require('./xle_df.json');
//const xlk_daily = require('./xlk_daily_df.json');
//const xlk_df = require('./xlk_df.json');

// Something more

module.exports = () => ({
  sorted_sector_daily: sorted_sector_daily,
  sorted_sector_weekly: sorted_sector_weekly,
  sorted_sector_monthly: sorted_sector_monthly,
  sorted_sector_yearly: sorted_sector_yearly,

  raw_sectors: raw_sectors,

  sorted_xlb_daily: sorted_xlb_daily,
  sorted_xlc_daily: sorted_xlc_daily,
  sorted_xle_daily: sorted_xle_daily,
  sorted_xlf_daily: sorted_xlf_daily,
  sorted_xli_daily: sorted_xli_daily,
  sorted_xlk_daily: sorted_xlk_daily,
  sorted_xlp_daily: sorted_xlp_daily,
  sorted_xlre_daily: sorted_xlre_daily,
  sorted_xlu_daily: sorted_xlu_daily,
  sorted_xlv_daily: sorted_xlv_daily,
  sorted_xly_daily: sorted_xly_daily,

  sorted_xlb_weekly: sorted_xlb_weekly,
  sorted_xlc_weekly: sorted_xlc_weekly,
  sorted_xle_weekly: sorted_xle_weekly,
  sorted_xlf_weekly: sorted_xlf_weekly,
  sorted_xli_weekly: sorted_xli_weekly,
  sorted_xlk_weekly: sorted_xlk_weekly,
  sorted_xlp_weekly: sorted_xlp_weekly,
  sorted_xlre_weekly: sorted_xlre_weekly,
  sorted_xlu_weekly: sorted_xlu_weekly,
  sorted_xlv_weekly: sorted_xlv_weekly,
  sorted_xly_weekly: sorted_xly_weekly,

  sorted_xlb_monthly: sorted_xlb_monthly,
  sorted_xlc_monthly: sorted_xlc_monthly,
  sorted_xle_monthly: sorted_xle_monthly,
  sorted_xlf_monthly: sorted_xlf_monthly,
  sorted_xli_monthly: sorted_xli_monthly,
  sorted_xlk_monthly: sorted_xlk_monthly,
  sorted_xlp_monthly: sorted_xlp_monthly,
  sorted_xlre_monthly: sorted_xlre_monthly,
  sorted_xlu_monthly: sorted_xlu_monthly,
  sorted_xlv_monthly: sorted_xlv_monthly,
  sorted_xly_monthly: sorted_xly_monthly,

  sorted_xlb_yearly: sorted_xlb_yearly,
  sorted_xlc_yearly: sorted_xlc_yearly,
  sorted_xle_yearly: sorted_xle_yearly,
  sorted_xlf_yearly: sorted_xlf_yearly,
  sorted_xli_yearly: sorted_xli_yearly,
  sorted_xlk_yearly: sorted_xlk_yearly,
  sorted_xlp_yearly: sorted_xlp_yearly,
  sorted_xlre_yearly: sorted_xlre_yearly,
  sorted_xlu_yearly: sorted_xlu_yearly,
  sorted_xlv_yearly: sorted_xlv_yearly,
  sorted_xly_yearly: sorted_xly_yearly,




  raw_xlb: raw_xlb,
  raw_xlc: raw_xlc,
  raw_xle: raw_xle,
  raw_xlf: raw_xlf,
  raw_xli: raw_xli,
  raw_xlk: raw_xlk,
  raw_xlp: raw_xlp,
  raw_xlre: raw_xlre,
  raw_xlu: raw_xlu,
  raw_xlv: raw_xlv,
  raw_xly: raw_xly,

  //xle_df: xle_df,
  //xlk_daily: xlk_daily,
  //xlk_df: xlk_df
  // Something more
});