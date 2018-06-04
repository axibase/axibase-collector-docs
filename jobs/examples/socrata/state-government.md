# Overview

This list contains references to datasets released by State Governments on [data.gov](http://catalog.data.gov/dataset?q=&sort=views_recent+desc&organization_type=State+Government&res_format=JSON) in [Socrata](https://github.com/socrata) format (JSON).

## Dataset Types

* [Series](#series)
* [Messages](#messages)

___

## Series

* Datasets

| **State** | **Name** | **Attribution** |
|:---|:---|:---|
| Illinois | [Abortion Demographics, 1995-2012](#abortion-demographics-1995-2012) | Illinois Department of Public Health, Office of Finance and Administration, Division of Vital Records |
| Maryland | [Anne Arundel County Crime Rate By Type](#anne-arundel-county-crime-rate-by-type) | MSAC |
| New York | [Automobiles Annual Imports and Exports Through Port Authority of NY NJ Maritime Terminals: Beginning 2000](#automobiles-annual-imports-and-exports-through-port-authority-of-ny-nj-maritime-terminals-beginning-2000) | The Port Authority of New York & New Jersey |
| Maryland | [Employment Figures](#employment-figures) | Bureau of Labor Statistics |
| New York | [Solar Photovoltaic (PV) Incentive Program Completed Projects by City and Contractor: Beginning 2010](#solar-photovoltaic-pv-incentive-program-completed-projects-by-city-and-contractor-beginning-2010) | New York State Energy Research and Development Authority |
| Hawaii | [Table 17: Solid Waste Recycled (in tons)](#table-17-solid-waste-recycled-in-tons) | Iowa Department of Education, Adequate Yearly Progress |
| Iowa | [Math And Reading Proficiency by School Year, Public School District, and Grade Level](#math-and-reading-proficiency-by-school-year-public-school-district-and-grade-level) | Iowa Department of Education, Adequate Yearly Progress |
| Hawaii | [AAA Fuel Prices](#aaa-fuel-prices) | Department of Economic Development and Tourism |
| Connecticut | [Sales and Use Tax per Town by NAICS (2013 and 2014)](#sales-and-use-tax-per-town-by-naics-2013-and-2014) | Department of Revenue Services |
| Maryland | [Per Capita Electricity Consumption](#per-capita-electricity-consumption) | MEA |
| Maryland | [MVA Vehicle Sales Counts by Month for CY 2002-2015](#mva-vehicle-sales-counts-by-month-for-cy-2002---2015) | Motor Vehicle Administration |
| Connecticut | [DAS HR Almanac - Executive Branch Employment By Race](#das-hr-almanac---executive-branch-employment-by-race) | DAS Human Resources |
| New York | [Scholarship Recipients and Dollars by Sector Group: Beginning 2009](#scholarship-recipients-and-dollars-by-sector-group-beginning-2009) | New York State Higher Education Services Corporation |
| New York | [Public Assistance and SNAP Fraud Prevention Performance Measures: Beginning 2013](#public-assistance-and-snap-fraud-prevention-performance-measures-beginning-2013) | New York State Office of Temporary and Disability Assistance (OTDA) |
| Maryland | [Maryland Veterans Unemployment Rate](#maryland-veterans-unemployment-rate) | Bureau of Labor Statistics
| Maryland | [Trips Taken on Public Transit by Transit Type - Monthly Total Trips](#trips-taken-on-public-transit-by-transit-type---monthly-total-trips) | Maryland Transit Authority |
| Iowa | [Employee Compensation by Industry in Iowa](#employee-compensation-by-industry-in-iowa) | U.S. Department of Commerce, Bureau of Economic Analysis, Compensation of Employees by Industry (SQ6, SQ6N) |

### Abortion Demographics, 1995-2012

| **Name** | **Value** |
|:---|:---|
| Id | f7nd-jj28 |
| Name | Abortion Demographics, 1995-2012 |
| State | [Illinois](https://data.illinois.gov) |
| Description | The number of induced pregnancy terminations reported in Illinois by county (if in excess of 50), by age and marital status.<br>Note: Marital status and age are only for Illinois residents. |
| Attribution | Illinois Department of Public Health, Office of Finance and Administration, Division of Vital Records |
| Category | Health |
| Date Range | 1995-2012 |
| Links | catalog: `http://catalog.data.gov/dataset/abortion-demographics-1995-2012-8f496`,  metadata: `https://data.illinois.gov/api/views/f7nd-jj28`,  data: `https://data.illinois.gov/api/views/f7nd-jj28/rows.json?accessType=DOWNLOAD`,  portal: `https://apps.axibase.com/chartlab/55eb27ce` |

* Command

```ls
series e:f7nd-jj28 d:1995-01-01T00:00:00.000Z t:year=TOTAL m:f7nd-jj28.value=52300
```

* JSON

```JSON
{
      "_2006": 46467,
      "_1996": 53613,
      "_1997": 50147,
      "_2005": 43409,
      "_1998": 49403,
      "_2004": 43537,
      "_1999": 45924,
      "_2003": 42228,
      "_2009": 46077,
      "_2008": 47717,
      "_2007": 45298,
      "_1995": 52300,
      "_2012": 43203,
      "_2000": 45884,
      "_2010": 41859,
      "_2001": 46546,
      "_2011": 41324,
      "_2002": 46945,
      "year": "TOTAL"
}
```

<!--
### Fields

| **Name** | **Type** |
|:---|:---|
| a | metric |
| b | tag |
| c | time |
| d | ignored |
-->

<!-- Insert Data set by nikitachrs-->

### Anne Arundel County Crime Rate By Type

| **Name** | **Value** |
|:---|:---|
| Id | 3fys-ggpk |
| Name | Anne Arundel County Crime Rate By Type |
| State | [Maryland](https://data.maryland.gov) |
| Description | Historical crime rates per 100,000 people, 1975 - present. |
| Attribution | MSAC |
| Category | Public Safety |
| Date Range | 1975-2012 |
| Links | [catalog](http://catalog.data.gov/dataset/anne-arundel-county-crime-rate-by-type-e5923), [metadata](https://data.maryland.gov/api/views/3fys-ggpk),  [data](https://data.maryland.gov/api/views/3fys-ggpk/rows.json?accessType=DOWNLOAD), [portal](https://apps.axibase.com/chartlab/a85c4f60) |

### Additional Commands

```ls
series e:3fys-ggpk d:1975-01-01T00:00:00.000Z m:property_crime_rate=6151.1 m:larceny_theft=3843.2
m:murder=4.8 m:robbery=124.6 m:total_crime_rate=6759.7 m:b_e=1708.6 m:agg_assault=456.9
m:m_v_theft=599.3 m:violent_crime_rate=608.6 m:rape=22.3 m:population=331390
```

* JSON

```JSON
{
      "murder": 4.8,
      "larceny_theft": 3843.2,
      "total_crime_rate": 6759.7,
      "total_crime_ratae_percent_change": null,
      "violent_crime_rate": 608.6,
      "property_crime_rate": 6151.1,
      "robbery": 124.6,
      "property_crime_rate_percent_change": null,
      "agg_assault": 456.9,
      "violent_crime_rate_percent_change": null,
      "b_e": 1708.6,
      "m_v_theft": 599.3,
      "year": 1975,
      "rape": 22.3,
      "population": 331390
}
```

### Automobiles Annual Imports and Exports Through Port Authority of NY NJ Maritime Terminals: Beginning 2000

| **Name** | **Value** |
|:---|:---|
| Id | u49g-d7hw |
| Name | Automobiles Annual Imports and Exports Through Port Authority of NY NJ Maritime Terminals: Beginning 2000 |
| State | [New York](https://data.ny.gov) |
| Description | This dataset represents the total number of Automobiles Imported and Exported annually through maritime terminals located within Port Authority property in the Port of New York and New Jersey in vehicle units beginning in 2000. |
| Attribution | The Port Authority of New York & New Jersey |
| Category | Transportation |
| Date Range | 2000-2015 |
| Links | [catalog](http://catalog.data.gov/dataset/automobiles-annual-imports-and-exports-through-port-authority-of-ny-nj-maritime-terminals-), [attribution](http://www.panynj.gov/port/pdf/port-trade-statistics-summary-2001-2011.pdf), [metadata](https://data.ny.gov/api/views/u49g-d7hw), [data](https://data.ny.gov/api/views/u49g-d7hw/rows.json?accessType=DOWNLOAD), [portal](https://apps.axibase.com/chartlab/c041c40b) |

#### Series Command

```ls
series e:u49g-d7hw d:2015-01-01T00:00:00.000Z t:type=Imports m:volume=433822
```

* JSON

```JSON
{
      "volume": 433822,
      "year": 2015,
      "type": "Imports"
}
```

### Employment Figures

| **Name** | **Value** |
|:---|:---|
| Id | je5z-53wn |
| Name | Employment Figures |
| State | [Maryland](https://data.maryland.gov) |
| Description | Figures from the Bureau of Labor Statistics, and are subject to revision. |
| Attribution | Bureau of Labor Statistics |
| Category | Business and Economy |
| Date Range | 2003-2014 |
| Links | `http://catalog.data.gov/dataset/employment-figures-f55ae`,  [portal](https://apps.axibase.com/chartlab/fc75db9b) |

### Additional Series Commands

```ls
series e:je5z-53wn d:2003-01-01T00:00:00.000Z m:maryland_jobs=2481200 m:national_jobs_created_lost=89000
m:maryland_jobs_created_lost=3800 m:national_jobs=130380000 m:maryland_unemployment_rate=4.4
m:national_unemployment_rate=5.8 m:maryland_civilian_labor_force=2877486 m:maryland_employment=2751073
m:maryland_unemployment=126413
```

* JSON

```JSON
{
      "maryland_jobs": 2481200,
      "jobs_recovered_goal_to_reach_pre_recession_peak": null,
      "national_unemployment_rate": 5.8,
      "maryland_unemployment_rate": 4.4,
      "jobs_recovered_maryland": null,
      "national_jobs_created_lost": 89000,
      "maryland_jobs_created_lost": 3800,
      "national_jobs": 130380000,
      "month": "Jan-03",
      "year": 2003,
      "maryland_job_growth_since_post_recession_bottom": null,
      "maryland_civilian_labor_force": 2877486,
      "maryland_employment": 2751073,
      "maryland_unemployment": 126413
}
```

### Solar Photovoltaic (PV) Incentive Program Completed Projects by City and Contractor: Beginning 2010

| **Name** | **Value** |
|:---|:---|
| Id | 3pzs-2zsk |
| Name | Solar Photovoltaic (PV) Incentive Program Completed Projects by City and Contractor: Beginning 2010 |
| State | [New York](https://data.ny.gov) |
| Description | The Solar Photovoltaic (PV) Incentive Program Completed Projects by City and Contractor Dataset provides market insight into the volume of work and photovoltaic (PV) capacity installed in New York State annually, by city and contractor, beginning August 2010 under the New York State Energy Research and Development Authority (NYSERDA)’s NY-Sun Solar Electric Incentive Program Opportunity Notice (PON) 2112. The dataset includes the following data points: Project Install Year, Contractor, County, City, Project Count by City, Project Cost, NYSERDA Incentives, Kilowatt Capacity, Expected Annual Kilowatt Hour Production, and NYSERDA Solicitation. |
| Attribution | New York State Energy Research and Development Authority |
| Category | Energy & Environment |
| Date Range | 2010-2015 |
| Links | `https://data.ny.gov/api/views/3pzs-2zsk`, [portal](https://apps.axibase.com/chartlab/a4936180) |

* Command

```ls
series e:3pzs-2zsk d:2010-01-01T00:00:00.000Z t:county=Allegany t:contractor=Other
t:solicitation="PON 2112" t:city=Other m:project_count_by_city=1 m:project_cost=34440
m:total_nameplate_kw=4.6 m:expected_kwh_annual_production=5399.66 m:incentive_dollars=8050
```

* JSON

```JSON
{
      "total_nameplate_kw": 4.6,
      "project_cost": 34440,
      "project_count_by_city": 1,
      "expected_kwh_annual_production": 5399.66,
      "incentive_dollars": 8050,
      "county": "Allegany",
      "contractor": "Other",
      "project_install_year": 2010,
      "solicitation": "PON 2112",
      "city": "Other"
}
```

### Table 17: Solid Waste Recycled (in tons)

| **Name** | **Value** |
|:---|:---|
| Id | v48g-wbhi |
| Name | Table 17: Solid Waste Recycled (in tons) |
| State | [Hawaii](https://data.hawaii.gov) |
| Description | DOH Environmental Indicators |
| Attribution | DOH |
| Category | Health |
| Date Range | 2004-2008 |
| Links | [catalog](http://catalog.data.gov/dataset/table-17-solid-waste-recycled-in-tons-851c9), [attribution](http://hawaii.gov/doh), [metadata](https://data.hawaii.gov/api/views/v48g-wbhi),  [data](https://data.hawaii.gov/api/views/v48g-wbhi/rows.json?accessType=DOWNLOAD),  [portal](https://apps.axibase.com/chartlab/48b1d9b2) |

* Command

```ls
series e:v48g-wbhi d:2004-01-01T00:00:00.000Z m:percent_diverted=32.5 m:disposed_statewide=1427904
m:diverted_statewide=688820 m:produced_statewide=2116724
```

* JSON

```JSON
{
      "percent_diverted": 32.5,
      "calendar_year": 2004,
      "_": 1,
      "disposed_statewide": 1427904,
      "diverted_statewide": 688820,
      "produced_statewide": 2116724
}
```

### Math And Reading Proficiency by School Year, Public School District, and Grade Level

| **Name** | **Value** |
|:---|:---|
| Id | f3h8-mnxi |
| Name | Math And Reading Proficiency by School Year, Public School District and Grade Level |
| State | [Iowa](https://data.iowa.gov) |
| Description | Dataset contains information on public school districts academic progress of their students in reading and math annually starting with school year ending in 2003.  All public schools and districts report annually to the Iowa Department of Education through Adequate Yearly Progress (AYP).<br>All AYP determinations are made annually using reading and math student assessment data.  Proficiency is based on a standard score scale.  More information can be found at: `http://itp.education.uiowa.edu/ia/AYPInformation.aspx` |
| Attribution | Iowa Department of Education, Adequate Yearly Progress |
| Category | Education |
| Date Range | 2003-2015 |
| Links | [catalog](http://catalog.data.gov/dataset/math-and-reading-proficiency-by-school-year-public-school-district-and-grade-level), [attribution](http://itp.education.uiowa.edu/ia/AYPInformation.aspx), [metadata](https://data.iowa.gov/api/views/f3h8-mnxi),  [data](https://data.iowa.gov/api/views/f3h8-mnxi/rows.json?accessType=DOWNLOAD),  [portal](https://apps.axibase.com/chartlab/bc9ba2d9) |

* Command

```ls
series e:f3h8-mnxi d:2003-01-01T00:00:00.000Z t:topic=Reading t:district_name=Central
t:proficient_category="60.1 - 70%" m:total=59 m:proficient_2=67.8 m:grade=11
m:district=1080 m:proficient_1=40
```

* JSON

```JSON
{
      "total": 59,
      "topic": "Reading",
      "proficient_2": 67.8,
      "district_name": "Central",
      "grade": 11,
      "district": "1080",
      "school_year": 2003,
      "proficient_category": "60.1 - 70%",
      "proficient_1": 40
}
```

### AAA Fuel Prices

| **Name** | **Value** |
|:---|:---|
| Id | dqp6-3idi |
| Name | AAA Fuel Prices |
| State | [Hawaii](https://data.hawaii.gov) |
| Description | AAA Monthly Fuel Prices |
| Attribution | Department of Economic Development and Tourism |
| Category | Economic Development |
| Date Range | 2006-2012 |
| Links | [catalog](http://catalog.data.gov/dataset/aaa-fuel-prices-52bf0), [attribution](http://hawaii.gov/dbedt),  [metadata](https://data.hawaii.gov/api/views/dqp6-3idi),  [data](https://data.hawaii.gov/api/views/dqp6-3idi/rows.json?accessType=DOWNLOAD),  [portal](https://apps.axibase.com/chartlab/ee379926) |

* Command

```ls
series e:dqp6-3idi d:2006-01-01T00:00:00.000Z t:county=US t:fuel="Gasoline - Regular"
t:physicalunit=Dollars m:price=2.314
```

* JSON

```JSON
{
      "price": 2.314,
      "county": "US",
      "month_of_price": "2006-01-01T00:00:00",
      "fuel": "Gasoline - Regular",
      "physicalunit": "Dollars"
}
```

### Sales and Use Tax per Town by NAICS (2013 and 2014)

| **Name** | **Value** |
|:---|:---|
| Id | rkm7-uwkb |
| Name | Sales and Use Tax per Town by NAICS (2013 and 2014) |
| State | [Connecticut](https://data.ct.gov) |
| Description | Sales and use tax data, by quarter, by town, disaggregated by the North America Industrial Classification (NAICS) groups for calendar years 2013 and 2014.  The data available is unique to each municipality as detailed NAICS information is only provided where there are ten or more taxpayers in a given category.<br>This data will be updated annually so that all four quarters of a calendar year are available at once.  This list reflects the tax collected at both the 6.35% and 7% rates, where applicable. |
| Attribution | Department of Revenue Services |
| Category | Government |
| Date Range | 2013-2014 |
| Links | [catalog](http://catalog.data.gov/dataset/sales-and-use-tax-per-town-by-naics-2013-and-2014), [attribution](http://www.ct.gov/drs/cwp/view.asp?a=4128&q=483506), [metadata](https://data.ct.gov/api/views/rkm7-uwkb),  [data](https://data.ct.gov/api/views/rkm7-uwkb/rows.json?accessType=DOWNLOAD), [portal](https://apps.axibase.com/chartlab/6be07c75) |

* Command

```ls
series e:rkm7-uwkb d:2014-01-01T00:00:00.000Z t:naics_industry_code="230 Construction"
t:municipality="OUT OF COUNTRY" m:taxpayer_count=16 m:total_tax_due_at_7=0
m:retail_sales_of_goods=0 m:total_tax_due_at_6_35=0
```

* JSON

```JSON
{
      "naics_industry_code": "230 Construction",
      "taxpayer_count": 16,
      "total_tax_due_at_7": 0,
      "retail_sales_of_goods": 0,
      "periods_ending": "Quarter 1 - JAN to MAR",
      "municipality": "OUT OF COUNTRY ",
      "calendar_year": 2014,
      "total_tax_due_at_6_35": 0
}
```

### Per Capita Electricity Consumption

| **Name** | **Value** |
|:---|:---|
| Id | 64jf-g2fe |
| Name | Per Capita Electricity Consumption |
| State | [Maryland](https://data.maryland.gov) |
| Description | Data are provided by the Maryland Energy Administration (MEA). The data shows per capita electricity usage overall and usage demand during times of peak electricity use (peak demand). |
| Attribution | MEA |
| Category | Energy and Environment |
| Date Range | 2007-2015 |
| Links | `http://catalog.data.gov/dataset/per-capita-electricity-consumption-7b888`, [portal](https://apps.axibase.com/chartlab/db5aa772) |

* Command

```ls
series e:64jf-g2fe d:2007-01-01T00:00:00.000Z m:per_capita_consumption_2015_goal=10.521
m:actual_per_capita_consumption=12.38 m:empower_per_capita_consumption_annual_goal=12.38
m:peak_demand_2015_goal=2.173 m:per_capita_consumption_2015_goal_percent_below_baseline=-15
m:peak_demand_percent_below_2007_baseline_goal_15=0 m:empower_peak_demand_annual_goals=2.56
m:per_capita_consumption_percent_below_2007_baseline=0
m:peak_demand_2015_goal_percent_below_baseline=-15 m:peak_demand_annual_goals_percent_below_baseline=0
m:actual_peak_demand=2.56 m:consumption_annual_goals_percent_below_baseline=0
```

* JSON

```JSON
{
      "peak_demand_2015_goal": 2.173,
      "peak_demand_percent_below_2007_baseline_goal_15": 0,
      "peak_demand_annual_goals_percent_below_baseline": 0,
      "actual_peak_demand": 2.56,
      "per_capita_consumption_2015_goal": 10.521,
      "empower_per_capita_consumption_annual_goal": 12.38,
      "actual_per_capita_consumption": 12.38,
      "per_capita_consumption_2015_goal_percent_below_baseline": -15,
      "empower_peak_demand_annual_goals": 2.56,
      "per_capita_consumption_percent_below_2007_baseline": 0,
      "year": 2007,
      "projected_per_capita_peak_demand_percent_below_baseline": null,
      "peak_demand_2015_goal_percent_below_baseline": -15,
      "projected_per_capita_consumption_percent_below_baseline": null,
      "consumption_annual_goals_percent_below_baseline": 0,
      "projected_per_capita_peak_demand": null,
      "projected_per_capita_consumption": null
}
```

### MVA Vehicle Sales Counts by Month for CY 2002 - 2015

| **Name** | **Value** |
|:---|:---|
| Id | un65-7ipd |
| Name | MVA Vehicle Sales Counts by Month for CY 2002-2015 |
| State | [Maryland](https://data.maryland.gov) |
| Description | The number of new and used vehicles and the sales dollars respectively sold by month. Data as of October 2015. |
| Attribution | Motor Vehicle Administration |
| Category | Transportation |
| Date Range | 2007-2015 |
| Links | [catalog](http://catalog.data.gov/dataset/mva-vehicle-sales-counts-by-month-for-cy-2002-2015), [attribution](http://www.mva.maryland.gov/), [metadata](https://data.maryland.gov/api/views/un65-7ipd),  [data](https://data.maryland.gov/api/views/un65-7ipd/rows.json?accessType=DOWNLOAD), [portal](https://apps.axibase.com/chartlab/f2083bc9) |

* Command

```ls
series e:un65-7ipd d:2002-01-01T00:00:00.000Z m:new=31106 m:total_sales_used=386481929
m:used=49927 m:total_sales_new=755015820
```

* JSON

```JSON
{
      "new": 31106,
      "month": "JAN",
      "year": 2002,
      "total_sales_used": 386481929,
      "used": 49927,
      "total_sales_new": 755015820
}
```

### DAS HR Almanac - Executive Branch Employment By Race

| **Name** | **Value** |
|:---|:---|
| Id | qm34-pq7e |
| Name | DAS HR Almanac - Executive Branch Employment By Race |
| State | [Connecticut](https://data.ct.gov) |
| Description | This data is reflective of the State of Connecticut Executive Branch workforce only.  The data does not reflect employees of the University of Connecticut Health Center, University of Connecticut, and Board of Regents which includes the state university system and community colleges.  Judicial Branch and Legislative Branch employees are also not reflected in this data. |
| Attribution | DAS Human Resources |
| Category | Government |
| Date Range | 2003-2015 |
| Links | [catalog](http://catalog.data.gov/dataset/das-hr-almanac-executive-branch-employment-by-race),  [metadata](https://data.ct.gov/api/views/qm34-pq7e),  [data](https://data.ct.gov/api/views/qm34-pq7e/rows.json?accessType=DOWNLOAD), [portal](https://apps.axibase.com/chartlab/88942f63) |

* Command

```ls
series e:qm34-pq7e d:2003-01-01T00:00:00.000Z m:other=920 m:white=27361 m:unknown=235
m:amer_indian=117 m:hispanic=2956 m:black=6559 m:asian=568
```

* JSON

```JSON
{
      "other": 920,
      "white": 27361,
      "year": 2003,
      "unknown": 235,
      "amer_indian": 117,
      "hispanic": 2956,
      "black": 6559,
      "asian": 568
 }
```

### Scholarship Recipients and Dollars by Sector Group: Beginning 2009

| **Name** | **Value** |
|:---|:---|
| Id | d8hf-wqd9 |
| Name | Scholarship Recipients and Dollars by Sector Group: Beginning 2009 |
| State | [New York](https://data.ny.gov) |
| Description | This data includes the number of Scholarship award recipients and dollar amounts by TAP Sector Group beginning with the 2009 academic year (for HESC-administered scholarships only). |
| Attribution | New York State Higher Education Services Corporation |
| Category | Education |
| Date Range | 2009-2014 |
| Links | [catalog](http://catalog.data.gov/dataset/scholarship-recipients-and-dollars-by-sector-group-beginning-2009), [atribution](http://www.hesc.ny.gov/content.nsf/SFC/Grants_Scholarships_and_Awards), [metadata](https://data.ny.gov/api/views/d8hf-wqd9),  [data](https://data.ny.gov/api/views/d8hf-wqd9/rows.json?accessType=DOWNLOAD), [portal](https://apps.axibase.com/chartlab/9026c3d7) |

* Command

```ls
series e:d8hf-wqd9 d:2014-01-01T00:00:00.000Z t:tap_sector_group="3-SUNY SO"
t:scholarship_name="Flight 3407 Memorial Scholarship" m:scholarship_dollars=42954
m:scholarship_fte=2.5 m:scholarship_headcount=3
```

* JSON

```JSON
{
      "academic_year": 2014,
      "scholarship_dollars": 42954,
      "scholarship_name": "Flight 3407 Memorial Scholarship",
      "tap_sector_group": "3-SUNY SO",
      "scholarship_fte": 2.5,
      "scholarship_headcount": 3
}
```

### Public Assistance and SNAP Fraud Prevention Performance Measures: Beginning 2013

| **Name** | **Value** |
|:---|:---|
| Id | uubd-eei2 |
| Name | Public Assistance and SNAP Fraud Prevention Performance Measures: Beginning 2013 |
| State | [New York](https://data.ny.gov) |
| Description | This dataset from the New York State Office of Temporary and Disability Assistance contains the results of several local district investigations initiated by flagged cases of the State’s cash public assistance programs and the Supplemental Nutrition Assistance Program (SNAP).  It includes information from the Front End Detection System (FEDS), the Intentional Program Violations (IPVs), Prison matches, and from the Public Assistance Reporting Information System (PARIS). |
| Attribution | New York State Office of Temporary and Disability Assistance (OTDA) |
| Category | Human Services |
| Date Range | 2013-2016 |
| Links | [catalog](http://catalog.data.gov/dataset/public-assistance-and-snap-fraud-prevention-performance-measures-beginning-2013), [attribution](https://otda.ny.gov/resources/welfare-fraud/), [metadata](https://data.ny.gov/api/views/uubd-eei2),  [data](https://data.ny.gov/api/views/uubd-eei2/rows.json?accessType=DOWNLOAD), [portal](https://apps.axibase.com/chartlab/0e4a225d) |

* Command

```ls
series e:uubd-eei2 d:2013-01-01T00:00:00.000Z t:district=Albany m:prison_unresolved=0
m:prison_closed_resolved=75 m:feds_total_investigated=33 m:prison_exonerated_resolved=25
m:total_ipvs=24 m:paris_closed_resolved=30 m:feds_cases_no_impact=0
m:paris_total_matches=215 m:ipv_positive_investigations=17 m:paris_unresolved=0
m:paris_exonerated_resolved=60 m:feds_cases_no_errors=39 m:prison_total_matches=65
m:prison_closed_prior_resolved=0 m:feds_cases_referred=1 m:feds_cases_denied_grant_reduced=61
m:paris_closed_prior_resolved=9
```

* JSON

```JSON
{
      "prison_unresolved": 0,
      "prison_closed_resolved": 75,
      "feds_total_investigated": 33,
      "prison_exonerated_resolved": 25,
      "district_cd": 1,
      "total_ipvs": 24,
      "paris_closed_resolved": 30,
      "feds_cases_no_impact": 0,
      "paris_total_matches": 215,
      "ipv_positive_investigations": 17,
      "paris_unresolved": 0,
      "paris_exonerated_resolved": 60,
      "feds_cases_no_errors": 39,
      "prison_total_matches": 65,
      "year": 2013,
      "prison_closed_prior_resolved": 0,
      "district": "Albany",
      "feds_cases_referred": 1,
      "feds_cases_denied_grant_reduced": 61,
      "paris_closed_prior_resolved": 9,
      "quarter": 1
}
```

### Maryland Veterans Unemployment Rate

| **Name** | **Value** |
|:---|:---|
| Id | prxf-ppu5 |
| Name | Maryland Veterans Unemployment Rate |
| State | [Maryland](https://data.maryland.gov) |
| Description | This data set contains the veterans unemployment rate in Maryland. Figures come from the Bureau of Labor Statistics, and are subject to revision. |
| Attribution | Bureau of Labor Statistics |
| Category | Business and Economy |
| Date Range | 2009-2014 |
| Links | [catalog](http://catalog.data.gov/dataset/maryland-veterans-unemployment-rate-3ea61), [attribution](http://www.bls.gov/), [metadata](https://data.maryland.gov/api/views/prxf-ppu5),  [data](https://data.maryland.gov/api/views/prxf-ppu5/rows.json?accessType=DOWNLOAD), [portal](https://apps.axibase.com/chartlab/61e23fa5) |

* Command

```ls
series e:prxf-ppu5 d:2010-01-01T00:00:00.000Z m:maryland_veterans_unemployment_rate=5
m:national_veterans_unemployment_rate=8.7
```

* JSON

```JSON
{
      "maryland_veterans_unemployment_rate": 5,
      "year": 2010,
      "national_veterans_unemployment_rate": 8.7
}
```

### Trips Taken on Public Transit by Transit Type - Monthly Total Trips

| **Name** | **Value** |
|:---|:---|
| Id | 5ymg-2p8u |
| Name | Trips Taken on Public Transit by Transit Type - Monthly Total Trips |
| State | [Maryland](https://data.maryland.gov) |
| Description | Data are provided by the Maryland Transit Administration (MTA). This data set includes total trips taken by bus, metro, rail, and mobility/paratransit services. Beginning in FY2014, the Maryland Transit Administration (MTA) began counting Core Bus ridership using an Automated Passenger Count (APC) system to better track the number of people boarding and leaving the buses. In order to maintain the integrity of historical comparisons for the Transit Ridership Goal, the MTA used ridership estimate differences between the new APC system and previous counting estimates for its Bus Service to allow for apples-to-apples comparisons between fiscal years. |
| Attribution | Maryland Transit Authority |
| Category | Transportation |
| Date Range | 2007-2016 |
| Links | [catalog](http://catalog.data.gov/dataset/trips-taken-on-public-transit-by-transit-type-4abd1), [attribution](http://mta.maryland.gov/), [metadata](https://data.maryland.gov/api/views/5ymg-2p8u),  [data](https://data.maryland.gov/api/views/5ymg-2p8u/rows.json?accessType=DOWNLOAD), [portal](https://apps.axibase.com/chartlab/fd596ed9) |

* Command

```ls
series e:5ymg-2p8u d:2007-07-06T00:00:00.000Z m:marc_total=566473 m:bus=5022875
m:metro=1062276 m:total_ridership=7560691 m:mobility=66973 m:light_rail=563420
m:commuter_bus_total=249082 m:taxi_access_trips=29592
```

* JSON

```JSON
{
      "fiscal_year": 2007,
      "washington": null,
      "marc_total": 566473,
      "bus": 5022875,
      "icc": null,
      "metro": 1062276,
      "baltimore": null,
      "month": "Jul-06",
      "total_ridership": 7560691,
      "mobility": 66973,
      "light_rail": 563420,
      "commuter_bus_total": 249082,
      "taxi_access_trips": 29592
}
```

### Employee Compensation by Industry in Iowa

| **Name** | **Value** |
|:---|:---|
| Id | yrss-ncc4 |
| Name | Employee Compensation by Industry in Iowa |
| State | [Iowa](https://data.iowa.gov) |
| Description | This dataset contains employee compensation estimates in thousands of dollars, seasonally adjusted at annual rates.  All dollar estimates are in current dollars (not adjusted for inflation).  Compensation is the total remuneration, both monetary and in kind, payable by employers to employees in return for their work during the period. It consists of wages and salaries and of supplements to wages and salaries. Compensation is presented on an accrual basis - that is, it reflects compensation liabilities incurred by the employer in a given period regardless of when the compensation is actually received by the employee. The estimates of compensation by industry for 1998-2006 are based on the 2002 North American Industry Classification System (NAICS). The estimates for 2007-2010 are based on the 2007 NAICS. The estimates for 2011 forward are based on the 2012 NAICS. |
| Attribution | U.S. Department of Commerce, Bureau of Economic Analysis, Compensation of Employees by Industry (SQ6, SQ6N) |
| Category | Economy |
| Date Range | 1998-2016 |
| Links | [catalog](http://catalog.data.gov/dataset/employee-compensation-by-industry-in-iowa), [attribution](http://www.bea.gov/itable/index.cfm), [metadata](https://data.iowa.gov/api/views/yrss-ncc4),  [data](https://data.iowa.gov/api/views/yrss-ncc4/rows.json?accessType=DOWNLOAD), [portal](https://apps.axibase.com/chartlab/f5eae012) |

* Command

```ls
series e:yrss-ncc4 d:1998-03-31T00:00:00.000Z t:industry_type=Farm t:industry=Farm m:compensation=351164
```

* JSON

```JSON
{
      "compensation": 351164,
      "quarter_ending": "1998-03-31T00:00:00",
      "industry_type": "Farm",
      "industry": "Farm"
}
```

## Messages

* Datasets

| **State** | **Name** | **Attribution** |
|:---|:---|:---|
| Connecticut | [Insurance Company Complaints, Resolutions, Status, and Recoveries](#insurance-company-complaints-resolutions-status-and-recoveries) | Department of Insurance |
| New York | [Lottery Powerball Winning Numbers: Beginning 2010](#lottery-powerball-winning-numbers-beginning-2010) | New York State Gaming Commission |
| New York | [Lottery Mega Millions Winning Numbers: Beginning 2002](#lottery-mega-millions-winning-numbers-beginning-2002) | New York State Gaming Commission |
| Oregon | [New Business List - June](#new-business-list---june) |  |
| Oregon | [UCC List of Filings Entered Last Month](#ucc-list-of-filings-entered-last-month) |  |
| New York | [Lottery Cash 4 Life Winning Numbers: Beginning 2014](#lottery-cash-4-life-winning-numbers-beginning-2014) | New York State Gaming Commission |
| Connecticut | [Accidental Drug Related Deaths 2012-2015](#accidental-drug-related-deaths-2012-2015) | Office of the Chief Medical Examiner |
| Oregon | [Oregon Consumer Complaints](#oregon-consumer-complaints) | Oregon Department of Justice |
| Hawaii | [OAHU Food Establishments](#oahu-food-establishments) | Department of Health |
| New York | [Parolees Under Community Supervision: Beginning 2008](#parolees-under-community-supervision-beginning-2008) | NYS Department of Corrections and Community Supervision |
| New York | [State Liquor Authority (SLA) Brand Label and Wholesaler Information for Alcoholic Beverage Products Registered in New York State](#state-liquor-authority-sla-brand-label-and-wholesaler-information-for-alcoholic-beverage-products-registered-in-new-york-state) | NYSLA Wholesale Bureau / NYSITS |
| Connecticut | [Information Technology Project Portfolio](#information-technology-project-portfolio) | Oregon Military Department |
| Oregon | [UCC Secured Parties List](#ucc-secured-parties-list) |  |

<!--
### Attorney General Consumer Complaints

| **Name** | **Value** |
|:---|:---|
| Id | gpri-47xz |
| Name | Attorney General Consumer Complaints |
| State | [Washington](https://data.wa.gov) |
| Description | Complaint data from consumer complaints filed with the Consumer Protection Division. <br>The existence of a complaint is not evidence of wrongdoing. |
| Attribution | Washington State Attorney General's Office Consumer Protection Division |
| Date Range | 2013-2016 |
| Links | [catalog](http://catalog.data.gov/dataset/attorney-general-consumer-complaints),    [metadata](https://data.wa.gov/api/views/gpri-47xz),  [data](https://data.wa.gov/api/views/gpri-47xz/rows.json?accessType=DOWNLOAD), [portal](https://apps.axibase.com/chartlab/ad6653c1) |

* Command

```ls
message e:gpri-47xz d:2016-04-12T00:00:00.000Z t:id=483906 t:businesszip=98148-1220 t:openedyear=2016.0
t:naics="713940-Fitness & Recreational Industries" t:businessstate=WA
t:source="Washington State Attorney General's Office Consumer Protection Division" t:status=Open
t:business_id=257432 t:type="Attorney General Consumer Complaints" t:business="Highline Athletic Club"
t:businesscity=Burien
```

#### JSON

```JSON
{
      "actualsavings": null,
      "businesszip": "98148-1220",
      "openedyear": 2016,
      "businessstate": "WA",
      "naicsname": null,
      "openeddate": "2016-04-12T00:00:00",
      "status": "Open",
      "business": "Highline Athletic Club",
      "businessstreetline2": null,
      "businessstreetline1": null,
      "id": "483906",
      "estimatedsavings": null,
      "naics": "713940-Fitness &amp; Recreational Industries",
      "businesscategory": null,
      "business_id": "257432",
      "businesscity": "Burien"
}
```

-->

### Insurance Company Complaints, Resolutions, Status, and Recoveries

| **Name** | **Value** |
|:---|:---|
| Id | t64r-mt64 |
| Name | Insurance Company Complaints, Resolutions, Status, and Recoveries |
| State | [Connecticut](https://data.ct.gov) |
| Description | Listing of consumer complaints filed against Insurance companies licensed in Connecticut.<br>This dataset includes the Company, Line of Business, nature of complaint, outcome or resolution, and recovery. |
| Attribution | Department of Insurance |
| Category | Business |
| Date Range | 2007-2016 |
| Links | [catalog](http://catalog.data.gov/dataset/insurance-company-complaints-resolutions-status-and-recoveries), [attribution](http://www.ct.gov/cid), [metadata](https://data.ct.gov/api/views/t64r-mt64),  [data](https://data.ct.gov/api/views/t64r-mt64/rows.json?accessType=DOWNLOAD), [portal](https://apps.axibase.com/chartlab/b1200161) |

* Command

```ls
message e:t64r-mt64 d:2013-05-15T00:00:00.000Z t:file_no=302165.0 t:source="Department of Insurance"
t:coverage="Auto Medical Payment" t:reason="Unfair Claims Practice" t:status=Closed
t:company="21st Century Assurance Company" t:subreason="Claim Delays" t:closed=2013-08-13T00:00:00
t:conclusion=Unjustified t:type=Business t:disposition="Claim Settled" t:recovery=2586.0
```

* JSON

```JSON
{
     "file_no": 302165,
      "status": "Closed",
      "reason": "Unfair Claims Practice",
      "coverage": "Auto Medical Payment",
      "subreason": "Claim Delays",
      "company": "21st Century Assurance Company",
      "conclusion": "Unjustified",
      "closed": "2013-08-13T00:00:00",
      "recovery": 2586,
      "disposition": "Claim Settled",
      "opened": "2013-05-15T00:00:00"
}
```

### Lottery Powerball Winning Numbers: Beginning 2010

| **Name** | **Value** |
|:---|:---|
| Id | d6yy-54nr |
| Name | Lottery Powerball Winning Numbers: Beginning 2010 |
| State | [New York](https://data.ny.gov) |
| Description | Go to `http://on.ny.gov/1GpWiHD` on the New York Lottery website for past Powerball results and payouts. |
| Attribution | New York State Gaming Commission |
| Category | Government & Finance |
| Date Range | 2010-2016 |
| Links | [catalog](http://catalog.data.gov/dataset/lottery-powerball-winning-numbers-beginning-2010), [attribution](http://nylottery.ny.gov/wps/portal/Home/Lottery/home/your+lottery/drawing+results/drawingresults_powerball), [metadata](https://data.ny.gov/api/views/d6yy-54nr),  [data](https://data.ny.gov/api/views/d6yy-54nr/rows.json?accessType=DOWNLOAD), [portal](https://apps.axibase.com/chartlab/09133023) |

* Command

```ls
message e:d6yy-54nr d:2010-02-03T00:00:00.000Z t:source="New York State Gaming Commission"
t:type="Government & Finance" t:multiplier=2.0 m:"17 22 36 37 52 24"
```

* JSON

```JSON
{
      "draw_date": "2010-02-03T00:00:00",
      "winning_numbers": "17 22 36 37 52 24",
      "multiplier": 2
}
```

### Lottery Mega Millions Winning Numbers: Beginning 2002

| **Name** | **Value** |
|:---|:---|
| Id | 5xaw-6ayf |
| Name | Lottery Mega Millions Winning Numbers: Beginning 2002 |
| State | [New York](https://data.ny.gov) |
| Description | Go to `http://on.ny.gov/1J8tPSN` on the New York Lottery website for past Mega Millions results and payouts.|
| Attribution | New York State Gaming Commission |
| Category | Government & Finance |
| Date Range | 2002-2016 |
| Links | [catalog](http://catalog.data.gov/dataset/lottery-mega-millions-winning-numbers-beginning-2002), [attribution](http://nylottery.ny.gov/wps/portal/Home/Lottery/home/your+lottery/drawing+results/drawingresultsmega), [metadata](https://data.ny.gov/api/views/5xaw-6ayf),  [data](https://data.ny.gov/api/views/5xaw-6ayf/rows.json?accessType=DOWNLOAD), [portal](https://apps.axibase.com/chartlab/3084bd37) |

* Command

```ls
message e:5xaw-6ayf d:2002-05-17T00:00:00.000Z t:source="New York State Gaming Commission"
t:type="Government & Finance" t:mega_ball=30 m:"15 18 25 33 47"
```

* JSON

```JSON
{
      "draw_date": "2002-05-17T00:00:00",
      "winning_numbers": "15 18 25 33 47",
      "multiplier": null,
      "mega_ball": "30"
}
```

### New Business List - June

| **Name** | **Value** |
|:---|:---|
| Id | i8h7-mn6v |
| Name | New Business List - June |
| State | [Oregon](https://data.oregon.gov) |
| Description | Businesses registered with the Secretary of State Corporation Division during the month of June. |
| Category | Business |
| Date Range | June 2016 |
| Links | [catalog](http://catalog.data.gov/dataset/new-business-list-june-1accb),  [metadata](https://data.oregon.gov/api/views/i8h7-mn6v),  [data](https://data.oregon.gov/api/views/i8h7-mn6v/rows.json?accessType=DOWNLOAD), [portal](https://apps.axibase.com/chartlab/83760504) |

* Command

```ls
message e:i8h7-mn6v d:2016-06-01T00:00:00.000Z t:business_name="12 STONE CONTRACTING GROUP, INC."
t:associated_name_type="MAILING ADDRESS" t:source=i8h7-mn6v t:zip_code=31106 t:address="PO BOX 8958"
t:state=GA t:type=Business t:entity_type="FOREIGN BUSINESS CORPORATION"
t:city=ATLANTA t:registry_number=122151194
```

* JSON

```JSON
{
      "zip_code": "31106",
      "middle_name": null,
      "state": "GA",
      "address_continued": null,
      "suffix": null,
      "city": "ATLANTA",
      "registry_number": "122151194",
      "business_name": "12 STONE CONTRACTING GROUP, INC.",
      "associated_name_type": "MAILING ADDRESS",
      "first_name": null,
      "entity_of_record_name": null,
      "address": "PO BOX 8958",
      "not_of_record_entity": null,
      "registry_date": "2016-06-01T00:00:00",
      "last_name": null,
      "entity_type": "FOREIGN BUSINESS CORPORATION",
      "entity_of_record_reg_number": null
}
```

### UCC List of Filings Entered Last Month

| **Name** | **Value** |
|:---|:---|
| Id | snfi-f79b |
| Name | UCC List of Filings Entered Last Month |
| State | [Oregon](https://data.oregon.gov) |
| Description | Updated 8/1/2016. List of New UCC filings entered during the previous month.  This list will be updated by the 9th of every month. |
| Category | Business |
| Date Range | July 2016 |
| Links | [catalog](http://catalog.data.gov/dataset/ucc-list-of-filings-entered-last-month-7c45d),  [metadata](https://data.oregon.gov/api/views/snfi-f79b),  [data](https://data.oregon.gov/api/views/snfi-f79b/rows.json?accessType=DOWNLOAD), [portal](https://apps.axibase.com/chartlab/6e35e121) |

* Command

```ls
message e:snfi-f79b d:2016-07-28T00:00:00.000Z t:lapse_date=2022-01-27T00:00:00 t:file_number=1866-23
t:entity="KEYBANK NATIONAL ASSOCIATION" t:st_cd_txt=OH t:zip_code_txt=44144 t:type=Business
t:file_type=AMENDMENT t:lien_type=UCC t:source=snfi-f79b t:city_descr=BROOKLYN t:party_type=SP
t:entity_type=ORG t:mail_addr_1="4910 TIEDEMAN ROAD" t:cntry_cd_txt=USA t:original_file_number=1866
```

* JSON

```JSON
{
      "lapse_date": "2022-01-27T00:00:00",
      "lien_type": "UCC",
      "city_descr": "BROOKLYN",
      "file_number": "1866-23",
      "party_type": "SP",
      "entity": "KEYBANK NATIONAL ASSOCIATION",
      "st_cd_txt": "OH",
      "zip_code_txt": "44144",
      "mail_addr_2": null,
      "mail_addr_1": "4910 TIEDEMAN ROAD",
      "entity_type": "ORG",
      "cntry_cd_txt": "USA",
      "filing_date": "2016-07-28T00:00:00",
      "original_file_number": "1866",
      "file_type": "AMENDMENT"
}
```

### Lottery Cash 4 Life Winning Numbers: Beginning 2014

| **Name** | **Value** |
|:---|:---|
| Id | kwxv-fwze |
| Name | Lottery Cash 4 Life Winning Numbers: Beginning 2014 |
| State | [New York](https://data.ny.gov) |
| Description | Go to `http://on.ny.gov/1xRIvPz` on the New York Lottery website for past Cash 4 Life results and payouts. |
| Attribution | New York State Gaming Commission |
| Category | Government & Finance |
| Date Range | 2014-2016 |
| Links | [catalog](http://catalog.data.gov/dataset/lottery-cash-4-life-winning-numbers-beginning-2014), [attribution](http://nylottery.ny.gov/wps/portal/Home/Lottery/home/your+lottery/drawing+results/drawingresults_cash4life), [metadata](https://data.ny.gov/api/views/kwxv-fwze),  [data](https://data.ny.gov/api/views/kwxv-fwze/rows.json?accessType=DOWNLOAD), [portal](https://apps.axibase.com/chartlab/954ff842) |

* Command

```ls
message e:kwxv-fwze d:2014-06-16T00:00:00.000Z t:source="New York State Gaming Commission"
t:type="Government & Finance" t:cash_ball=03 m:"09 36 44 53 59"
```

* JSON

```JSON
{
      "draw_date": "2014-06-16T00:00:00",
      "winning_numbers": "09 36 44 53 59",
      "cash_ball": "03"
}
```

### Accidental Drug Related Deaths 2012-2015

| **Name** | **Value** |
|:---|:---|
| Id | rybz-nyjw |
| Name | Accidental Drug Related Deaths  2012-2015 |
| State | [Connecticut](https://data.ct.gov) |
| Description | A listing of each accidental death associated with drug overdose in Connecticut from 2012 to 2015. A "Y" value under the different substance columns indicates whether that particular substance was detected. Data is derived from an investigation by the Office of the Chief Medical Examiner which includes the toxicity report, death certificate, as well as a scene investigation. The "Morphine (Not Heroin)" values are related to the differences between how Morphine and Heroin are metabolized and therefore detected in the toxicity results. Heroin metabolizes to 6-MAM which then metabolizes to morphine.  6-MAM is unique to heroin, and has a short half-life (as does heroin itself). Thus, in some heroin deaths, the toxicity results will not indicate whether the morphine is from heroin or prescription morphine. In these cases the Medical Examiner may be able to determine the cause based on the scene investigation (such as  finding heroin needles). If they find prescription morphine at the scene it is certified as "Morphine (not heroin)." Therefore, the Cause of Death may indicate Morphine, but the Heroin or Morphine (Not Heroin) may not be indicated. "Any Opioid" – if the Medical Examiner cannot conclude whether the cause of death is from RX Morphine or heroin based morphine in the toxicity results, that column may be checked |
| Attribution | Office of the Chief Medical Examiner |
| Category | Health and Human Services |
| Date Range | 2012-2015 |
| Links | [catalog](http://catalog.data.gov/dataset/accidental-drug-related-deaths-january-2012-sept-2015), [attribution](http://www.ct.gov/ocme), [metadata](https://data.ct.gov/api/views/rybz-nyjw),  [data](https://data.ct.gov/api/views/rybz-nyjw/rows.json?accessType=DOWNLOAD), [portal](https://apps.axibase.com/chartlab/80aaea79) |

* Command

```ls
message e:rybz-nyjw d:2014-06-28T00:00:00.000Z t:casenumber=14-9876 t:hydr_cod=Y
t:source="Office of the Chief Medical Examiner" t:mannerofdeath=Accident t:benzo_s=Y
t:type="Health and Human Services" t:fentanyl=Y m:"Acute fent, hydrocod, benzodiazepine"
```

* JSON

```JSON
{
      "residence_county": null,
      "residence_state": null,
      "sex": null,
      "other": null,
      "amendedmannerofdeath": null,
      "location": null,
      "date": "2014-06-28T00:00:00",
      "race": null,
      "injuryplace": null,
      "death_state": null,
      "hydr_cod": "Y",
      "mannerofdeath": "Accident",
      "age": null,
      "benzo_s": "Y",
      "methadone": null,
      "any_opioid": null,
      "oxyc": null,
      "etoh": null,
      "tramad": null,
      "immediatecausea": "Acute fent, hydrocod, benzodiazepine",
      "death_city": null,
      "fentanyl": "Y",
      "morphine_not_heroin": null,
      "oxym": null,
      "casenumber": "14-9876",
      "residence_city": null,
      "amphet": null,
      "death_county": null,
      "coc": null,
      "heroin": null
}
```

### Oregon Consumer Complaints

| **Name** | **Value** |
|:---|:---|
| Id | 2ix7-8hwk |
| Name | Oregon Consumer Complaints |
| State | [Oregon](https://data.oregon.gov) |
| Description | Consumer complaints registered with the Oregon Deptartment of Justice.  The database of consumer complaints is derived from consumer contacts for the past 3 years and is for information only. This database may not offer a completely accurate or comprehensive account of every incident. Several factors, including a company’s size and volume of transactions, may affect the likelihood of a consumer complaint being filed. The number of complaints about a business may not be a reliable measure as to whether it is appropriately conducting business. The information in this database is updated as soon as possible. However, recently submitted complaints may not be immediately available. The statements in this database do not necessarily reflect the opinion of the DOJ. For more information, see `http://www.doj.state.or.us/finfraud/index.shtml` |
| Attribution | Oregon Department of Justice |
| Category | Public Safety |
| Date Range | 2013-2016 |
| Links | [catalog](http://catalog.data.gov/dataset/oregon-consumer-complaints-7f511), [attribution](http://www.doj.state.or.us/), [metadata](https://data.oregon.gov/api/views/2ix7-8hwk),  [data](https://data.oregon.gov/api/views/2ix7-8hwk/rows.json?accessType=DOWNLOAD), [portal](https://apps.axibase.com/chartlab/00c21bea) |

* Command

```ls
message e:2ix7-8hwk d:2014-03-05T00:00:00.000Z t:respondent="7-ELEVEN, INC*" t:zip=752210711
t:status=Closed t:closing_description="Voluntarily Resolved" t:state=TX t:address_1="CUSTOMER RELATIONS"
t:reference_no_=FF1411-14 t:address_2="PO BOX 711" t:type="Public Safety" t:city=DALLAS
t:source="Oregon Department of Justice" t:date_closed=2014-06-27T00:00:00
t:business_type="Fuel: Gasoline Stations"
m:"Provided goods or services different than the ones complainant ordered; unauthorized work"
```

* JSON

```JSON
{
      "complaint_description": "Provided goods or services different than the ones complainant ordered;
            unauthorized work",
      "respondent": "7-ELEVEN, INC*",
      "zip": "752210711",
      "status": "Closed ",
      "closing_description": "Voluntarily Resolved",
      "state": "TX",
      "date_open": "2014-03-05T00:00:00",
      "date_closed": "2014-06-27T00:00:00",
      "address_1": "CUSTOMER RELATIONS",
      "reference_no_": "FF1411-14",
      "address_2": "PO BOX 711",
      "business_type": "Fuel: Gasoline Stations",
      "city": "DALLAS"
}
```

### OAHU Food Establishments

| **Name** | **Value** |
|:---|:---|
| Id | qkvm-skze |
| Name | OAHU Food Establishments |
| State | [Hawaii](https://data.hawaii.gov) |
| Description | Lists represent all of the permitted Food Establishments.  These include everything from restaurants, take out, fast-food, convenience stores, mom and pop markets, shave ice stands, supermarkets, mega markets (such as Costco, Sam’s, and Walmart), lunch wagons, food manufacturers, etc. |
| Attribution | Department of Health |
| Category | Health |
| Date Range | 2005-2012 |
| Links | [catalog](http://catalog.data.gov/dataset/oahu-food-establishments-8adda), [metadata](https://data.hawaii.gov/api/views/qkvm-skze),  [data](https://data.hawaii.gov/api/views/qkvm-skze/rows.json?accessType=DOWNLOAD), [portal](https://apps.axibase.com/chartlab/fdef2e30) |

* Command

```ls
message e:qkvm-skze d:2011-07-25T00:00:00.000Z t:tmkzone=1.0 t:facility_permit=8807.0
t:establishment="MATSUMOTO'S OKAZUYA RESTAURANT, LLC" t:facility_type="137 New and Renewal 1"
t:tmkparcel=24.0 t:permit_expire_date=2013-08-02T00:00:00 t:mailing_address_zip_code=96817 t:tmkplat=7.0
t:permit_holder="TODD MATSUMOTO" t:type=Health t:source="Department of Health"
t:establishment_address_zip_code=96817 t:risk_category="Category 1"
t:mailing_address_street_name="GULICK AVENUE" t:business_status=Open t:establishment_address_state=HAWAII
t:establishment_address_city=HONOLULU t:mailing_address_state=HAWAII t:telephone=(808)721-7464
t:establishment_address_street_name="GULICK AVENUE" t:establishment_permit=8807.0 t:tmksection=3.0
t:mailing_address_city=HONOLULU
```

* JSON

```JSON
{
      "establishment_address_unit": "   ",
      "tmkzone": 1,
      "facility_permit": 8807,
      "tmkparcel": 24,
      "permit_holder": "TODD MATSUMOTO",
      "po_box": null,
      "st_inspection": "2011-07-25T00:00:00",
      "mailing_address_street_name": "GULICK AVENUE ",
      "business_status": "Open",
      "establishment_address_city": "HONOLULU",
      "mailing_address_state": "HAWAII",
      "establishment_permit": 8807,
      "mailing_address_city": "HONOLULU",
      "tmksection": 3,
      "mailing_address_unit": "   ",
      "establishment": "MATSUMOTO'S OKAZUYA RESTAURANT, LLC",
      "facility_type": "137 New and Renewal 1",
      "permit_expire_date": "2013-08-02T00:00:00",
      "mailing_address_zip_code": "96817",
      "tmkplat": 7,
      "mailing_care_of": null,
      "establishment_address_zip_code": "96817",
      "risk_category": "Category 1",
      "establishment_address_state": "HAWAII",
      "telephone": "(808)721-7464",
      "establishment_address_street_name": "GULICK AVENUE "
}
```

### Parolees Under Community Supervision: Beginning 2008

| **Name** | **Value** |
|:---|:---|
| Id | pmxm-gftz |
| Name | Parolees Under Community Supervision: Beginning 2008 |
| State | [New York](https://data.ny.gov) |
| Description | Provides data about parolees under community supervision on March 31 of the snapshot year. Information includes region of supervision, county of residence, snapshot year, supervision level, gender, age as of the file date, and crime type for most serious instant offense. |
| Attribution | NYS Department of Corrections and Community Supervision |
| Category | Public Safety |
| Date Range | 2008-2015 |
| Links | [catalog](http://catalog.data.gov/dataset/parolees-under-community-supervision-beginning-2008), [metadata](https://data.ny.gov/api/views/pmxm-gftz),  [data](https://data.ny.gov/api/views/pmxm-gftz/rows.json?accessType=DOWNLOAD), [portal](https://apps.axibase.com/chartlab/3bc9ae9a) |

* Command

```ls
message e:pmxm-gftz d:2008-01-01T00:00:00.000Z t:region=WILLARD
t:source="NYS Department of Corrections and Community Supervision" t:county=SENECA
t:crime="DRUG OFFENSES" t:age=29.0 t:gender=MALE t:type="Public Safety"
```

* JSON

```JSON
{
      "region": "WILLARD",
      "county": "SENECA",
      "crime": "DRUG OFFENSES",
      "age": 29,
      "snapshot_year": 2008,
      "supervision_level": null,
      "gender": "MALE"
}
```

### State Liquor Authority (SLA) Brand Label and Wholesaler Information for Alcoholic Beverage Products Registered in New York State

| **Name** | **Value** |
|:---|:---|
| Id | n2dz-pwuk |
| Name | State Liquor Authority (SLA) Brand Label and Wholesaler Information for Alcoholic Beverage Products Registered in New York State |
| State | [New York](https://data.ny.gov) |
| Description | Brand Label and Wholesale Information for Alcohol Products Registered in New York State. The New York State Alcohol Beverage Control Law specifies that no manufacturer or wholesaler shall sell to any retailer nor shall any retailer purchase any alcoholic beverages unless these beverages are labeled in accordance with the Authority's Rules and Federal Regulations, and unless such labels shall be registered with and approved by the State Liquor Authority. Effective January 1, 1994, wine does not need to be brand label registered if the wine has received label approval from the Bureau of Alcohol, Tobacco, and Firearms (BATF). |
| Attribution | NYSLA Wholesale Bureau / NYSITS |
| Category | Economic Development |
| Date Range | 2016-2018 |
| Links | [catalog](http://catalog.data.gov/dataset/state-liquor-authority-sla-brand-label-and-wholesaler-information-for-alcoholic-beverage-p), [metadata](https://data.ny.gov/api/views/n2dz-pwuk),  [data](https://data.ny.gov/api/views/n2dz-pwuk/rows.json?accessType=DOWNLOAD), [portal](https://apps.axibase.com/chartlab/f83cf3ff) |

* Command

```ls
message e:n2dz-pwuk d:2017-06-30T00:00:00.000Z t:brand_label_serial_number=5002370
t:wholesaler_name="MATT BREWING CO INC" t:source="NYSLA Wholesale Bureau / NYSITS"
t:brand_label_name="SARANAC PALE ALE" t:license_class_code=650 t:wholesaler_license_serial_number=2503534
t:license_type_code=1 t:domestic_d_or_imported_i=D t:type="Economic Development" t:product_description=ALE
t:license_class_description=ALE
```

* JSON

```JSON
{
      "brand_label_serial_number": "5002370",
      "wholesaler_name": "MATT BREWING CO INC",
      "wholesaler_license_serial_number": "2503534",
      "license_class_code": "650",
      "brand_label_name": "SARANAC PALE ALE",
      "license_type_code": "1",
      "domestic_d_or_imported_i": "D",
      "product_description": "ALE",
      "license_class_description": "ALE",
      "brand_label_expiration_date": "2017-06-30T00:00:00"
}
```

### Information Technology Project Portfolio

| **Name** | **Value** |
|:---|:---|
| Id | i7h5-rx65 |
| Name | Information Technology Project Portfolio |
| State | [Connecticut](https://data.ct.gov) |
| Description | This dataset includes Information Technology projects reported to the Office of Policy and Management by each state agency.  The dataset is updated on a quarterly basis minimally and includes active projects as well as completed projects (Post-Implementation). |
| Attribution | Oregon Military Department |
| Category | Government |
| Date Range | 2015-2016 |
| Links | [catalog](http://catalog.data.gov/dataset/information-technology-project-portfolio), [attribution](http://www.ct.gov/opm), [metadata](https://data.ct.gov/api/views/i7h5-rx65),  [data](https://data.ct.gov/api/views/i7h5-rx65/rows.json?accessType=DOWNLOAD), [portal](https://apps.axibase.com/chartlab/0653c6b5) |

* Command

```ls
message e:i7h5-rx65 d:2015-12-30T13:11:00.000Z t:project_health=Green t:level=1.0
t:project_name="Virtual Desktop Pilot" t:source="Office of Policy and Management"
t:it_capital_investment_fund=0.0 t:project_start_date=2013-03-04T00:00:00
t:planned_project_end_date=2014-02-05T00:00:00 t:total_budget=500000.0
t:project_phase="Post Implementation" t:type=Government t:agency_name="Department of Children and Families"
m:"Pilot the use of virtual desktops or virtual applications in the agency."
```

* JSON

```JSON
{
      "project_health": "Green",
      "project_name": "Virtual Desktop Pilot",
      "date_information_is_being_provided": "2015-12-30T13:11:00",
      "level": 1,
      "it_capital_investment_fund": 0,
      "project_start_date": "2013-03-04T00:00:00",
      "project_phase": "Post Implementation",
      "total_budget": 500000,
      "planned_project_end_date": "2014-02-05T00:00:00",
      "agency_name": "Department of Children and Families",
      "project_description": "Pilot the use of virtual desktops or virtual applications in the agency."
}
```

### UCC Secured Parties List

| **Name** | **Value** |
|:---|:---|
| Id | 2kf7-i54h |
| Name | UCC Secured Parties List |
| State | [Oregon](https://data.oregon.gov) |
| Description | Updated 8/1/2016. List of All Active Filings and their associated Secured Parties. This Dataset will be updated monthly by the 9th of each month. |
| Category | Business |
| Date Range | 1970-2016 |
| Links | [catalog](http://catalog.data.gov/dataset/ucc-secured-parties-list-23e64),  [metadata](https://data.oregon.gov/api/views/2kf7-i54h),  [data](https://data.oregon.gov/api/views/2kf7-i54h/rows.json?accessType=DOWNLOAD), [portal](https://apps.axibase.com/chartlab/4a12f7d4) |

* Command

```ls
message e:2kf7-i54h d:1991-07-02T00:00:00.000Z t:filenumber=104008 t:postalcode=97290-6550
t:lapse_date=2021-07-02T00:00:00 t:secured_party="KEY BANK OF OREGON" t:source=2kf7-i54h
t:addr1="PO BOX 66550" t:state=OR t:lt_cd=UCC t:type=Business t:city=PORTLAND t:country=USA
```

* JSON

```JSON
{
      "postalcode": "97290-6550",
      "filenumber": "104008",
      "secured_party": "KEY BANK OF OREGON",
      "lapse_date": "2021-07-02T00:00:00",
      "addr1": "PO BOX 66550",
      "addr2": null,
      "state": "OR",
      "lt_cd": "UCC",
      "image_link": [
         "http://records.sos.state.or.us/webdrawer/webdrawer.dll/webdrawer/rec/1901587/view",
         null
      ],
      "filing_date": "1991-07-02T00:00:00",
      "country": "USA",
      "city": "PORTLAND"
}
```
