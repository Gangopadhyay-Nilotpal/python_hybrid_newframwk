pytest -s -v -m "sanity" --html=./_Reports/report.html .\testCases

rem pytest -s -v -m "regression" --html=./_Reports/report.html .\testCases
rem pytest -s -v -m "sanity and regression" --html=./_Reports/report.html .\testCase --browser chrome
rem pytest -s -v -m "sanity or regression" --html=./_Reports/report.html .\testCase --browser chrome