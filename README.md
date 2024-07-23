# mon_projet_behave


pip install allure-behave

pip install behave-html-formatter


pip install extent-reports


behave -f allure_behave.formatter:AllureFormatter -o allure_reports.\features

pip install behave-html-formatter 

behave -f behave_html_formatter:HTMLFormatter -o reports/test_report.html 