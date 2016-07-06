clear
set more off

set maxvar 30000

local allfiles : dir "../../data/gip/v1/en" files "*.dta"
foreach file in `allfiles' {
  use ../../data/gip/v1/en/`file', clear
  saveold temp/v1/en/`file', replace
}
