$(document).ready(function () {
    $("progress_container").hide();
    document.getElementById("progress_container").style.display = 'none';
    var $branches = $("#branches-select");
    var $branches2 = $("#branches-select2");
    var $select_years_to = $('#select_years_to');
    var $select_years_from = $('#select_years_from');
    var $select_years_to_2 = $('#select_years_to_2');
    var $select_years_from_2 = $('#select_years_from_2');
    var $subjects = $("#subjects-select");
    var $subjects2 = $("#subjects-select2");
    var allbranches = [];
    var allschools = [];
    var allyears = [];
  //  var colors = [ 'rgba(158, 27, 72, 0.9)', 'rgba(255, 10, 50, 0.9)', 'rgba(86, 23, 148, 0.9)', 'rgba(62, 146, 2, 0.9)', 'rgba(7, 160, 163, 0.9)', 'rgba(146, 137, 24, 0.9)', 'rgba(111, 24, 170, 0.9)','rgba(0,174,219,0.9)','rgba(162,0,255,0.9)','rgba(0,0,0,0.9)','rgba(212,18,67,0.9)','rgba(96,35,32,0.9)','rgba(243,119,53,0.9)','rgba(209,17,65,0.9)','rgba(0,177,89,0.9)','rgba(55,56,84,0.9)','rgba(255, 51, 159 ,0.9)','rgba(245, 61, 61  ,0.9)','rgba(36, 113, 163,0.9)','rgba(125, 206, 160,0.9)','rgba(120, 40, 31  ,0.9)','rgba(156, 109, 50 ,0.9)','rgba(71, 156, 50,0.9)','rgba(156, 50, 82,0.9)','rgba(31, 255, 12,0.9)', 'rgba(157, 142, 12, 0.9)','rgba(151, 60, 110, 0.9)', 'rgba(173, 167, 15, 0.9)', 'rgba(71, 24, 135, 0.9)', 'rgba(155, 106, 42, 0.9)', 'rgba(33, 17, 132, 0.9)', 'rgba(163, 2, 88, 0.9)', 'rgba(25, 139, 83, 0.9)', 'rgba(118, 85, 31, 0.9)', 'rgba(156, 123, 29, 0.9)', 'rgba(146, 7, 120, 0.9)', 'rgba(100, 129, 36, 0.9)', 'rgba(144, 22, 128, 0.9)', 'rgba(18, 105, 154, 0.9)', 'rgba(64, 139, 14, 0.9)', 'rgba(59, 174, 4, 0.9)', 'rgba(138, 171, 9, 0.9)', 'rgba(20, 147, 32, 0.9)', 'rgba(95, 22, 150, 0.9)', 'rgba(121, 61, 40, 0.9)', 'rgba(30, 136, 78, 0.9)', 'rgba(62, 48, 152, 0.9)', 'rgba(92, 32, 150, 0.9)', 'rgba(44, 136, 134, 0.9)', 'rgba(62, 62, 143, 0.9)', 'rgba(126, 87, 31, 0.9)', 'rgba(146, 52, 60, 0.9)', 'rgba(32, 141, 15, 0.9)', 'rgba(6, 173, 103, 0.9)', 'rgba(114, 127, 36, 0.9)', 'rgba(34, 123, 21, 0.9)', 'rgba(142, 16, 116, 0.9)', 'rgba(55, 162, 47, 0.9)', 'rgba(83, 160, 11, 0.9)', 'rgba(2, 178, 138, 0.9)', 'rgba(132, 20, 125, 0.9)', 'rgba(168, 13, 77, 0.9)', 'rgba(18, 100, 128, 0.9)', 'rgba(80, 167, 33, 0.9)', 'rgba(36, 123, 38, 0.9)', 'rgba(44, 15, 165, 0.9)', 'rgba(66, 32, 175, 0.9)', 'rgba(120, 107, 25, 0.9)', 'rgba(24, 170, 44, 0.9)', 'rgba(163, 44, 26, 0.9)', 'rgba(134, 42, 101, 0.9)', 'rgba(37, 32, 133, 0.9)', 'rgba(22, 143, 10, 0.9)', 'rgba(77, 154, 40, 0.9)', 'rgba(38, 124, 155, 0.9)', 'rgba(92, 162, 16, 0.9)', 'rgba(7, 150, 132, 0.9)', 'rgba(140, 172, 0, 0.9)', 'rgba(24, 68, 121, 0.9)', 'rgba(150, 149, 12, 0.9)', 'rgba(86, 140, 36, 0.9)', 'rgba(43, 128, 142, 0.9)', 'rgba(7, 35, 167, 0.9)', 'rgba(61, 149, 136, 0.9)', 'rgba(153, 83, 38, 0.9)', 'rgba(130, 3, 147, 0.9)', 'rgba(145, 12, 29, 0.9)', 'rgba(98, 123, 37, 0.9)', 'rgba(54, 64, 142, 0.9)', 'rgba(136, 25, 125, 0.9)', 'rgba(163, 56, 30, 0.9)', 'rgba(3, 122, 162, 0.9)', 'rgba(46, 160, 36, 0.9)', 'rgba(8, 17, 160, 0.9)', 'rgba(179, 67, 16, 0.9)', 'rgba(136, 146, 42, 0.9)', 'rgba(133, 16, 144, 0.9)', 'rgba(14, 49, 170, 0.9)', 'rgba(42, 39, 162, 0.9)', 'rgba(179, 35, 112, 0.9)', 'rgba(32, 164, 74, 0.9)', 'rgba(150, 139, 47, 0.9)', 'rgba(63, 94, 148, 0.9)', 'rgba(112, 148, 6, 0.9)', 'rgba(4, 144, 152, 0.9)', 'rgba(57, 133, 142, 0.9)', 'rgba(78, 166, 29, 0.9)', 'rgba(107, 165, 15, 0.9)', 'rgba(54, 140, 69, 0.9)', 'rgba(23, 42, 176, 0.9)', 'rgba(153, 57, 76, 0.9)', 'rgba(58, 146, 62, 0.9)', 'rgba(132, 150, 50, 0.9)', 'rgba(70, 39, 124, 0.9)', 'rgba(173, 21, 79, 0.9)', 'rgba(7, 178, 45, 0.9)', 'rgba(141, 25, 158, 0.9)', 'rgba(121, 141, 33, 0.9)', 'rgba(115, 147, 40, 0.9)', 'rgba(34, 166, 136, 0.9)', 'rgba(49, 125, 144, 0.9)', 'rgba(99, 32, 143, 0.9)', 'rgba(48, 80, 160, 0.9)'];
    var $schools = $("#schools-select");
    var barGraphDiv = document.getElementById("academicBar");
    var barLayout;
    var lineGraphDiv = document.getElementById("academicLine");

    var config = {
        modeBarButtonsToRemove: ['autoScale2d', 'resetScale2d',
            'hoverClosestCartesian', 'hoverCompareCartesian', 'zoom2d', 'pan2d', 'select2d', 'lasso2d', 'zoomIn2d', 'zoomOut2d'
        ],
        displaylogo: false
    };

    function ajaxCallsFunc(type, url, contentType, data, callback) {
        $.ajax({
            type: type,
            url: url,
            contentType: contentType,
            data: data,
            success: callback
        });
    }

    ajaxCallsFunc('POST', "http://41.164.192.98:5000/Branches", 'application/json', null, function (branches) {
        console.log(branches);
        $.each(branches, function (i, branch) {
            $branches.append('<option value="' + branch + '">' + branch + '</option>');
            $branches.material_select();
            $branches2.append('<option value="' + branch + '">' + branch + '</option>');
            $branches2.material_select();
            allbranches.push(branch);
        });
    });
    ajaxCallsFunc('POST', "http://41.164.192.98:5000/GetTimeYears", 'application/json', null, function (years) {
        console.log(years);
        $.each(years, function (i, year) {
            $select_years_to.append('<option value="' + year + '">' + year + '</option>');
            $select_years_to.material_select();
            $select_years_from.append('<option value="' + year + '">' + year + '</option>');
            $select_years_from.material_select();
            allyears.push(year);
        });

        //For Acedmic over trend
        $.each(years, function (i, year) {
            $select_years_to_2.append('<option value="' + year + '">' + year + '</option>');
            $select_years_to_2.material_select();
            $select_years_from_2.append('<option value="' + year + '">' + year + '</option>');
            $select_years_from_2.material_select();
            allyears.push(year);
        });

    });

    ajaxCallsFunc('POST', "http://41.164.192.98:5000/GetSchools", 'application/json', null, function (schools) {
        console.log(schools);
        $.each(schools, function (i, school) {
            $schools.append('<option value="' + school + '">' + school + '</option>');
            $schools.material_select();
            allschools.push(school);
        });
    });

    var branchList = [];
    var allSubjects = [];
    $("#generateSubjects").click(function () {
        var filtertype = $('input[name=group1]:checked').val();
        var filterDatetype = $('input[name=time_selection]:checked').val();
        if (filtertype == "Branch") {
            branchList = $("#branches-select").val();
        } else if (filtertype == "allbranches") {
            filtertype = "Branch";
            branchList = allbranches;

        } else if (filtertype == "School") {
            branchList = $("#schools-select").val();
        } else if (filtertype == "allschools") {
            filtertype = "School";
            branchList = allschools;
        }

        var datefrom = "";
        var dateto = "";

        if (filterDatetype == 'time_selected') {

            datefrom = $('.datepickerFrom').val();
            dateto = $('.datepickerTo').val();

        } else {

            selected_term_to = $('#term-select_to').val();
            selected_term_from = $('#term-select_from').val();

            seleted_year_to = $('#select_years_to').val();
            seleted_year_from = $('#select_years_from').val();


            dateto = selected_term_from + "|" + seleted_year_from;
            datefrom = selected_term_to + "|" + seleted_year_to;

            //    console.log("to");
            //    console.log(selected_term_to);
            //    console.log(seleted_year_to);
            //    console.log("from");
            //    console.log(selected_term_from);
            //    console.log(seleted_year_from);

        }


        // var datefrom = $('.datepickerFrom').val();
        // var dateto = $('.datepickerTo').val();
        var gradeList = $("#grades-select").val();
        var tempStr = gradeList.join();
        gradeList = tempStr.split(",");
        var data = JSON.stringify({
            "subjectList": [""],
            "instituteList": branchList,
            "gradeList": gradeList,
            "DateFrom": datefrom,
            "DateTo": dateto,
            "flag": 6,
            "filtertype": filtertype
        });
        allSubjects = []
        //console.log(data + "  <-- Sent data");
        ajaxCallsFunc('POST', "http://41.164.192.98:5000/AcademicGraph", 'application/json', data, function (subjects) {
            console.log(subjects);
            $.each(subjects, function (i, subjects) {
                $subjects.append('<option value="' + subjects + '">' + subjects + '</option>');
                $subjects.material_select();
                console.log(subjects)
                allSubjects.push(subjects);
            });
        });
    });
    var flagtext;
    var title1 = "";
    var tempLis = [];
    $("#drawgraph").click(function () {
        document.getElementById("progress_container").style.display = 'block';

        tempLis = [];
        var datefrom = "";
        var datato = "";
        var filtertype = $('input[name=group1]:checked').val();
        var filterDatetype = $('input[name=time_selection]:checked').val();
        if (filtertype == "Branch") {
            branchList = $("#branches-select").val();
        } else if (filtertype == "allbranches") {
            filtertype = "Branch";
            branchList = allbranches;

        } else if (filtertype == "School") {
            branchList = $("#schools-select").val();
        } else if (filtertype == "allschools") {
            filtertype = "School";
            branchList = allschools;
        }

        var subjectFilterType = $('input[name=subjectGroup]:checked').val();
        if (subjectFilterType == "allsubjects") {
            subjectList = allSubjects;
        } else if (subjectFilterType == "subjects") {
            subjectList = $("#subjects-select").val();
        }

        // var branchList = $("#branches-select").val();
        var gradeList = $("#grades-select").val();
        var tempStr = gradeList.join();
        gradeList = tempStr.split(",");
        if (filterDatetype == 'time_selected') {

            datefrom = $('.datepickerFrom').val();
            dateto = $('.datepickerTo').val();

        } else {

            selected_term_to = $('#term-select_to').val();
            selected_term_from = $('#term-select_from').val();

            seleted_year_to = $('#select_years_to').val();
            seleted_year_from = $('#select_years_from').val();

            dateto = selected_term_from + "|" + seleted_year_from;
            datefrom = selected_term_to + "|" + seleted_year_to;

        }
        var flag = parseInt($('#flag-select').val());
        flagtext = $("#flag-select option:selected").text()

        var comparisonList = [];
        if ($('#term-checkbox').is(':checked')) {
            comparisonList.push($("#term-select").val());
            comparisonList.push($("#term-select2").val());
        }
        //console.log(subjectList, branchList, filtertype, flag, gradeList, datefrom, dateto, comparisonList);
        title1 = "Academic: (" + datefrom + ")-(" + dateto + ") <br /> Grades: (" + gradeList + ") <br />" + filtertype + " (" + branchList + ")";

        if (!($('#term-checkbox').is(':checked'))) {
            var data = JSON.stringify({
                "subjectList": subjectList,
                "instituteList": branchList,
                "gradeList": gradeList,
                "DateFrom": datefrom,
                "DateTo": dateto,
                "flag": flag,
                "filtertype": filtertype
            });
            console.log(data);
            ajaxCallsFunc('POST', "http://41.164.192.98:5000/AcademicGraph", 'application/json', data, function (response) {
                console.log(response);
                var graphData = {
                    type: "bar",
                    x: [],
                    y: [],
                    text: [],
                    textposition: 'auto',
                    hoverinfo: 'none'
                };
                for (var branch in response) {
                    console.log(branch);
                    graphData['x'].push(branch);
                    graphData['y'].push(response[branch]);
                    graphData['text'].push(response[branch]);
                    //   console.log(response[branch]);
                    //tempLis.push(graphData);
                }
                tempLis.push(graphData);
                document.getElementById("progress_container").style.display = 'none';
                var layout = {
                    title: "Something"
                };
                if (flag == 2) {
                    //alert ("Calledf");
                    Plotly.newPlot(barGraphDiv, tempLis, {
                        yaxis: {
                            title: flagtext,
                            range: [0, 100]
                        },
                        title: title1,
                        titlefont: {
                            size: 12
                        },
                        layout
                    }, config);
                } else {
                    Plotly.newPlot(barGraphDiv, tempLis, {
                        yaxis: {
                            title: flagtext
                        },
                        title: title1,
                        titlefont: {
                            size: 12

                        },
                        layout
                    }, config);
                }
            });
        } else if (($('#term-checkbox').is(':checked'))) {
            //bargraph

            var data = JSON.stringify({
                "subjectList": subjectList,
                "instituteList": branchList,
                "gradeList": gradeList,
                "DateFrom": datefrom,
                "DateTo": dateto,
                "flag": flag,
                "comparisonList": comparisonList,
                "filtertype": filtertype
            });
            console.log(data);

            ajaxCallsFunc('POST', "http://41.164.192.98:5000/AcademicGraph", 'application/json', data, function (response) {
                console.log(response);
                for (var subject in response) {
                    var graphData = {
                        name,
                        x: [],
                        y: [],
                        type: 'bar'
                    };
                    graphData['name'] = subject;
                    for (var term in response[subject]) {
                        graphData['x'].push(term);
                        graphData['y'].push(response[subject][term]);
                    }
                    tempLis.push(graphData);
                }
                console.log(graphData);
                console.log(tempLis)
                document.getElementById("progress_container").style.display = 'none';


                var d3 = Plotly.d3;

                var WIDTH_IN_PERCENT_OF_PARENT = 60,
                    HEIGHT_IN_PERCENT_OF_PARENT = 80;

                var gd3 = d3.select('body')
                    .append('div')
                    .style({
                        width: WIDTH_IN_PERCENT_OF_PARENT + '%',
                        'margin-left': (100 - WIDTH_IN_PERCENT_OF_PARENT) / 2 + '%',

                        height: HEIGHT_IN_PERCENT_OF_PARENT + 'vh',
                        'margin-top': (100 - HEIGHT_IN_PERCENT_OF_PARENT) / 2 + 'vh'
                    });

                var gd = gd3.node();


                if (flag == 2) {

                    Plotly.newPlot(barGraphDiv, tempLis, {
                        barmode: 'group',
                        yaxis: {
                            title: flagtext,
                            range: [0, 100]
                        },
                        title: title1,
                        titlefont: {
                            size: 12

                        }

                    }, config);
                } else {


                    Plotly.newPlot(barGraphDiv, tempLis, {
                        barmode: 'group',
                        yaxis: {
                            title: flagtext
                        },
                        title: title1,
                        titlefont: {
                            size: 12

                        }

                    }, config);
                }


            });
        }
    });

    $("#generateSubjects2").click(function () {

        var datefrom = "";
        var dateto = "";
        var allsubjects = [];
        var group2 = $('input[name=group2]:checked').val();
        var filterDatetype = $('input[name=time_selection_2]:checked').val();
        if (group2 == "Branch") {
            var branchList = $("#branches-select2").val();
        } else if (group2 == "allbranches") {
            var branchList = allbranches;
        }
        if (filterDatetype == 'time_selected_2') {

            datefrom = $('.datepickerFrom2').val();
            dateto = $('.datepickerTo2').val();

        } else {

            selected_term_to = $('#term-select_to_2').val();
            selected_term_from = $('#term-select_from_2').val();

            seleted_year_to = $('#select_years_to_2').val();
            seleted_year_from = $('#select_years_from_2').val();

            dateto = selected_term_from + "|" + seleted_year_from;
            datefrom = selected_term_to + "|" + seleted_year_to;

            console.log("to");
            console.log(selected_term_to);
            console.log(seleted_year_to);
            console.log("from");
            console.log(selected_term_from);
            console.log(seleted_year_from);





        }



        var gradeList = $("#grade-select2").val();
        var tempStr = gradeList.join();
        gradeList = tempStr.split(",");
        // var datefrom = $('.datepickerFrom2').val();
        // var dateto = $('.datepickerTo2').val();

        var data = JSON.stringify({
            "subjectList": [""],
            "instituteList": branchList,
            "gradeList": gradeList,
            "DateFrom": datefrom,
            "DateTo": dateto,
            "flag": 6,
            "filtertype": ""
        });
        console.log(data + "  <-- Sent data");
        ajaxCallsFunc('POST', "http://41.164.192.98:5000/AcademicGraph", 'application/json', data, function (subjects) {
            console.log(subjects);
            $.each(subjects, function (i, subjects) {
                $subjects2.append('<option value="' + subjects + '">' + subjects + '</option>');
                $subjects2.material_select();
                allSubjects.push(subjects);
            });
        });
    });

    var title3 = "";
    var lineGraphData = [];
    $("#drawgraph2").click(function () {
        subjectList = [];
        document.getElementById("progress_container").style.display = 'block';
        console.log("All subjects" + allSubjects);
        lineGraphData = [];
        var datefrom = "";
        var dateto = "";
        var subjectFilterType2 = $('input[name=subjectGroup2]:checked').val();
        if (subjectFilterType2 == "allsubjects") {
            subjectList = allSubjects;
        } else if (subjectFilterType2 == "subjects") {
            subjectList = $("#subjects-select2").val();
        }

        var filterDatetype = $('input[name=time_selection_2]:checked').val();
        var group2 = $('input[name=group2]:checked').val();
        if (group2 == "Branch") {
            var branchList = $("#branches-select2").val();
        } else if (group2 == "allbranches") {
            //  filtertype = "Branch";
            var branchList = allbranches;
        }



        if (filterDatetype == 'time_selected_2') {

            datefrom = $('.datepickerFrom2').val();
            dateto = $('.datepickerTo2').val();

        } else {

            selected_term_to = $('#term-select_to_2').val();
            selected_term_from = $('#term-select_from_2').val();

            seleted_year_to = $('#select_years_to_2').val();
            seleted_year_from = $('#select_years_from_2').val();

            dateto = selected_term_from + "|" + seleted_year_from;
            datefrom = selected_term_to + "|" + seleted_year_to;

        }




        var gradeList = $("#grade-select2").val();
        var tempStr = gradeList.join();
        gradeList = tempStr.split(",");
        // var datefrom = $('.datepickerFrom2').val();
        // var dateto = $('.datepickerTo2').val();
        title3 = "Academic: (" + datefrom + ")-(" + dateto + ") Grades (" + gradeList + ") <br>" + "Branches (" + branchList + ")";
        console.log(subjectList, branchList, gradeList, datefrom, dateto);
        //line graph
        var LineData = JSON.stringify({
            "subjectList": subjectList,
            "instituteList": branchList,
            "gradeList": gradeList,
            "DateFrom": datefrom,
            "DateTo": dateto,
            "filtertype": "Branch",
            "flag": 5
        });
        ajaxCallsFunc('POST', "http://41.164.192.98:5000/AcademicGraph", 'application/json', LineData, function (response) {
            console.log(response);
            var i = 0;
            for (var branch in response) {
                var graphData = {
                    name,
                    x: [],
                    y: [],
                    line : {
                        width:1,
                       
                    
                      }
                };
                graphData['name'] = branch;
           //     graphData['line']['color'] = colors[i];
                console.log(branch + "<-- branch");
                for (var year in response[branch]) {
                    console.log(year + "<-- year");
                    graphData['x'].push(year);
                    graphData['y'].push(response[branch][year]);
                }
                lineGraphData.push(graphData);
                i++;
            }
            // console.log(graphData);
            // console.log(lineGraphData)
            document.getElementById("progress_container").style.display = 'none';

            Plotly.newPlot(lineGraphDiv, lineGraphData, {
                yaxis: {
                    title: "Number of students"
                },
                title: title3,
                titlefont: {
                    size: 12

                }
            }, config);
        });
    });




    //resize trigger
    $(window).resize(function () {
        if (this.resizeTO) clearTimeout(this.resizeTO);
        this.resizeTO = setTimeout(function () {
            $(this).trigger('resizeEnd');
        }, 500);
    });

    //redraw graph when window resize is completed  
    $(window).on('resizeEnd', function () {
        if (($('#term-checkbox').is(':checked'))) {
            Plotly.newPlot(barGraphDiv, tempLis, {
                barmode: 'group',
                yaxis: {
                    title: flagtext
                },
                title: title1
            }, config);
        } else {
            Plotly.newPlot(barGraphDiv, tempLis, {
                yaxis: {
                    title: flagtext
                },
                title: title1,
                titlefont: {
                    size: 12

                }
            }, config);
        }
        Plotly.newPlot(lineGraphDiv, lineGraphData, {
                yaxis: {
                    title: "Number of students"
                },
                title: title3,
                titlefont: {
                    size: 12

                }
            },
            config);

    });


    //date picker
    $('.datepickerFrom').pickadate({
        selectMonths: true, // Creates a dropdown to control month
        selectYears: 15, // Creates a dropdown of 15 years to control year,
        today: 'Today',
        clear: 'Clear',
        close: 'Ok',
        format: 'yyyy-mm-dd',

        closeOnSelect: false // Close upon selecting a date,
    });
    $('.datepickerTo').pickadate({
        selectMonths: true, // Creates a dropdown to control month
        selectYears: 15, // Creates a dropdown of 15 years to control year,
        today: 'Today',
        clear: 'Clear',
        close: 'Ok',
        format: 'yyyy-mm-dd',

        closeOnSelect: false // Close upon selecting a date,
    });
    $('.datepickerFrom2').pickadate({
        selectMonths: true, // Creates a dropdown to control month
        selectYears: 15, // Creates a dropdown of 15 years to control year,
        today: 'Today',
        clear: 'Clear',
        close: 'Ok',
        format: 'yyyy-mm-dd',

        closeOnSelect: false // Close upon selecting a date,
    });
    $('.datepickerTo2').pickadate({
        selectMonths: true, // Creates a dropdown to control month
        selectYears: 15, // Creates a dropdown of 15 years to control year,
        today: 'Today',
        clear: 'Clear',
        format: 'yyyy-mm-dd',

        close: 'Ok',
        closeOnSelect: false // Close upon selecting a date,
    });

    $("input[name$='time_selection']").click(function () {
        var selected = $(this).val();
        console.log(selected);
        if (selected == 'time_term_year') {

            $('#date_from').attr('disabled', true);
            $('#date_to').attr('disabled', true);

            $('#term-select_to').attr('disabled', false);
            $('#term-select_from').attr('disabled', false);
            $('#select_years_to').attr('disabled', false);
            $('#select_years_from').attr('disabled', false);
            $('select').material_select();

        } else if (selected == 'time_selected') {

            $('#date_from').attr('disabled', false);
            $('#date_to').attr('disabled', false);


            $('#term-select_to').attr('disabled', true);
            $('#term-select_from').attr('disabled', true);
            $('#select_years_to').attr('disabled', true);
            $('#select_years_from').attr('disabled', true);
            $('select').material_select();



        }
    });


    //For Second Datetime Acedmic over trend graph 

    $("input[name$='time_selection_2']").click(function () {
        var selected = $(this).val();
        console.log(selected);
        if (selected == 'time_term_year_2') {

            $('.datepickerFrom2').attr('disabled', true);
            $('.datepickerTo2').attr('disabled', true);

            $('#term-select_to_2').attr('disabled', false);
            $('#term-select_from_2').attr('disabled', false);
            $('#select_years_to_2').attr('disabled', false);
            $('#select_years_from_2').attr('disabled', false);
            $('select').material_select();

        } else if (selected == 'time_selected_2') {

            $('.datepickerFrom2').attr('disabled', false);
            $('.datepickerTo2').attr('disabled', false);


            $('#term-select_to_2').attr('disabled', true);
            $('#term-select_from_2').attr('disabled', true);
            $('#select_years_to_2').attr('disabled', true);
            $('#select_years_from_2').attr('disabled', true);
            $('select').material_select();



        }
    });


    $('input:radio[name="group1"]').change(function () {
        if ($(this).val() == 'Branch') {
            $('#branches-select').attr('disabled', false);
            $('#branches-select').material_select();
            $('#schools-select').attr('disabled', true);


        } else if ($(this).val() == 'School') {
            $('#schools-select').attr('disabled', false);
            $('#schools-select').material_select();
            $('#branches-select').attr('disabled', true);

        }
    });

    $('select').material_select();
});