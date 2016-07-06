library("r2ddi")

dir2xml(
  path_in = "temp/v1/en/",
  path_out = "r2ddi/v1/en/",
  missing_codes=-9:-1, 
  my_cores=30)
