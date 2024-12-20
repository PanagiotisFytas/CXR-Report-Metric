import config
from CXRMetric.run_eval import calc_metric
from CXRMetric.run_eval import CompositeMetric

gt_reports_files = config.GT_REPORTS_FILES
predicted_reports_files = config.PREDICTED_REPORTS_FILES
out_file_files = config.OUT_FILE_FILES
use_idf = config.USE_IDF

if __name__ == "__main__":
    for gt_reports, predicted_reports, out_file in zip(gt_reports_files, predicted_reports_files, out_file_files):
        calc_metric(gt_reports, predicted_reports, out_file, use_idf)
