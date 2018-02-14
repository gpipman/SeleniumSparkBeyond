# SparkBeyond
Selenium Excercise
The Selenium Excercise program performs the requirements of the following document

Selenium​ ​ Exercise
Write​ ​ a ​ ​ Java,​ ​ Scala​ ​ (recommended),​ ​ Python​ ​ or​ ​ Go​ ​ program​ ​ that​ ​ implements​ ​ the​ ​ following​ ​ Web
procedures​ ​ using​ ​ Selenium.
Please​ ​ use​ ​ the​ ​ Page​ ​ Object​ ​ Model​​ ​ design​ ​ pattern​ ​ to​ ​ make​ ​ your​ ​ code​ ​ readable​ ​ and​ ​ extendable.
Please​ ​ divide​ ​ the​ ​ source​ ​ object​ ​ models​ ​ capabilities​ ​ (java​ ​ ->​ ​ src/main)​ ​ and​ ​ the​ ​ testing​ ​ source
code​ ​ (java​ ​ ->​ ​ src/test).
High​ ​ level​ ​ structure:
Please​ ​ do​ ​ not​ ​ follow​ ​ this​ ​ list​ ​ as​ ​ if​ ​ it​ ​ is​ ​ the​ ​ only​ ​ classes​ ​ in​ ​ the​ ​ source​ ​ code.
Basic​ ​ object​ ​ models​ ​ should​ ​ at​ ​ least​ ​ include:
● Login
● Main​ ​ page
● Results​ ​ page

Test​ ​ procedure:
● Go​ ​ to​ ​ http://www.udemy.com
● Login
● Select​ ​ "development"​ ​ ->​ ​ "Web​ ​ development"​ ​ (make​ ​ it​ ​ compatible​ ​ for​ ​ both​ ​ “Categories”
and​ ​ “courses​ ​ menu​ ​ bar’)
● Use​ ​ the​ ​ search​ ​ box​ ​ to​ ​ look​ ​ for​ ​ "selenium"​ ​ courses
● Choose​ ​ Price​ ​ ->​ ​ free
Test​ ​ Assertions​ ​ (pytest​ ​ recommended):
● Assert​ ​ we​ ​ get​ ​ at​ ​ least​ ​ 2 ​ ​ and​ ​ no​ ​ more​ ​ than​ ​ 10​ ​ courses
● Assert​ ​ all​ ​ courses​ ​ are​ ​ marked​ ​ "Free"
● Assert​ ​ at​ ​ least​ ​ one​ ​ course​ ​ has​ ​ the​ ​ word​ ​ "Selenium"​ ​ in​ ​ it's​ ​ title.

General:
1. Deliver​ ​ a ​ ​ GitHub​ ​ Repo​ ​ including
a. Source​ ​ code​ ​ / ​ ​ Test​ ​ source​ ​ code
b. README​ ​ - ​ ​ describe​ ​ how​ ​ to​ ​ run/compile​ ​ and​ ​ how​ ​ to​ ​ test
2. Assume​ ​ local​ ​ chromedriver​ ​ is​ ​ used​ ​ at​ ​ /usr/local/bin/chromedriver
3. Further​ ​ assumptions​ ​ should​ ​ be​ ​ written​ ​ in​ ​ README​ ​ file


How to run the program 
change directory to src and type the command :python2.7 gustavo/seleniumexcersise.py
In my computer gustavo@gustavo-desktop:/mnt/working/home/gustavo/eclipse_Selenium_workspace/github/SparkBeyond/src$ python2.7 gustavo/seleniumexcersise.py
The output is as following:
gustavo@gustavo-desktop:/mnt/working/home/gustavo/eclipse_Selenium_workspace/github/SparkBeyond/src$ python2.7 gustavo/seleniumexcersise.py
Online Courses - Anytime, Anywhere | Udemy
<div class="ellipsis">
            Categories
        </div>
<span class="menu__title">Development</span>
<span class="menu__title">Web Development</span>
Web Development Online Courses: Build and Enhance Websites
Online Courses - Anytime, Anywhere | Udemy
<span class="hidden-xxs">All Filters</span>
<div class="filter--filter-container--2BpVy"><span class="filter--filter-title--15hZ8">Price</span><div class="filter--filter-option--2ggxb checkbox"><label><input type="checkbox" value="on"><span class="checkbox-label"><span data-purpose="filter-option-title" class="filter--filter-option-text--3nAaz">Paid</span><span class="filter--filter-option-count--3QA7t"><!-- react-text: 316 --> <!-- /react-text --><!-- react-text: 317 -->117<!-- /react-text --></span></span></label></div><div class="filter--filter-option--2ggxb checkbox"><label><input type="checkbox" value="on"><span class="checkbox-label"><span data-purpose="filter-option-title" class="filter--filter-option-text--3nAaz">Free</span><span class="filter--filter-option-count--3QA7t"><!-- react-text: 324 --> <!-- /react-text --><!-- react-text: 325 -->9<!-- /react-text --></span></span></label></div></div>
<span class="filter--filter-option-count--3QA7t"><!-- react-text: 324 --> <!-- /react-text --><!-- react-text: 325 -->9<!-- /react-text --></span>
2
Gustavo
9
9
Free
Free
Free
Free
Free
Free
Free
Free
Free
.
----------------------------------------------------------------------
Ran 1 test in 29.759s

OK
