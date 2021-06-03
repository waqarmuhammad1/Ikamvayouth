$(document).ready(function () {

    $("progress_container").hide();
    document.getElementById("progress_container").style.display = 'none';
    // var colors = [ 'rgba(158, 27, 72, 0.9)', 'rgba(255, 10, 50, 0.9)', 'rgba(86, 23, 148, 0.9)', 'rgba(62, 146, 2, 0.9)', 'rgba(7, 160, 163, 0.9)', 'rgba(146, 137, 24, 0.9)', 'rgba(111, 24, 170, 0.9)','rgba(0,174,219,0.9)','rgba(162,0,255,0.9)','rgba(0,0,0,0.9)','rgba(212,18,67,0.9)','rgba(96,35,32,0.9)','rgba(243,119,53,0.9)','rgba(209,17,65,0.9)','rgba(0,177,89,0.9)','rgba(55,56,84,0.9)','rgba(255, 51, 159 ,0.9)','rgba(245, 61, 61  ,0.9)','rgba(36, 113, 163,0.9)','rgba(125, 206, 160,0.9)','rgba(120, 40, 31  ,0.9)','rgba(156, 109, 50 ,0.9)','rgba(71, 156, 50,0.9)','rgba(156, 50, 82,0.9)','rgba(31, 255, 12,0.9)', 'rgba(157, 142, 12, 0.9)','rgba(151, 60, 110, 0.9)', 'rgba(173, 167, 15, 0.9)', 'rgba(71, 24, 135, 0.9)', 'rgba(155, 106, 42, 0.9)', 'rgba(33, 17, 132, 0.9)', 'rgba(163, 2, 88, 0.9)', 'rgba(25, 139, 83, 0.9)', 'rgba(118, 85, 31, 0.9)', 'rgba(156, 123, 29, 0.9)', 'rgba(146, 7, 120, 0.9)', 'rgba(100, 129, 36, 0.9)', 'rgba(144, 22, 128, 0.9)', 'rgba(18, 105, 154, 0.9)', 'rgba(64, 139, 14, 0.9)', 'rgba(59, 174, 4, 0.9)', 'rgba(138, 171, 9, 0.9)', 'rgba(20, 147, 32, 0.9)', 'rgba(95, 22, 150, 0.9)', 'rgba(121, 61, 40, 0.9)', 'rgba(30, 136, 78, 0.9)', 'rgba(62, 48, 152, 0.9)', 'rgba(92, 32, 150, 0.9)', 'rgba(44, 136, 134, 0.9)', 'rgba(62, 62, 143, 0.9)', 'rgba(126, 87, 31, 0.9)', 'rgba(146, 52, 60, 0.9)', 'rgba(32, 141, 15, 0.9)', 'rgba(6, 173, 103, 0.9)', 'rgba(114, 127, 36, 0.9)', 'rgba(34, 123, 21, 0.9)', 'rgba(142, 16, 116, 0.9)', 'rgba(55, 162, 47, 0.9)', 'rgba(83, 160, 11, 0.9)', 'rgba(2, 178, 138, 0.9)', 'rgba(132, 20, 125, 0.9)', 'rgba(168, 13, 77, 0.9)', 'rgba(18, 100, 128, 0.9)', 'rgba(80, 167, 33, 0.9)', 'rgba(36, 123, 38, 0.9)', 'rgba(44, 15, 165, 0.9)', 'rgba(66, 32, 175, 0.9)', 'rgba(120, 107, 25, 0.9)', 'rgba(24, 170, 44, 0.9)', 'rgba(163, 44, 26, 0.9)', 'rgba(134, 42, 101, 0.9)', 'rgba(37, 32, 133, 0.9)', 'rgba(22, 143, 10, 0.9)', 'rgba(77, 154, 40, 0.9)', 'rgba(38, 124, 155, 0.9)', 'rgba(92, 162, 16, 0.9)', 'rgba(7, 150, 132, 0.9)', 'rgba(140, 172, 0, 0.9)', 'rgba(24, 68, 121, 0.9)', 'rgba(150, 149, 12, 0.9)', 'rgba(86, 140, 36, 0.9)', 'rgba(43, 128, 142, 0.9)', 'rgba(7, 35, 167, 0.9)', 'rgba(61, 149, 136, 0.9)', 'rgba(153, 83, 38, 0.9)', 'rgba(130, 3, 147, 0.9)', 'rgba(145, 12, 29, 0.9)', 'rgba(98, 123, 37, 0.9)', 'rgba(54, 64, 142, 0.9)', 'rgba(136, 25, 125, 0.9)', 'rgba(163, 56, 30, 0.9)', 'rgba(3, 122, 162, 0.9)', 'rgba(46, 160, 36, 0.9)', 'rgba(8, 17, 160, 0.9)', 'rgba(179, 67, 16, 0.9)', 'rgba(136, 146, 42, 0.9)', 'rgba(133, 16, 144, 0.9)', 'rgba(14, 49, 170, 0.9)', 'rgba(42, 39, 162, 0.9)', 'rgba(179, 35, 112, 0.9)', 'rgba(32, 164, 74, 0.9)', 'rgba(150, 139, 47, 0.9)', 'rgba(63, 94, 148, 0.9)', 'rgba(112, 148, 6, 0.9)', 'rgba(4, 144, 152, 0.9)', 'rgba(57, 133, 142, 0.9)', 'rgba(78, 166, 29, 0.9)', 'rgba(107, 165, 15, 0.9)', 'rgba(54, 140, 69, 0.9)', 'rgba(23, 42, 176, 0.9)', 'rgba(153, 57, 76, 0.9)', 'rgba(58, 146, 62, 0.9)', 'rgba(132, 150, 50, 0.9)', 'rgba(70, 39, 124, 0.9)', 'rgba(173, 21, 79, 0.9)', 'rgba(7, 178, 45, 0.9)', 'rgba(141, 25, 158, 0.9)', 'rgba(121, 141, 33, 0.9)', 'rgba(115, 147, 40, 0.9)', 'rgba(34, 166, 136, 0.9)', 'rgba(49, 125, 144, 0.9)', 'rgba(99, 32, 143, 0.9)', 'rgba(48, 80, 160, 0.9)'];
    var config = {
        modeBarButtonsToRemove: ['autoScale2d', 'resetScale2d',
            'hoverClosestCartesian', 'hoverCompareCartesian', 'zoom2d', 'pan2d', 'select2d', 'lasso2d', 'zoomIn2d', 'zoomOut2d'
        ],
        displaylogo: false
    };

    var $branches = $("#branches-select");
    var $branches2 = $("#branches-select2");
    var $year = $("#year-select");
    var $year2 = $("#year-select2");
    var $year3 = $("#year-select3");


    var $schools = $("#schools-select");
    var $schools2 = $("#schools-select2");
    var barGraphDiv = document.getElementById("gradeBar");
    var barGraphDivAll = document.getElementById("gradeBarAll");
    var lineGraphDiv = document.getElementById("gradeLine");
    var barLayout;
    var yearlist2 = [];
    var allschools = [];
    var allbranches = [];

    function ajaxCallsFunc(type, url, contentType, data, callback) {
        $.ajax({
            type: type,
            url: url,
            contentType: contentType,
            data: data,
            success: callback
        });
    }
    var dummydata = JSON.stringify({
        "filesList": ["2017.xlsx"],
        "instituteList": ["Makhaza"],
        "filterType": ["Branch"],
        "flag": 13,
        "yearslist": ["2017"]
    });
    var dummydata3 = JSON.stringify({
        "filesList": ["2017.xlsx"],
        "instituteList": ["Makhaza"],
        "filterType": ["Branch"],
        "flag": 16,
        "yearslist": ["2017"]
    });



    ajaxCallsFunc('POST', "http://41.164.192.98:5000/TrackingGraph", 'application/json', dummydata3, function (branches) {
        console.log(branches);
        $.each(branches, function (i, branch) {
            $branches.append('<option value="' + branch + '">' + branch + '</option>');
            $branches.material_select();
            $branches2.append('<option value="' + branch + '">' + branch + '</option>');
            $branches2.material_select();
            allbranches.push(branch);
        });
    });


    ajaxCallsFunc('POST', "http://41.164.192.98:5000/TrackingGraph", 'application/json', dummydata, function (schools) {
        console.log(schools);
        $.each(schools, function (i, school) {
            $schools.append('<option value="' + school + '">' + school + '</option>');
            $schools.material_select();
            $schools2.append('<option value="' + school + '">' + school + '</option>');
            $schools2.material_select();
            allschools.push(school);
        });
    });
    ajaxCallsFunc('POST', "http://41.164.192.98:5000/GetYears", 'application/json', null, function (years) {
        $.each(years, function (i, year) {
            $year.append('<option value="' + year + '">' + year + '</option>');
            $year.material_select();
            $year2.append('<option value="' + year + '">' + year + '</option>');
            $year2.material_select();
            $year3.append('<option value="' + year + '">' + year + '</option>');
            $year3.material_select();
        });
    });


    var tempLis = [];
    var graphAll = [];
    var branchList = [];
    $("#drawgraph").click(function () {
        document.getElementById("progress_container").style.display = 'block';
        graphAll = [];
        tempLis2 = [];
        tempLis = [];
        var filtertype = $('input[name=group1]:checked').val();
        if (filtertype == "Branch") {
            branchList = $("#branches-select").val();
        } else if (filtertype == "allbranches") {
            filtertype = "Branch";
            branchList = allbranches;
        } else if (filtertype == "School Attending") {
            branchList = $("#schools-select").val();
        } else if (filtertype == "allschools") {
            filtertype = "School Attending";
            branchList = allschools;
        }

        var flag = $("#options-select").val();
        var filesList = [];
        var yearlist = $("#year-select").val();



        for (var year in yearlist) {
            filesList.push(yearlist[year] + ".xlsx");
        }
        if (flag == 3) {
            var dummydata = JSON.stringify({
                "filesList": filesList,
                "instituteList": branchList,
                "filterType": filtertype,
                "flag": 14,
                "yearslist": yearlist
            });
            ajaxCallsFunc('POST', "http://41.164.192.98:5000/TrackingGraph", 'application/json', dummydata, function (response) {
                console.log(response);
                $('#data').text("");
                $('#heading').text("Number of students applied nowhere:");
                $.each(response, function (i, response) {
                    $('#data').append(i + ': ' + response + '<br>')
                });
            });
            var dummydata2 = JSON.stringify({
                "filesList": filesList,
                "instituteList": branchList,
                "filterType": filtertype,
                "flag": 15,
                "yearslist": yearlist
            });
            ajaxCallsFunc('POST', "http://41.164.192.98:5000/TrackingGraph", 'application/json', dummydata2, function (response) {
                console.log(response);
                $('#data2').text("");
                $('#heading2').text("Average number of applications per student:");
                $.each(response, function (i, response) {
                    $('#data2').append(i + ': ' + response + '<br>')
                });
            });

        }
        //      alert(filesList+ branchList+ filtertype+flag+ yearlist);
        var data2 = JSON.stringify({
            "filesList": filesList,
            "instituteList": allbranches,
            "filterType": "Branch",
            "flag": parseInt(flag),
            "yearslist": yearlist
        });
        // alert(data2);
        ajaxCallsFunc('POST', "http://41.164.192.98:5000/TrackingGraph", 'application/json', data2, function (response) {
            console.log(response);
            var i = 0;
            var dic = {};
            for (var keys in response) {
                for (var branch in response[keys]) {
                    if (branch in dic) {
                        var temp = dic[branch]
                        temp += response[keys][branch]
                        dic[branch] = temp

                    } else {
                        dic[branch] = response[keys][branch]
                    }
                }
            }
            branchCount = 0;
            discardList = []
            for(var key in dic){
                if(dic[key] > 0){
                    branchCount++;
                }
                else{
                    discardList.push(key)
                }
            }

            
            for (var reason in response) {
                var y = 0;
                var graphData = {
                    name,
                    x: [],
                    y: [],
                    type: 'bar',
                    marker: {
                        width: 1
                    }
                };
                graphData['name'] = reason;
                var count = 0;
                //graphData['marker']['color'] = colors[i];
                for (var branch in response[reason]) {
                    // count +=1;
                    graphData['x'].push("All branches");
                    y += response[reason][branch];

                }
                y = (y / branchCount);
                graphData['y'].push(y);
                graphAll.push(graphData);
                i++;
            }
            Plotly.newPlot(barGraphDivAll, graphAll, {
                showlegend: false,
                barmode: 'stack',
                yaxis: {
                    title: '% of students',
                    range: [0, 100]
                }
            }, config);
        });

        var data = JSON.stringify({
            "filesList": filesList,
            "instituteList": branchList,
            "filterType": filtertype,
            "flag": parseInt(flag),
            "yearslist": yearlist
        });
        var flagtext = $("#options-select option:selected").text();
        //console.log(flagtext);
        var title1 = "Grade 12 Tracking, " + flagtext + " Years:"+ yearlist;
        ajaxCallsFunc('POST', "http://41.164.192.98:5000/TrackingGraph", 'application/json', data, function (response) {
            console.log(response);
            var i = 0;
            var dic = {};
            for (var keys in response) {
                for (var branch in response[keys]) {
                    if (branch in dic) {
                        var temp = dic[branch]
                        temp += response[keys][branch]
                        dic[branch] = temp

                    } else {
                        dic[branch] = response[keys][branch]
                    }
                }
            }
            branchCount = 0;
            discardList = []
            for(var key in dic){
                if(dic[key] > 0){
                    branchCount++;
                }
                else{
                    discardList.push(key)
                }
            }
            for (var reason in response) {
                var graphData = {
                    name,
                    x: [],
                    y: [],
                    type: 'bar',
                    marker: {
                        width: 1,


                    }
                };
                graphData['name'] = reason;
                // graphData['marker']['color'] = colors[i];
                for (var branch in response[reason]) {
                    if(discardList.includes(branch)){
                        continue;
                    }
                    graphData['x'].push(branch);
                    graphData['y'].push(response[reason][branch]);
                }
                tempLis.push(graphData);
                i++;
            }
            barLayout = {
                barmode: 'stack',
                yaxis: {
                    title: '% of students',
                    range: [0, 100]
                },
                title: title1
            };
            document.getElementById("progress_container").style.display = 'none';
            Plotly.newPlot(barGraphDiv, tempLis, barLayout, config);
        });
    });
    //line graph
    var lineGraphData = [];
    $("#drawgraph2").click(function () {
        document.getElementById("progress_container").style.display = 'block';
        lineGraphData = [];

        var filtertype = $('input[name=group2]:checked').val();
        if (filtertype == "Branch") {
            var branchList = $("#branches-select2").val();
        } else if (filtertype == "allbranches") {
            filtertype = "Branch";
            branchList = allbranches;
        } else if (filtertype == "School Attending") {
            branchList = $("#schools-select2").val();
        } else if (filtertype == "allschools") {
            filtertype = "School Attending";
            branchList = allschools;
        }
        var flag = $("#options-select2").val();

        var yearFrom = $("#year-select2").val();
        var yearTo = $("#year-select3").val();
        var filesList = [];

        filesList.push(yearFrom + ".xlsx");
        filesList.push(yearTo + ".xlsx");

        console.log(filesList, branchList, filtertype, flag, yearFrom, yearTo);


        var flagtext = $("#options-select2 option:selected").text();

        var title2 = "Grade 12 Tracking, " + flagtext + " Years: " + yearFrom +"-" +yearTo +"<br>" + branchList ;
        var lineData = JSON.stringify({
            "filesList": filesList,
            "instituteList": branchList,
            "filterType": filtertype,
            "flag": parseInt(flag),
            "YearFrom": parseInt(yearFrom),
            "YearTo": parseInt(yearTo)
        });

        ajaxCallsFunc('POST', "http://41.164.192.98:5000/TrackingGraph", 'application/json', lineData, function (response) {
            console.log(response);
            var i = 0;
            for (var category in response) {
                var graphData = {
                    name,
                    x: [],
                    y: [],
                    marker: {
                        width: 1,


                    }
                };
                graphData['name'] = category;
                //   graphData['marker']['color'] = colors[i];
                //     console.log(category + "<-- category");
                for (var year in response[category]) {
                    //       console.log(year + "<-- year");

                    graphData['x'].push(year);
                    graphData['y'].push(response[category][year]);
                }
                lineGraphData.push(graphData);
                i++;
            }
            // console.log(graphData);
            // console.log(lineGraphData)
            document.getElementById("progress_container").style.display = 'none';
            Plotly.newPlot(lineGraphDiv, lineGraphData, {
                yaxis: {
                    title: 'Number of students',

                },
                title: title2,
                titlefont: {
                    size: 12

                },
                xaxis: {

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
        Plotly.newPlot(barGraphDiv, tempLis, barLayout, config);
        Plotly.newPlot(barGraphDivAll, graphAll, {
            showlegend: false,
            barmode: 'stack',
            yaxis: {
                title: '% of students',
                range: [0, 100]
            }
        }, config);
        Plotly.newPlot(lineGraphDiv, lineGraphData, config);

    });
    //date picker
    $('.datepickerFrom').pickadate({
        selectMonths: true, // Creates a dropdown to control month
        selectYears: 15, // Creates a dropdown of 15 years to control year,
        today: 'Today',
        clear: 'Clear',
        close: 'Ok',
        closeOnSelect: false // Close upon selecting a date,
    });
    $('.datepickerTo').pickadate({
        selectMonths: true, // Creates a dropdown to control month
        selectYears: 15, // Creates a dropdown of 15 years to control year,
        today: 'Today',
        clear: 'Clear',
        close: 'Ok',
        closeOnSelect: false // Close upon selecting a date,
    });

    $('.datepickerFrom2').pickadate({
        selectMonths: true, // Creates a dropdown to control month
        selectYears: 15, // Creates a dropdown of 15 years to control year,
        today: 'Today',
        clear: 'Clear',
        close: 'Ok',
        closeOnSelect: false // Close upon selecting a date,
    });
    $('.datepickerTo2').pickadate({
        selectMonths: true, // Creates a dropdown to control month
        selectYears: 15, // Creates a dropdown of 15 years to control year,
        today: 'Today',
        clear: 'Clear',
        close: 'Ok',
        closeOnSelect: false // Close upon selecting a date,
    });



    $('select').material_select();


    // document.getElementById('myFile').onchange = function () {
    //     $("#year").hide();
    //     $("#year2").hide();
    //     var a = this.files;

    //     var temp;
    //     for (var item in a) {
    //         if (a[item].type == "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet" || a[item].type == "application/vnd.ms-excel") {
    //             temp = a[item].name;
    //             selectedFiles.push(a[item].name);
    //             console.log(temp);
    //             var temp2 = temp.split('.');
    //             yearlist2.push(temp2[0]);
    //             $year.append('<option value="' + temp2[0] + '">' + temp2[0] + '</option>');
    //             $year2.append('<option value="' + temp2[0] + '">' + temp2[0] + '</option>');
    //             $year3.append('<option value="' + temp2[0] + '">' + temp2[0] + '</option>');
    //             $year.material_select();
    //             $year2.material_select();
    //             $year3.material_select();
    //         }
    //     }
    // };
});