$(document).ready(function () {
    $("progress_container").hide();
    document.getElementById("progress_container").style.display = 'none';
    var $branches = $("#branches-select");
    var $schools = $("#schools-select");
    var $branches2 = $("#branches-select2");
    var $branches3 = $("#branches-select3");
    var $select_years_to = $('#select_years_to');
    var $select_years_from = $('#select_years_from');
    var $select_years_to_2 = $('#select_years_to_2');
    var $select_years_from_2 = $('#select_years_from_2');
    var $select_years_to_3 = $('#select_years_to_3');
    var $select_years_from_3 = $('#select_years_from_3');
    var allyears = [];
    //  var colors = [ 'rgba(158, 27, 72, 0.9)', 'rgba(255, 10, 50, 0.9)', 'rgba(86, 23, 148, 0.9)', 'rgba(62, 146, 2, 0.9)', 'rgba(7, 160, 163, 0.9)', 'rgba(146, 137, 24, 0.9)', 'rgba(111, 24, 170, 0.9)','rgba(0,174,219,0.9)','rgba(162,0,255,0.9)','rgba(0,0,0,0.9)','rgba(212,18,67,0.9)','rgba(96,35,32,0.9)','rgba(243,119,53,0.9)','rgba(209,17,65,0.9)','rgba(0,177,89,0.9)','rgba(55,56,84,0.9)','rgba(255, 51, 159 ,0.9)','rgba(245, 61, 61  ,0.9)','rgba(36, 113, 163,0.9)','rgba(125, 206, 160,0.9)','rgba(120, 40, 31  ,0.9)','rgba(156, 109, 50 ,0.9)','rgba(71, 156, 50,0.9)','rgba(156, 50, 82,0.9)','rgba(31, 255, 12,0.9)', 'rgba(157, 142, 12, 0.9)','rgba(151, 60, 110, 0.9)', 'rgba(173, 167, 15, 0.9)', 'rgba(71, 24, 135, 0.9)', 'rgba(155, 106, 42, 0.9)', 'rgba(33, 17, 132, 0.9)', 'rgba(163, 2, 88, 0.9)', 'rgba(25, 139, 83, 0.9)', 'rgba(118, 85, 31, 0.9)', 'rgba(156, 123, 29, 0.9)', 'rgba(146, 7, 120, 0.9)', 'rgba(100, 129, 36, 0.9)', 'rgba(144, 22, 128, 0.9)', 'rgba(18, 105, 154, 0.9)', 'rgba(64, 139, 14, 0.9)', 'rgba(59, 174, 4, 0.9)', 'rgba(138, 171, 9, 0.9)', 'rgba(20, 147, 32, 0.9)', 'rgba(95, 22, 150, 0.9)', 'rgba(121, 61, 40, 0.9)', 'rgba(30, 136, 78, 0.9)', 'rgba(62, 48, 152, 0.9)', 'rgba(92, 32, 150, 0.9)', 'rgba(44, 136, 134, 0.9)', 'rgba(62, 62, 143, 0.9)', 'rgba(126, 87, 31, 0.9)', 'rgba(146, 52, 60, 0.9)', 'rgba(32, 141, 15, 0.9)', 'rgba(6, 173, 103, 0.9)', 'rgba(114, 127, 36, 0.9)', 'rgba(34, 123, 21, 0.9)', 'rgba(142, 16, 116, 0.9)', 'rgba(55, 162, 47, 0.9)', 'rgba(83, 160, 11, 0.9)', 'rgba(2, 178, 138, 0.9)', 'rgba(132, 20, 125, 0.9)', 'rgba(168, 13, 77, 0.9)', 'rgba(18, 100, 128, 0.9)', 'rgba(80, 167, 33, 0.9)', 'rgba(36, 123, 38, 0.9)', 'rgba(44, 15, 165, 0.9)', 'rgba(66, 32, 175, 0.9)', 'rgba(120, 107, 25, 0.9)', 'rgba(24, 170, 44, 0.9)', 'rgba(163, 44, 26, 0.9)', 'rgba(134, 42, 101, 0.9)', 'rgba(37, 32, 133, 0.9)', 'rgba(22, 143, 10, 0.9)', 'rgba(77, 154, 40, 0.9)', 'rgba(38, 124, 155, 0.9)', 'rgba(92, 162, 16, 0.9)', 'rgba(7, 150, 132, 0.9)', 'rgba(140, 172, 0, 0.9)', 'rgba(24, 68, 121, 0.9)', 'rgba(150, 149, 12, 0.9)', 'rgba(86, 140, 36, 0.9)', 'rgba(43, 128, 142, 0.9)', 'rgba(7, 35, 167, 0.9)', 'rgba(61, 149, 136, 0.9)', 'rgba(153, 83, 38, 0.9)', 'rgba(130, 3, 147, 0.9)', 'rgba(145, 12, 29, 0.9)', 'rgba(98, 123, 37, 0.9)', 'rgba(54, 64, 142, 0.9)', 'rgba(136, 25, 125, 0.9)', 'rgba(163, 56, 30, 0.9)', 'rgba(3, 122, 162, 0.9)', 'rgba(46, 160, 36, 0.9)', 'rgba(8, 17, 160, 0.9)', 'rgba(179, 67, 16, 0.9)', 'rgba(136, 146, 42, 0.9)', 'rgba(133, 16, 144, 0.9)', 'rgba(14, 49, 170, 0.9)', 'rgba(42, 39, 162, 0.9)', 'rgba(179, 35, 112, 0.9)', 'rgba(32, 164, 74, 0.9)', 'rgba(150, 139, 47, 0.9)', 'rgba(63, 94, 148, 0.9)', 'rgba(112, 148, 6, 0.9)', 'rgba(4, 144, 152, 0.9)', 'rgba(57, 133, 142, 0.9)', 'rgba(78, 166, 29, 0.9)', 'rgba(107, 165, 15, 0.9)', 'rgba(54, 140, 69, 0.9)', 'rgba(23, 42, 176, 0.9)', 'rgba(153, 57, 76, 0.9)', 'rgba(58, 146, 62, 0.9)', 'rgba(132, 150, 50, 0.9)', 'rgba(70, 39, 124, 0.9)', 'rgba(173, 21, 79, 0.9)', 'rgba(7, 178, 45, 0.9)', 'rgba(141, 25, 158, 0.9)', 'rgba(121, 141, 33, 0.9)', 'rgba(115, 147, 40, 0.9)', 'rgba(34, 166, 136, 0.9)', 'rgba(49, 125, 144, 0.9)', 'rgba(99, 32, 143, 0.9)', 'rgba(48, 80, 160, 0.9)'];
    var config = {
        modeBarButtonsToRemove: ['autoScale2d', 'resetScale2d',
            'hoverClosestCartesian', 'hoverCompareCartesian', 'zoom2d', 'pan2d', 'select2d', 'lasso2d', 'zoomIn2d', 'zoomOut2d'
        ],
        displaylogo: false
    };
    var allschools = [];
    var allbranches = [];
    var barGraphDiv = document.getElementById("attendanceBar");
    var barLayout;
    var lineGraphDiv = document.getElementById("attendanceLine");
    var lineGraphDiv2 = document.getElementById("attendanceLine2");

    $('select').material_select();
    var greenColor = 'rgb(50,171, 96)';
    var redColor = 'rgb(222,45,38)';
    var yellowColor = 'rgb(232, 188, 13)';
    var blackColor = 'rgb(107, 107, 107)';



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
        //console.log(branches);
        $.each(branches, function (i, branch) {
            $branches.append('<option value="' + branch + '">' + branch + '</option>');
            $branches.material_select();
            $branches2.append('<option value="' + branch + '">' + branch + '</option>');
            $branches2.material_select();
            $branches3.append('<option value="' + branch + '">' + branch + '</option>');
            $branches3.material_select();
            allbranches.push(branch);
        });
    });
    ajaxCallsFunc('POST', "http://41.164.192.98:5000/GetTimeYears", 'application/json', null, function (years) {
        //console.log(years);
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


        //For Acedmic over trend
        $.each(years, function (i, year) {
            $select_years_to_3.append('<option value="' + year + '">' + year + '</option>');
            $select_years_to_3.material_select();
            $select_years_from_3.append('<option value="' + year + '">' + year + '</option>');
            $select_years_from_3.material_select();
            allyears.push(year);
        });

    });


    ajaxCallsFunc('POST', "http://41.164.192.98:5000/GetSchools", 'application/json', null, function (schools) {
        //  console.log(schools);
        $.each(schools, function (i, school) {
            $schools.append('<option value="' + school + '">' + school + '</option>');
            $schools.material_select();
            allschools.push(school);
        });
    });
    var tempLis = [];
    var tempLis2 = [];
    var branchList = [];
    $("#drawgraph").click(function () {
        document.getElementById("progress_container").style.display = 'block';
        tempLis = [];
        tempLis2 = [];

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

        var gradeList = $("#grades-select").val();
        var tempStr = gradeList.join();
        gradeList = tempStr.split(",");
        //var datefrom = $('.datepickerFrom').val();
        //var dateto = $('.datepickerTo').val();
        console.log(branchList, gradeList, filtertype, datefrom, dateto);
        var title1 = "Student Attendance " + gradeList + "  (" + datefrom + ")-(" + dateto + ")";
        var data2 = JSON.stringify({
            "BranchList": allbranches,
            "GradesList": gradeList,
            "filtertype": "Branch",
            "datefrom": datefrom,
            "dateto": dateto,
            "flag": 1
        });

        ajaxCallsFunc('POST', "http://41.164.192.98:5000/AttendanceGraph", 'application/json', data2, function (response) {
            var response;
            // var color1;
            var y = 0;
            for (var reason in response) {
                y= 0;
                var graphData = {
                    name,
                    x: [],
                    y: [],
                    type: 'bar',
                    marker: {
                        color: ''
                    },
                    text: ''
                };
                graphData['name'] = reason;
                if (reason == "Yellow 70-79") {
                    graphData['marker']['color'] = yellowColor;
                } else if (reason == "Red 50-69") {
                    graphData['marker']['color'] = redColor;
                }
                if (reason == "Green 80-100") {
                    graphData['marker']['color'] = greenColor;
                }
                if (reason == "Black 0-49") {
                    graphData['marker']['color'] = blackColor;
                }

                for (var branch in response[reason]) {
                    graphData['x'].push("All branches");
                    y += response[reason][branch];
                }
                graphData['y'].push(y);
                tempLis2.push(graphData);

            }

            //  console.log(tempLis)
            barLayout = {
                barmode: 'stack',
                yaxis: {
                    title: 'Number of students'
                },
                showlegend: false
            };

            Plotly.newPlot(attendanceBarAll, tempLis2, barLayout, config);
        });


        var data = JSON.stringify({
            "BranchList": branchList,
            "GradesList": gradeList,
            "filtertype": filtertype,
            "datefrom": datefrom,
            "dateto": dateto,
            "flag": 1
        });
        // console.log(data);
        ajaxCallsFunc('POST', "http://41.164.192.98:5000/AttendanceGraph", 'application/json', data, function (response) {
            for (var reason in response) {
                var graphData = {
                    name,
                    x: [],
                    y: [],
                    type: 'bar',
                    marker: {
                        color: ''
                    }

                };
                graphData['name'] = reason;
                if (reason == "Yellow 70-79") {
                    graphData['marker']['color'] = yellowColor;
                } else if (reason == "Red 50-69") {
                    graphData['marker']['color'] = redColor;
                }
                if (reason == "Green 80-100") {
                    graphData['marker']['color'] = greenColor;
                }
                if (reason == "Black 0-49") {
                    graphData['marker']['color'] = blackColor;
                }
                for (var branch in response[reason]) {
                    graphData['x'].push(branch);
                    graphData['y'].push(response[reason][branch]);
                }
                tempLis.push(graphData);

            }
            //  console.log(graphData);
            // console.log(tempLis)
            barLayout2 = {
                barmode: 'stack',
                yaxis: {
                    title: 'Number of students'
                },
                title: title1
            };
            document.getElementById("progress_container").style.display = 'none';

            Plotly.newPlot(barGraphDiv, tempLis, barLayout2, config);
        });
    });
    var lineGraphData = [];
    $("#drawgraph2").click(function () {
        document.getElementById("progress_container").style.display = 'block';
        lineGraphData = [];
        var group2 = $('input[name=group2]:checked').val();
        var filterDatetype = $('input[name=time_selection_2]:checked').val();
        if (group2 == "Branch") {
            var branchList = $("#branches-select2").val();
        } else if (group2 == "allbranches") {
            group2 = "Branch";
            var branchList = allbranches;
        }
        var datefrom = "";
        var dateto = "";

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
        // var branchList = $("#branches-select2").val();
        var gradeList = $("#grades-select2").val();
        var tempStr = gradeList.join();
        gradeList = tempStr.split(",");
        var colorList = $("#color-select").val();
        //var datefrom = $('.datepickerFrom2').val();
        //var dateto = $('.datepickerTo2').val();
        //  console.log(branchList, gradeList, colorList, datefrom, dateto);
        var title2 = "Student Attendance " + gradeList + "  (" + datefrom + ")-(" + dateto + ")";
        var LineData = JSON.stringify({
            "BranchList": branchList,
            "GradesList": gradeList,
            "ColorsList": colorList,
            "datefrom": datefrom,
            "dateto": dateto,
            "flag": 2
        });
        ajaxCallsFunc('POST', "http://41.164.192.98:5000/AttendanceGraph", 'application/json', LineData, function (response) {
            //  console.log(response);
            var i = 0;
            for (var branch in response) {
                var graphData = {
                    name,
                    x: [],
                    y: [],
                    line: {
                        width: 1,


                    }
                };
                graphData['name'] = branch;

                for (var year in response[branch]) {
                    graphData['x'].push(year);
                    graphData['y'].push(response[branch][year]);
                }
                lineGraphData.push(graphData);
                i++;
            }

            document.getElementById("progress_container").style.display = 'none';

            Plotly.newPlot(lineGraphDiv, lineGraphData, {
                yaxis: {
                    title: 'Number of students'
                },
                title: title2
            }, config);
        });
    });
    var lineGraphData2 = [];
    $("#drawgraph3").click(function () {
        document.getElementById("progress_container").style.display = 'block';
        lineGraphData2 = [];
        var filtertype = $('input[name=group3]:checked').val();
        var filterDatetype = $('input[name=time_selection_3]:checked').val();
        if (filtertype == "Branch") {
            var branchList = $("#branches-select3").val();
        } else if (filtertype == "allbranches") {
            filtertype = "Branch";
            var branchList = allbranches;
        }


        var datefrom = "";
        var dateto = "";

        if (filterDatetype == 'time_selected_3') {

            datefrom = $('.datepickerFrom3').val();
            dateto = $('.datepickerTo3').val();

        } else {

            selected_term_to = $('#term-select_to_3').val();
            selected_term_from = $('#term-select_from_3').val();

            seleted_year_to = $('#select_years_to_3').val();
            seleted_year_from = $('#select_years_from_3').val();


            dateto = selected_term_from + "|" + seleted_year_from;
            datefrom = selected_term_to + "|" + seleted_year_to;


        }
        //   var branchList = $("#branches-select3").val();
        var gradeList = $("#grades-select3").val();
        var tempStr = gradeList.join();
        gradeList = tempStr.split(",");
        var colorList = $("#color-select3").val();
        //var datefrom = $('.datepickerFrom3').val();
        //var dateto = $('.datepickerTo3').val();
        // console.log(branchList, gradeList, colorList, datefrom, dateto);
        var title3 = "Student Attendance " + gradeList + "  (" + datefrom + ")-(" + dateto + ")" + "<br> Branches: " + branchList;
        var LineData = JSON.stringify({
            "BranchList": branchList,
            "GradesList": gradeList,
            "ColorsList": colorList,
            "datefrom": datefrom,
            "dateto": dateto,
            "flag": 3
        });
        ajaxCallsFunc('POST', "http://41.164.192.98:5000/AttendanceGraph", 'application/json', LineData, function (response) {

            // console.log(response);
            for (var color in response) {
                var graphData = {
                    name,
                    x: [],
                    y: [],
                    marker: {
                        color: ''
                    }
                };
                graphData['name'] = color;
                if (color == "Yellow 70-79") {
                    graphData['marker']['color'] = yellowColor;
                } else if (color == "Red 50-69") {
                    graphData['marker']['color'] = redColor;
                }
                if (color == "Green 80-100") {
                    graphData['marker']['color'] = greenColor;
                }
                if (color == "Black 0-49") {
                    graphData['marker']['color'] = blackColor;
                }
                for (var year in response[color]) {
                    graphData['x'].push(year);
                    graphData['y'].push(response[color][year]);
                    // console.log(response[color][year]);
                }
                lineGraphData2.push(graphData);

            }
            console.log(graphData);
            //console.log(lineGraphData)

            document.getElementById("progress_container").style.display = 'none';

            Plotly.newPlot(lineGraphDiv2, lineGraphData2, {
                yaxis: {
                    title: 'Number of students'
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
        Plotly.newPlot(attendanceBarAll, tempLis2, barLayout, config);
        Plotly.newPlot(barGraphDiv, tempLis, barLayout2, config);
        Plotly.newPlot(lineGraphDiv, lineGraphData, {
            yaxis: {
                title: 'Number of students'
            }
        }, config);
        Plotly.newPlot(lineGraphDiv2, lineGraphData2, {
            yaxis: {
                title: 'Number of students'
            }
        }, config);
    });

    //date picker
    $('.datepickerFrom').pickadate({
        selectMonths: true, // Creates a dropdown to control month
        selectYears: 15, // Creates a dropdown of 15 years to control year,
        today: 'Today',
        clear: 'Clear',
        format: 'yyyy-mm-dd',
        close: 'Ok',
        closeOnSelect: true // Close upon selecting a date,
    });
    $('.datepickerTo').pickadate({
        selectMonths: true, // Creates a dropdown to control month
        selectYears: 15, // Creates a dropdown of 15 years to control year,
        today: 'Today',
        clear: 'Clear',
        format: 'yyyy-mm-dd',
        close: 'Ok',
        closeOnSelect: true // Close upon selecting a date,
    });
    $('.datepickerFrom2').pickadate({
        selectMonths: true, // Creates a dropdown to control month
        selectYears: 15, // Creates a dropdown of 15 years to control year,
        today: 'Today',
        clear: 'Clear',
        format: 'yyyy-mm-dd',
        close: 'Ok',
        closeOnSelect: true // Close upon selecting a date,
    });
    $('.datepickerTo2').pickadate({
        selectMonths: true, // Creates a dropdown to control month
        selectYears: 15, // Creates a dropdown of 15 years to control year,
        today: 'Today',
        clear: 'Clear',
        format: 'yyyy-mm-dd',
        close: 'Ok',
        closeOnSelect: true // Close upon selecting a date,
    });
    $('.datepickerFrom3').pickadate({
        selectMonths: true, // Creates a dropdown to control month
        selectYears: 15, // Creates a dropdown of 15 years to control year,
        today: 'Today',
        clear: 'Clear',
        format: 'yyyy-mm-dd',
        close: 'Ok',
        closeOnSelect: true // Close upon selecting a date,
    });
    $('.datepickerTo3').pickadate({
        selectMonths: true, // Creates a dropdown to control month
        selectYears: 15, // Creates a dropdown of 15 years to control year,
        today: 'Today',
        clear: 'Clear',
        format: 'yyyy-mm-dd',
        close: 'Ok',
        closeOnSelect: true // Close upon selecting a date,
    });


    $('select').material_select();


    $("input[name$='time_selection']").click(function () {
        var selected = $(this).val();
        console.log(selected);
        if (selected == 'time_term_year') {

            $('.datepickerFrom').attr('disabled', true);
            $('.datepickerTo').attr('disabled', true);

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

    $("input[name$='time_selection_3']").click(function () {
        var selected = $(this).val();
        console.log(selected);
        if (selected == 'time_term_year_3') {

            $('.datepickerFrom3').attr('disabled', true);
            $('.datepickerTo3').attr('disabled', true);

            $('#term-select_to_3').attr('disabled', false);
            $('#term-select_from_3').attr('disabled', false);
            $('#select_years_to_3').attr('disabled', false);
            $('#select_years_from_3').attr('disabled', false);
            $('select').material_select();

        } else if (selected == 'time_selected_3') {

            $('.datepickerFrom3').attr('disabled', false);
            $('.datepickerTo3').attr('disabled', false);


            $('#term-select_to_3').attr('disabled', true);
            $('#term-select_from_3').attr('disabled', true);
            $('#select_years_to_3').attr('disabled', true);
            $('#select_years_from_3').attr('disabled', true);
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
});